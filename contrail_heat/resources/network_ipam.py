from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import uuid


class HeatNetworkIpam(contrail.ContrailResource):
    PROPERTIES = (
        NAME,
    ) = (
        'name',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Network IPAM name'),
            update_allowed=True,
        ),
        # TODO add other properties as need arises
    }

    attributes_schema = {
        "name": _("The name of the Network IPAM."),
        "fq_name": _("The FQ name of the Network IPAM."),
        "show": _("All attributes."),
    }

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        ni_obj = vnc_api.NetworkIpam(name=self.properties[self.NAME],
                                     parent_obj=project_obj)
        ni_uuid = self.vnc_lib().network_ipam_create(ni_obj)
        self.resource_id_set(ni_uuid)

    def _show_resource(self):
        ni_obj = self.vnc_lib().network_ipam_read(id=self.resource_id)
        dic = {}
        dic['name'] = ni_obj.get_display_name()
        dic['fq_name'] = ni_obj.get_fq_name_str()
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().network_ipam_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::NetworkIpam': HeatNetworkIpam,
    }
