try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import properties
from heat.engine import constraints
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid


class HeatVirtualMachineInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, VIRTUAL_MACHINE_INTEFRACE_MAC_ADDRESSES, VIRTUAL_NETWORKS,
    ) = (
        'name', 'virtual_machine_interface_mac_addresses', 'virtual_networks',
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
        # TODO add additional properties which are currently needed
    }

    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "fq_name": _("The FQ name of the Virtual Network."),
        "virtual_machine_interface_mac_addresses": _("List of mac addresses."),
        "virtual_networks": _("List of virtual networks FQ names."),
        "show": _("All attributes."),
    }

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        vmi_obj = vnc_api.VirtualMachineInterface(
            name=self.properties[self.NAME], parent_obj=project_obj)
        vmi_obj.set_virtual_machine_interface_mac_addresses(
            vnc_api.MacAddressesType(
                self.properties[self.VIRTUAL_MACHINE_INTEFRACE_MAC_ADDRESSES]))
        for network in self.properties[self.VIRTUAL_NETWORKS]:
            vn_obj = self.vnc_lib().virtual_network_read(id=network)
            vmi_obj.add_virtual_network(vn_obj)
        vmi_uuid = self.vnc_lib().virtual_machine_interface_create(vmi_obj)

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

    def _show_resource(self):
        vmi_obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        dic = {}
        dic['name'] = vmi_obj.get_display_name()
        dic['fq_name'] = vmi_obj.get_fq_name_str()
        dic['virtual_machine_interface_mac_addresses'] = (
            vmi_obj.get_virtual_machine_interface_mac_addresses().
            get_mac_address())
        dic['virtual_networks'] = (
            [vn['to'] for vn in vmi_obj.get_virtual_network_refs() or []])
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().virtual_machine_interface_delete(
                id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::VirtualMachineInterface': HeatVirtualMachineInterface,
    }
