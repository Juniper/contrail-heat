from heat.engine import constraints
from heat.common import exception
from heat.engine import clients
from heat.engine.resources.neutron import neutron
from heat.engine import properties
from vnc_api.vnc_api import *
from contrail_heat.resources.contrail import ContrailResource

if clients.neutronclient is not None:
    from neutronclient.common.exceptions import NeutronClientException

from heat.openstack.common import log as logging

logger = logging.getLogger(__name__)


class NetworkPolicy(ContrailResource):
    PROPERTIES = (
        NAME, ENTRIES,
    ) = (
        'name', 'entries',
    )
    _rule_schema = {
       "policy_rule" : properties.Schema(
           properties.Schema.LIST,
           _('Array of policy rules'),
           schema=properties.Schema(
               properties.Schema.MAP,
                   schema={
                       "direction" : properties.Schema(
                             properties.Schema.STRING,
                             _('Direction of policy'),
                             constraints=[
                                constraints.AllowedValues(['<>', '<', '>']),
                             ],
                             default='<>'
                       ),
                       "protocol" : properties.Schema(
                             properties.Schema.STRING,
                             _('Protocol to match'),
                             default='any'
                        ),
                       "dst_addresses" : properties.Schema(
                             properties.Schema.LIST,
                             _('Array of dst addresses to match'),
                             required=True,
                             schema=properties.Schema(
                                 properties.Schema.MAP,
                                 schema={
                                     "virtual_network" : properties.Schema(
                                         properties.Schema.STRING,
                                         _('Virtual network to match'),
                                         required=True
                                     ),
                                 }
                             )
                       ),
                       "src_addresses" : properties.Schema(
                           properties.Schema.LIST,
                           _('Array of src addresses to match'),
                           required=True,
                           schema=properties.Schema(
                               properties.Schema.MAP,
                               schema={
                                   "virtual_network" : properties.Schema(
                                       properties.Schema.STRING,
                                       _('Virtual network to match'),
                                       required=True
                                   ),
                               }
                           )
                       ),
                       "action_list" : properties.Schema(
                           properties.Schema.MAP,
                           _('Array of src addresses to match'),
                           required=True,
                           schema={
                               "simple_action" : properties.Schema(
                                   properties.Schema.STRING,
                                   _('Simple Action'),
                                   default='pass'
                               ),
                               "apply_service" : properties.Schema(
                                   properties.Schema.LIST,
                                   _('Apply service'),
                                   required=True
                               ),
                           }
                       ),
                   }
           ),
           required=True,
       ),
    }
    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Name of the policy'),
            required=True
        ),
        ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('Policy entries'),
            schema=_rule_schema
        )
    }
    attributes_schema = {
        "status": _("The status of the policy."),
        "name": _("The name of the policy."),
        "fq_name": _("FQ name of this policy."),
        "tenant_id": _("The tenant owning this network."),
        "show": _("All attributes."),
    }

    @staticmethod
    def handle_get_network_policy_attributes(name, key, attributes):
        '''
        Support method for responding to FnGetAtt
        '''
        if key == 'show':
            return attributes

        if key in attributes.keys():
            if key == "fq_name":
                fq_name = attributes[key]
                return ':'.join(fq_name)
            else:
                return attributes[key]

        raise exception.InvalidTemplateAttribute(resource=name, key=key)

    def _resolve_attribute(self, name):
        try:
            attributes = self._show_resource()
        except NeutronClientException as ex:
            logger.warn(_("failed to fetch resource attributes: %s") %
                        str(ex))
            return None
        return self.handle_get_network_policy_attributes(self.name, name, attributes)

    def fix_apply_service(self, props):
        for policy_rule in props['entries']['policy_rule']:
            index = 0
            for service in policy_rule['action_list']['apply_service']:
                try:
                    si_obj = self.vnc_lib().service_instance_read(id=service)
                except:
                    si_obj = self.vnc_lib().service_instance_read(fq_name=service)
                policy_rule['action_list']['apply_service'][index] = si_obj.get_fq_name_str()
                index += 1

    def fix_vn_name(self, props):
        for policy_rule in props['entries']['policy_rule']:
            for dest_address in policy_rule['dst_addresses']:
                vn_name_or_id = dest_address['virtual_network']
                fq_name = self.neutron().show_network(vn_name_or_id)['network']['contrail:fq_name']
                dest_address['virtual_network'] = ':'.join(fq_name)
            for src_address in policy_rule['src_addresses']:
                vn_name_or_id = src_address['virtual_network']
                fq_name = self.neutron().show_network(vn_name_or_id)['network']['contrail:fq_name']
                src_address['virtual_network'] = ':'.join(fq_name)

    def handle_create(self):
        props = self.prepare_properties(
            self.properties,
            self.physical_resource_name())
        self.fix_vn_name(props)
        self.fix_apply_service(props)
        policy = self.neutron().create_policy({'policy': props})['policy']
        self.resource_id_set(policy['id'])

    def _show_resource(self):
        return self.neutron().show_policy(
            self.resource_id)['policy']

    def handle_delete(self):
        try:
            self.neutron().delete_policy(self.resource_id)
        except:
            pass 

def resource_mapping():
    if clients.neutronclient is None:
        return {}

    return {
        'OS::Contrail::NetworkPolicy': NetworkPolicy,
    }
