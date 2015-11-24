import uuid

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailVirtualNetwork(contrail.ContrailResource):
    PROPERTIES = (
        NAME, ROUTE_TARGETS, SHARED, EXTERNAL, ALLOW_TRANSIT,
        FORWARDING_MODE
    ) = (
        'name', 'route_targets', 'shared', 'external', 'allow_transit',
        'forwarding_mode'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Network name.'),
            update_allowed=True,
        ),
        ROUTE_TARGETS: properties.Schema(
            properties.Schema.LIST,
            _('Route Targets list.'),
            default=[],
            update_allowed=True,
        ),
        SHARED: properties.Schema(
            properties.Schema.STRING,
            _('Whether this network should be shared across all tenants. '
              'Note that the default policy setting restricts usage of this '
              'attribute to administrative users only.'),
            default='False',
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=True
        ),
        EXTERNAL: properties.Schema(
            properties.Schema.STRING,
            _('Whether this network should be external.'),
            default='False',
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=True
        ),
        ALLOW_TRANSIT: properties.Schema(
            properties.Schema.STRING,
            _('Whether this network should be transitive.'),
            default='False',
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=True
        ),
        FORWARDING_MODE: properties.Schema(
            properties.Schema.STRING,
            _('Forwarding mode of this network.'),
            default='l2_l3',
            constraints=[
                constraints.AllowedValues(['l2_l3', 'l2']),
            ],
            update_allowed=True
        ),
    }
    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "fq_name": _("The FQ name of the Virtual Network."),
        "route_targets": _("Route Targets list."),
        "shared": _("shared across all tenants."),
        "external": _("external."),
        "allow_transit": _("allow_transit."),
        "forwarding_mode": _("forwarding_mode."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        vn_obj = vnc_api.VirtualNetwork(name=self.properties[self.NAME],
                                        parent_obj=project_obj)
        vn_params = vnc_api.VirtualNetworkType()
        if self.properties[self.ALLOW_TRANSIT] == "True":
            vn_params.set_allow_transit(True)
        else:
            vn_params.set_allow_transit(False)
        vn_params.set_forwarding_mode(self.properties[self.FORWARDING_MODE])
        vn_obj.set_virtual_network_properties(vn_params)
        vn_obj.set_route_target_list(vnc_api.RouteTargetList(
            ["target:" + route for route in self.properties[
                self.ROUTE_TARGETS]]))
        if self.properties[self.SHARED] == "True":
            vn_obj.set_is_shared(True)
        else:
            vn_obj.set_is_shared(False)
        if self.properties[self.EXTERNAL] == "True":
            vn_obj.set_router_external(True)
        else:
            vn_obj.set_router_external(False)
        vn_uuid = self.vnc_lib().virtual_network_create(vn_obj)
        if self.properties[self.FLOOD_UNKNOWN_UNICAST] == "True":
            vn_obj.set_flood_unknown_unicast(True)
        else:
            vn_obj.set_flood_unknown_unicast(False)
        vn_uuid = super(ContrailVirtualNetwork, self).resource_create(vn_obj)
        self.resource_id_set(vn_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            vn_obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        except Exception as ex:
            LOG.warn(_("Virtual Network %s not found.") % self.name)
            raise ex

        vn_params = vnc_api.VirtualNetworkType()

        if prop_diff.get(self.ALLOW_TRANSIT) == "True":
            vn_params.set_allow_transit(True)
        else:
            vn_params.set_allow_transit(False)

        if prop_diff.get(self.SHARED) == "True":
            vn_obj.set_is_shared(True)
        else:
            vn_obj.set_is_shared(False)

        if prop_diff.get(self.EXTERNAL) == "True":
            vn_obj.set_router_external(True)
        else:
            vn_obj.set_router_external(False)

        fwd_mode = prop_diff.get(self.FORWARDING_MODE)
        if fwd_mode:
            vn_params.set_forwarding_mode(fwd_mode)

        vn_obj.set_virtual_network_properties(vn_params)

        rt_list = prop_diff.get(self.ROUTE_TARGETS)
        if rt_list:
            vn_obj.set_route_target_list(vnc_api.RouteTargetList(
                ["target:" + route for route in rt_list]))
 
        if prop_diff.get(self.FLOOD_UNKNOWN_UNICAST) == "True":
            vn_obj.set_flood_unknown_unicast(True)
        else:
            vn_obj.set_flood_unknown_unicast(False)
        self.vnc_lib().virtual_network_update(vn_obj)

    def _show_resource(self):
        vn_obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        rts = vn_obj.get_route_target_list().get_route_target()
        attrs = {
            'fq_name': vn_obj.get_fq_name_str(),
            'name': vn_obj.get_fq_name()[-1],
            'route_targets': [
                (rt[7:] if rt.startswith('target:') else rt) for rt in rts
            ],
            'shared': vn_obj.get_is_shared(),
            'external': vn_obj.get_router_external(),
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
