from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail


class HeatLogicalInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, PHYSICAL_INTERFACE, VIRTUAL_NETWORKS,
    ) = (
        'name', 'physical_interface', 'virtual_networks',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Physical interface name'),
            update_allowed=True,
        ),
        PHYSICAL_INTERFACE: properties.Schema(
            properties.Schema.STRING,
            _('Physical interface id.'),
            required=True,
        ),
        VIRTUAL_NETWORKS: properties.Schema(
            properties.Schema.LIST,
            _('Virtual networks list.'),
            default=[],
        ),
    }

    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "fq_name": _("The FQ name of the Virtual Network."),
        "virtual_networks": _('Virtual networks list.'),
        "show": _("All attributes."),
    }

    def handle_create(self):
        pi_obj = self.vnc_lib().physical_interface_read(
            id=self.properties[self.PHYSICAL_INTERFACE])
        li_obj = vnc_api.LogicalInterface(
            name=self.properties[self.NAME], parent_obj=pi_obj)
        for vn in self.properties[self.VIRTUAL_NETWORKS]:
            vn_obj = self.vnc_lib().virtual_network_read(id=vn)
            li_obj.add_virtual_network(vn_obj)
        li_uuid = self.vnc_lib().logical_interface_create(li_obj)
        self.resource_id_set(li_uuid)

    def _show_resource(self):
        li_obj = self.vnc_lib().logical_interface_read(id=self.resource_id)
        dic = {}
        dic['name'] = li_obj.get_display_name()
        dic['fq_name'] = li_obj.get_fq_name_str()
        dic['virtual_networks'] = (
            [li['to'] for li in li_obj.get_virtual_network_refs() or []])
        return dic

    def handle_delete(self):
        try:
            self.vnc_lib().logical_interface_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::LogicalInterface': HeatLogicalInterface,
    }
