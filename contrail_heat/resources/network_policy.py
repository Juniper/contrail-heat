from heat.engine import constraints
from heat.engine import clients
from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource

from heat.openstack.common import log as logging
import uuid
import copy

logger = logging.getLogger(__name__)


class NetworkPolicy(ContrailResource):
    PROPERTIES = (
        NAME, ENTRIES,
    ) = (
        'name', 'entries',
    )
    _rule_schema = {
        "policy_rule": properties.Schema(
            properties.Schema.LIST,
            _('Array of policy rules'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    "direction": properties.Schema(
                        properties.Schema.STRING,
                        _('Direction of policy'),
                        constraints=[
                            constraints.AllowedValues(['<>', '<', '>']),
                        ],
                        default='<>'
                    ),
                    "protocol": properties.Schema(
                        properties.Schema.STRING,
                        _('Protocol to match'),
                        default='any'
                    ),
                    "src_ports": properties.Schema(
                        properties.Schema.LIST,
                        _('Array of src ports to match'),
                        required=True,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                "start_port": properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('start port to match'),
                                    required=True
                                ),
                                "end_port": properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('end port to match'),
                                    required=True
                                ),
                            }
                        )
                    ),
                    "dst_ports": properties.Schema(
                        properties.Schema.LIST,
                        _('Array of dst ports to match'),
                        required=True,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                "start_port": properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('start port to match'),
                                    required=True
                                ),
                                "end_port": properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('end port to match'),
                                    required=True
                                ),
                            }
                        )
                    ),
                    "dst_addresses": properties.Schema(
                        properties.Schema.LIST,
                        _('Array of dst addresses to match'),
                        required=True,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                "virtual_network": properties.Schema(
                                    properties.Schema.STRING,
                                    _('Virtual network to match'),
                                    required=True
                                ),
                            }
                        )
                    ),
                    "src_addresses": properties.Schema(
                        properties.Schema.LIST,
                        _('Array of src addresses to match'),
                        required=True,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                "virtual_network": properties.Schema(
                                    properties.Schema.STRING,
                                    _('Virtual network to match'),
                                    required=True
                                ),
                            }
                        )
                    ),
                    "action_list": properties.Schema(
                        properties.Schema.MAP,
                        _('Array of src addresses to match'),
                        required=True,
                        schema={
                            "simple_action": properties.Schema(
                                properties.Schema.STRING,
                                _('Simple Action'),
                                default='pass'
                            ),
                            "apply_service": properties.Schema(
                                properties.Schema.LIST,
                                _('Apply service'),
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
        "name": _("The name of the policy."),
        "fq_name": _("FQ name of this policy."),
        "tenant_id": _("The tenant owning this network."),
        "rules": _("List of rules"),
        "show": _("All attributes."),
    }

    def fix_apply_service(self, props):
        for policy_rule in props['entries']['policy_rule']:
            for index, service in enumerate(
                    policy_rule['action_list']['apply_service'] or []):
                try:
                    si_obj = self.vnc_lib().service_instance_read(id=service)
                except:
                    si_obj = self.vnc_lib().service_instance_read(
                        fq_name_str=service)
                policy_rule['action_list']['apply_service'][
                    index] = si_obj.get_fq_name_str()

    def fix_vn_uuid_to_fqname(self, props):
        for policy_rule in props['entries']['policy_rule']:
            for dest_address in policy_rule['dst_addresses']:
                dest_address['virtual_network'] = ':'.join(
                    self.vnc_lib().id_to_fq_name(
                        dest_address['virtual_network']))
            for src_address in policy_rule['src_addresses']:
                src_address['virtual_network'] = ':'.join(
                    self.vnc_lib().id_to_fq_name(
                        src_address['virtual_network']))

    def handle_create(self):
        props = {}
        props['entries'] = copy.deepcopy(self.properties['entries'])
        self.fix_vn_uuid_to_fqname(props)
        self.fix_apply_service(props)
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        np_obj = vnc_api.NetworkPolicy(name=self.properties[self.NAME],
                                       parent_obj=project_obj)
        np_obj.set_network_policy_entries(
            vnc_api.PolicyEntriesType.factory(**props['entries']))
        np_uuid = self.vnc_lib().network_policy_create(np_obj)
        self.resource_id_set(np_uuid)

    def _show_resource(self):
        np_obj = self.vnc_lib().network_policy_read(id=self.resource_id)
        dict = {}
        dict['name'] = np_obj.get_display_name()
        dict['fq_name'] = np_obj.get_fq_name_str()
        rules = []
        entries = np_obj.get_network_policy_entries()
        if entries:
            for rule in entries.get_policy_rule():
                policy_rule = {}
                policy_rule['direction'] = rule.get_direction()
                policy_rule['protocol'] = rule.get_protocol()
                policy_rule['dst_addresses'] = []
                for addr in rule.get_dst_addresses() or []:
                    policy_rule['dst_addresses'].append(
                        addr.get_virtual_network())
                a_list = rule.get_action_list()
                policy_rule['action_list'] = {
                    'simple_action': a_list.get_simple_action(),
                    'apply_service': a_list.get_apply_service()
                }
                policy_rule['dst_ports'] = rule.get_dst_ports()
                policy_rule['application'] = rule.get_application()
                policy_rule['src_addresses'] = []
                for addr in rule.get_src_addresses() or []:
                    policy_rule['src_addresses'].append(
                        addr.get_virtual_network())
                policy_rule['src_ports'] = rule.get_src_ports()
                rules.append(policy_rule)
        dict['rules'] = rules
        return dict

    def handle_delete(self):
        try:
            self.vnc_lib().network_policy_delete(id=self.resource_id)
        except Exception:
            pass


def resource_mapping():
    return {
        'OS::Contrail::NetworkPolicy': NetworkPolicy,
    }
