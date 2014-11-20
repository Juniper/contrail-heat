import uuid

from contrail_heat.resources import contrail
from heat.common.i18n import _
from heat.engine import properties
from heat.engine import constraints
from heat.openstack.common import log as logging
from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailVirtualNetwork(contrail.ContrailResource):
    PROPERTIES = (
        NAME, ROUTE_TARGETS
    ) = (
        'name', 'route_targets'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Network name.'),
            update_allowed=False,
        ),
        ROUTE_TARGETS: properties.Schema(
            properties.Schema.LIST,
            _('Route Targets list.'),
            default=[],
        ),
    }

    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "fq_name": _("The FQ name of the Virtual Network."),
        "route_targets": _("Route Targets list."),
        "show": _("All attributes."),
    }

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        vn_obj = vnc_api.VirtualNetwork(name=self.properties[self.NAME],
                                        parent_obj=project_obj)
        vn_params = vnc_api.VirtualNetworkType()
        vn_params.set_forwarding_mode('l2_l3')
        vn_obj.set_virtual_network_properties(vn_params)
        vn_obj.set_route_target_list(vnc_api.RouteTargetList(
            ["target:" + route for route in self.properties[
                self.ROUTE_TARGETS]]))
        vn_uuid = self.vnc_lib().virtual_network_create(vn_obj)
        self.resource_id_set(vn_uuid)

    def _show_resource(self):
        vn_obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        rts = vn_obj.get_route_target_list().get_route_target()
        attrs = {
            'fq_name': vn_obj.get_fq_name_str(),
            'name': vn_obj.get_fq_name()[-1],
            'route_targets': [
                (rt[7:] if rt.startswith('target:') else rt) for rt in rts
            ],
        }
        return attrs

    def handle_delete(self):
        if self.resource_id is not None:
            try:
                self.vnc_lib().virtual_network_delete(id=self.resource_id)
            except Exception as ex:
                self._ignore_not_found(ex)
                LOG.warn(_("Virtual Network %s already deleted.") % self.name)


def resource_mapping():
    return {
        'OS::Contrail::VirtualNetwork': ContrailVirtualNetwork,
    }
