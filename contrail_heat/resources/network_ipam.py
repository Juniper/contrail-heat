try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
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
        "name": attributes.Schema(
            _('The name of the Network IPAM..'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the Network IPAM.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }
    
    @contrail.set_auth_token
    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        ni_obj = vnc_api.NetworkIpam(name=self.properties[self.NAME],
                                     parent_obj=project_obj)
        ni_uuid = super(HeatNetworkIpam, self).resource_create(ni_obj)
        self.resource_id_set(ni_uuid)

    @contrail.set_auth_token
    def _show_resource(self):
        ni_obj = self.vnc_lib().network_ipam_read(id=self.resource_id)
        dic = {}
        dic['name'] = ni_obj.get_display_name()
        dic['fq_name'] = ni_obj.get_fq_name_str()
        return dic

    @contrail.set_auth_token
    def handle_delete(self):
        try:
            self.vnc_lib().network_ipam_delete(id=self.resource_id)
        except Exception:
            pass

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::NetworkIpam': HeatNetworkIpam,
    }
