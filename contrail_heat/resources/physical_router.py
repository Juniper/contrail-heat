try:
    from heat.common.i18n import _
except ImportError:
    pass

from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid


class HeatPhysicalRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME,
    ) = (
        'name',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Physical Router name'),
            update_allowed=True,
        ),
    }

    attributes_schema = {
        "name": _("The name of the Physical Router."),
        "fq_name": _("The FQ name of the Physical Router."),
        "physical_interfaces": _("List of Physical Interfaces attached."),
        "show": _("All attributes."),
    }

    def handle_create(self):
        config_obj = self.vnc_lib().global_system_config_read(
            fq_name=["default-global-system-config"])
        pr_obj = vnc_api.PhysicalRouter(name=self.properties[self.NAME],
                                        parent_obj=config_obj)
        pr_uuid = self.vnc_lib().physical_router_create(pr_obj)
        self.resource_id_set(pr_uuid)

    def _show_resource(self):
        pr_obj = self.vnc_lib().physical_router_read(id=self.resource_id)
        dic = {}
        dic['name'] = pr_obj.get_display_name()
        dic['fq_name'] = pr_obj.get_fq_name_str()
        dic['physical_interfaces'] = (
            [pi['to'] for pi in pr_obj.get_physical_interfaces() or []])
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().physical_router_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::PhysicalRouter': HeatPhysicalRouter,
    }
