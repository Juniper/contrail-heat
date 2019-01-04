try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import properties
from heat.engine import constraints
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid


class HeatVirtualMachineInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, VIRTUAL_MACHINE_INTEFRACE_MAC_ADDRESSES, VIRTUAL_NETWORKS,
        PORT_TUPLES, SERVICE_INTERFACE_TYPE
    ) = (
        'name', 'virtual_machine_interface_mac_addresses', 'virtual_networks',
        'port_tuples', 'service_interface_type'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Machine Interface name'),
            update_allowed=True,
        ),
        VIRTUAL_MACHINE_INTEFRACE_MAC_ADDRESSES: properties.Schema(
            properties.Schema.LIST,
            _('List of mac addresses.'),
            default=[],
            update_allowed=False,  # TODO check if it's allowed
        ),
        VIRTUAL_NETWORKS: properties.Schema(
            properties.Schema.LIST,
            _('List of virtual networks.'),
            default=[],
            update_allowed=False,  # TODO check if it's allowed
        ),
        PORT_TUPLES: properties.Schema(
            properties.Schema.LIST,
            _('List of port tuples.'),
            default=[],
            update_allowed=False,  # TODO check if it's allowed
        ),
        SERVICE_INTERFACE_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('Service Interface Type.'),
            update_allowed=False
        ),
        # TODO add additional properties which are currently needed
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the Virtual Network.'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the Virtual Network.'),
        ),
        "service_interface_type": attributes.Schema(
            _('Service interface type.'),
        ),
        "virtual_machine_interface_mac_addresses": attributes.Schema(
            _('List of mac addresses.'),
        ),
        "virtual_networks": attributes.Schema(
            _('List of virtual networks FQ names.'),
        ),
        "port_tuples": attributes.Schema(
            _('List of port tuple FQ names.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    def _get_iip_name(self, pt_obj, vmi_obj, iip_family):
        try:
            si_obj = self.vnc_lib().service_instance_read(id=pt_obj.parent_uuid)
            st_list = si_obj.get_service_template_refs()
            st_obj = self.vnc_lib().service_template_read(id=st_list[0]['uuid'])
            st_props = st_obj.get_service_template_properties()
            st_if_list = st_props.get_interface_type()
        except Exception as e:
            return('-'.join([vmi_obj.uuid, if_type, iip_family]))

        if_type = self.properties[self.SERVICE_INTERFACE_TYPE]
        for vmi_index in range(0, len(st_if_list)):
            if ((if_type == st_if_list[vmi_index].service_interface_type) and
                    (st_if_list[vmi_index].shared_ip)):
                return('-'.join([si_obj.uuid, if_type, str(vmi_index), iip_family]))

        return('-'.join([vmi_obj.uuid, if_type, iip_family]))

    def _allocate_iip_for_family(self, vn_obj, pt_obj, vmi_obj, iip_family):
        iip_name = self._get_iip_name(pt_obj, vmi_obj, iip_family)
        iip_obj = vnc_api.InstanceIp(name=iip_name, instance_ip_family=iip_family)
        iip_obj.add_virtual_network(vn_obj)
        try:
            self.vnc_lib().instance_ip_create(iip_obj)
        except vnc_api.RefsExistError:
            iip_obj = self.vnc_lib().instance_ip_read(fq_name=[iip_name])
        return iip_obj

    @contrail.set_auth_token
    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        vmi_obj = vnc_api.VirtualMachineInterface(
            name=self.properties[self.NAME], parent_obj=project_obj)
        vmi_obj.set_virtual_machine_interface_mac_addresses(
            vnc_api.MacAddressesType(
                self.properties[self.VIRTUAL_MACHINE_INTEFRACE_MAC_ADDRESSES]))
        for network in self.properties[self.VIRTUAL_NETWORKS]:
            try:
                vn_obj = self.vnc_lib().virtual_network_read(id=network)
            except vnc_api.NoIdError:
                vn_obj = self.vnc_lib().virtual_network_read(fq_name_str=network)
            vmi_obj.add_virtual_network(vn_obj)

        for port_tuple in self.properties[self.PORT_TUPLES]:
            try:
                pt_obj = self.vnc_lib().port_tuple_read(id=port_tuple)
            except vnc_api.NoIdError:
                pt_obj = self.vnc_lib().port_tuple_read(fq_name_str=port_tuple)
            vmi_obj.add_port_tuple(pt_obj)
        vmi_props = vnc_api.VirtualMachineInterfacePropertiesType()
        vmi_props.set_service_interface_type(self.properties[self.SERVICE_INTERFACE_TYPE])
        vmi_obj.set_virtual_machine_interface_properties(vmi_props)
        vmi_uuid = super(HeatVirtualMachineInterface, self).resource_create(vmi_obj) 

        iip_obj = self._allocate_iip_for_family(vn_obj, pt_obj, vmi_obj, 'v4')
        iip_obj.add_virtual_machine_interface(vmi_obj)
        self.vnc_lib().instance_ip_update(iip_obj)

        self.resource_id_set(vmi_uuid)

    @contrail.set_auth_token
    def _show_resource(self):
        vmi_obj = self.vnc_lib().virtual_machine_interface_read(id=self.resource_id)
        dic = {}
        dic['name'] = vmi_obj.get_display_name()
        dic['fq_name'] = vmi_obj.get_fq_name_str()
        dic['service_interface_type'] = \
            vmi_obj.get_virtual_machine_properties.get_service_interface_type()
        dic['virtual_machine_interface_mac_addresses'] = (
            vmi_obj.get_virtual_machine_interface_mac_addresses().
            get_mac_address())
        dic['virtual_networks'] = (
            [vn['to'] for vn in vmi_obj.get_virtual_network_refs() or []])
        dic['port_tuples'] = (
            [pt['to'] for pt in vmi_obj.get_port_tuple_refs() or []])
        return dic

    @contrail.set_auth_token
    def handle_delete(self):
        if not self.resource_id:
            return
        try:
            vmi_obj = self.vnc_lib().virtual_machine_interface_read(id=self.resource_id)
        except Exception:
            return

        for iip in vmi_obj.get_instance_ip_back_refs() or []:
            try:
                self.vnc_lib().instance_ip_delete(id=iip['uuid'])
            except vnc_api.NoIdError:
                pass

        try:
            self.vnc_lib().virtual_machine_interface_delete(
                id=self.resource_id)
        except Exception:
            pass

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::VirtualMachineInterface': HeatVirtualMachineInterface,
    }
