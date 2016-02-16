try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import constraints
from novaclient import exceptions as nova_exceptions
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from heat.engine import scheduler
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource
import uuid

LOG = logging.getLogger(__name__)


class HeatRouteTable(ContrailResource):
    PROPERTIES = (
        NAME, SERVICE_INSTANCE, SERVICE_PORT_TAG, ROUTES
    ) = (
        'name', 'service_instance', 'service_port_tag', 'routes'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Route table name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_INSTANCE: properties.Schema(
            properties.Schema.STRING,
            _('Service instance name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_PORT_TAG: properties.Schema(
            properties.Schema.STRING,
            _('Service port tag.'),
            required=True,
            update_allowed=False
        ),
        ROUTES: properties.Schema(
            properties.Schema.LIST,
            _('A specified list of static routes.'),
            default=[],
            update_allowed=True
        ),
    }

    attributes_schema = {
        "name": _("The name of the Route Table."),
        "fq_name": _("The FQ name of the Route Table."),
        "service_instance": _("Service Instance for the Route Table."),
        "service_port_tag": _("Tag for attaching to the corresponding port."),
        "routes": _("List of static routes."),
        "tenant_id": _("Tenant id of the Service Instance."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

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

        route_table = vnc_api.RouteTableType()
        for route in self.properties[self.ROUTES]:
            route_table.add_route(vnc_api.RouteType(prefix=route))
        rt_obj = vnc_api.InterfaceRouteTable(
            name=self.properties[self.NAME], parent_obj=project_obj,
            interface_route_table_routes=route_table)
        rt_obj.set_service_instance(si_obj,
            vnc_api.ServiceInterfaceTag(self.properties[self.SERVICE_PORT_TAG]))
        rt_uuid = self.vnc_lib().interface_route_table_create(rt_obj)
        self.resource_id_set(rt_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            rt_obj = self.vnc_lib().interface_route_table_read(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Route table %s not found.") % self.name)
            raise
        except Exception as e:
            LOG.warn(_("Unknown error %s.") % str(e))
            raise

        route_table = vnc_api.RouteTableType()
        for route in prop_diff.get(self.ROUTES):
            route_table.add_route(vnc_api.RouteType(prefix=route))
        rt_obj.set_interface_route_table_routes(route_table)
        self.vnc_lib().interface_route_table_update(rt_obj)

    def handle_delete(self):
        if not self.resource_id:
            return

        try:
            rt_obj = self.vnc_lib().interface_route_table_read(id=self.resource_id)
        except vnc_api.NoIdError:
            return

        # drop all references
        si_refs = rt_obj.get_service_instance_refs()
        for si in si_refs or []:
            self._vnc_lib.ref_update('interface-route-table', rt_obj.uuid,
                'service-instance', si['uuid'], None, 'DELETE')
        vmi_back_refs = rt_obj.get_virtual_machine_interface_back_refs()
        for vmi in vmi_back_refs or []:
            self._vnc_lib.ref_update('virtual-machine-interface', vmi['uuid'],
                'interface-route-table', rt_obj.uuid, None, 'DELETE')

        # delete rt
        try:
            self.vnc_lib().interface_route_table_delete(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Route Table %s not found.") % self.name)
        except Exception as e:
            LOG.warn(_("Unknown error %s.") % str(e))
            raise

    def _show_resource(self):
        rt_obj = self.vnc_lib().interface_route_table_read(id=self.resource_id)
        si_list = rt_obj.get_service_instance_refs()
        dict = {}
        dict['name'] = rt_obj.get_display_name()
        dict['fq_name'] = rt_obj.get_fq_name_str()
        dict['tenant_id'] = rt_obj.parent_uuid
        dict['routes'] = []
        route_table = rt_obj.get_interface_route_table_routes()
        for route in route_table.get_route():
            dict['routes'].append(route.get_prefix())
        if si_list:
            dict['service_interface_tag'] = si_list[0]['attr'].get_interface_type()
            dict['service_instance'] = si_list[0]['to'][-1]
        return dict


def resource_mapping():
    return {
        'OS::Contrail::RouteTable': HeatRouteTable,
    }
