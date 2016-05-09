try:
    from heat.common.i18n import _
except ImportError:
    pass

from heat.engine import attributes
from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail


class HeatPhysicalInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, PHYSICAL_ROUTER,
    ) = (
        'name', 'physical_router',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Physical interface name'),
            update_allowed=True,
        ),
        PHYSICAL_ROUTER: properties.Schema(
            properties.Schema.STRING,
            _('Physical router id.'),
            default=None,
        ),
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the physical interface.'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the physical interface.'),
        ),
        "logical_interfaces": attributes.Schema(
            _('List of logical interfaces.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    def handle_create(self):
        pr_id = self.properties[self.PHYSICAL_ROUTER]
        if pr_id:
            pr_obj = self.vnc_lib().physical_router_read(id=pr_id)
        else:
            pr_obj = self.vnc_lib().physical_router_read(
                fq_name=["default-global-system-config",
                         "default-physical-router"])
        pi_obj = vnc_api.PhysicalInterface(
            name=self.properties[self.NAME], parent_obj=pr_obj)
        pi_uuid = self.vnc_lib().physical_interface_create(pi_obj)
        self.resource_id_set(pi_uuid)

    def _show_resource(self):
        pi_obj = self.vnc_lib().physical_interface_read(id=self.resource_id)
        dic = {}
        dic['name'] = pi_obj.get_display_name()
        dic['fq_name'] = pi_obj.get_fq_name_str()
        dic['logical_interfaces'] = (
            [li['to'] for li in pi_obj.get_logical_interfaces() or []])
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().physical_interface_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::PhysicalInterface': HeatPhysicalInterface,
    }
