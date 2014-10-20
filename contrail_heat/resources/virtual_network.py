from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid


class HeatVirtualNetwork(contrail.ContrailResource):
    PROPERTIES = (
        NAME,
    ) = (
        'name',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Network name'),
            update_allowed=False,
        ),
    }

    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "fq_name": _("The FQ name of the Virtual Network."),
        "network_id": _("A unique id for the network."),
        "show": _("All attributes."),
    }

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        vn_obj = vnc_api.VirtualNetwork(name=self.properties[self.NAME],
                                        parent_obj=project_obj)
        vn_uuid = self.vnc_lib().virtual_network_create(vn_obj)
        self.resource_id_set(vn_uuid)

    def _show_resource(self):
        vn_obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        dic = {}
        dic['name'] = vn_obj.get_display_name()
        dic['fq_name'] = vn_obj.get_fq_name_str()
        dic['network_id'] = vn_obj.get_network_id()
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().virtual_network_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::VirtualNetwork': HeatVirtualNetwork,
    }
