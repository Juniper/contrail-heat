try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from novaclient import exceptions as nova_exceptions
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from heat.engine import scheduler
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid

LOG = logging.getLogger(__name__)


class HeatPortTuple(contrail.ContrailResource):
    PROPERTIES = (
        NAME, SERVICE_INSTANCE, PORTS
    ) = (
        'name', 'service_instance', 'ports'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Port Tuple name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_INSTANCE: properties.Schema(
            properties.Schema.STRING,
            _('Service Instance name.'),
            required=True,
            update_allowed=False
        ),
        PORTS: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of ports based on template order'),
            required=True,
            update_allowed=False
        ),
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the Port Tuple.'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the Port Tuple.'),
        ),
        "service_instance": attributes.Schema(
            _('Service Instance for the Port Tuple.'),
        ),
        "ports": attributes.Schema(
            _('Service interfaces for the Port Tuple.'),
        ),
        "tenant_id": attributes.Schema(
            _('Tenant id of the Service Instance.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        try:
            si_obj = self.vnc_lib().service_instance_read(
                id=self.properties[self.SERVICE_INSTANCE])
        except vnc_api.NoIdError:
            si_name = project_obj.fq_name + \
                [self.properties[self.SERVICE_INSTANCE]]
            si_obj = self.vnc_lib().service_instance_read(fq_name=si_name)

        pt_obj = vnc_api.PortTuple(
            name=self.properties[self.NAME], parent_obj=si_obj)
        try:
            pt_uuid = self.vnc_lib().port_tuple_create(pt_obj)
        except vnc_api.RefsExistError:
            pt_obj = self.vnc_lib().port_tuple_read(fq_name=pt_obj.fq_name)
            pt_uuid = pt_obj.uuid

        st_uuid = si_obj.get_service_template_refs()[0]['uuid']
        st_obj = self.vnc_lib().service_template_read(id=st_uuid)
        st_props = st_obj.get_service_template_properties()
        if_list = st_props.get_interface_type()
        for index in range(0, len(if_list)):
            port_id = self.properties[self.PORTS][index]
            vmi_obj = self.vnc_lib().virtual_machine_interface_read(id=port_id)
            vmi_props = vnc_api.VirtualMachineInterfacePropertiesType()
            vmi_props.set_service_interface_type(
                if_list[index].get_service_interface_type())
            vmi_obj.set_virtual_machine_interface_properties(vmi_props)
            vmi_obj.add_port_tuple(pt_obj)
            self.vnc_lib().virtual_machine_interface_update(vmi_obj)

        self.resource_id_set(pt_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        pass

    @contrail.set_auth_token
    def handle_delete(self):
        if not self.resource_id:
            return

        try:
            pt_obj = self.vnc_lib().port_tuple_read(id=self.resource_id)
        except vnc_api.NoIdError:
            return

        vmi_back_refs = pt_obj.get_virtual_machine_interface_back_refs()
        for vmi in vmi_back_refs or []:
            self._vnc_lib.ref_update('virtual-machine-interface', vmi['uuid'],
                'port-tuple', pt_obj.uuid, None, 'DELETE')

        try:
            self.vnc_lib().port_tuple_delete(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Port Tuple %s not found.") % self.name)
        except Exception as e:
            LOG.warn(_("Unknown error %s.") % str(e))
            raise

    @contrail.set_auth_token
    def _show_resource(self):
        pt_obj = self.vnc_lib().port_tuple_read(id=self.resource_id)
        si_obj = self.vnc_lib().service_instance_read(id=pt_obj.parent_uuid)
        dict = {}
        dict['name'] = pt_obj.get_display_name()
        dict['fq_name'] = pt_obj.get_fq_name_str()
        dict['tenant_id'] = si_obj.parent_uuid
        dict['service_instance'] = si_obj.get_fq_name_str()
        return dict


def resource_mapping():
    return {
        'OS::Contrail::PortTuple': HeatPortTuple,
    }
