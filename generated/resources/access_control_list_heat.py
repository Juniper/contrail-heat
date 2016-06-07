
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailAccessControlList(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ACCESS_CONTROL_LIST_ENTRIES, ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION, ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID, VIRTUAL_NETWORK, SECURITY_GROUP
    ) = (
        'name', 'fq_name', 'display_name', 'access_control_list_entries', 'access_control_list_entries_dynamic', 'access_control_list_entries_acl_rule', 'access_control_list_entries_acl_rule_match_condition', 'access_control_list_entries_acl_rule_match_condition_protocol', 'access_control_list_entries_acl_rule_match_condition_src_address', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet_ip_prefix', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet_ip_prefix_len', 'access_control_list_entries_acl_rule_match_condition_src_address_virtual_network', 'access_control_list_entries_acl_rule_match_condition_src_address_security_group', 'access_control_list_entries_acl_rule_match_condition_src_address_network_policy', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet_list', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet_list_ip_prefix', 'access_control_list_entries_acl_rule_match_condition_src_address_subnet_list_ip_prefix_len', 'access_control_list_entries_acl_rule_match_condition_src_port', 'access_control_list_entries_acl_rule_match_condition_src_port_start_port', 'access_control_list_entries_acl_rule_match_condition_src_port_end_port', 'access_control_list_entries_acl_rule_match_condition_dst_address', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet_ip_prefix', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet_ip_prefix_len', 'access_control_list_entries_acl_rule_match_condition_dst_address_virtual_network', 'access_control_list_entries_acl_rule_match_condition_dst_address_security_group', 'access_control_list_entries_acl_rule_match_condition_dst_address_network_policy', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet_list', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet_list_ip_prefix', 'access_control_list_entries_acl_rule_match_condition_dst_address_subnet_list_ip_prefix_len', 'access_control_list_entries_acl_rule_match_condition_dst_port', 'access_control_list_entries_acl_rule_match_condition_dst_port_start_port', 'access_control_list_entries_acl_rule_match_condition_dst_port_end_port', 'access_control_list_entries_acl_rule_match_condition_ethertype', 'access_control_list_entries_acl_rule_action_list', 'access_control_list_entries_acl_rule_action_list_simple_action', 'access_control_list_entries_acl_rule_action_list_gateway_name', 'access_control_list_entries_acl_rule_action_list_apply_service', 'access_control_list_entries_acl_rule_action_list_mirror_to', 'access_control_list_entries_acl_rule_action_list_mirror_to_analyzer_name', 'access_control_list_entries_acl_rule_action_list_mirror_to_encapsulation', 'access_control_list_entries_acl_rule_action_list_mirror_to_analyzer_ip_address', 'access_control_list_entries_acl_rule_action_list_mirror_to_routing_instance', 'access_control_list_entries_acl_rule_action_list_mirror_to_udp_port', 'access_control_list_entries_acl_rule_action_list_assign_routing_instance', 'access_control_list_entries_acl_rule_action_list_log', 'access_control_list_entries_acl_rule_action_list_alert', 'access_control_list_entries_acl_rule_action_list_qos_action', 'access_control_list_entries_acl_rule_rule_uuid', 'virtual_network', 'security_group'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        ACCESS_CONTROL_LIST_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('ACCESS_CONTROL_LIST_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC.'),
                    update_allowed=True,
                    required=False,
                ),
                ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION: properties.Schema(
                                properties.Schema.MAP,
                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET: properties.Schema(
                                                properties.Schema.MAP,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST: properties.Schema(
                                                properties.Schema.LIST,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                        }
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET: properties.Schema(
                                                properties.Schema.MAP,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST: properties.Schema(
                                                properties.Schema.LIST,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                        }
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'IPv4', u'IPv6']),
                                        ],
                                    ),
                                }
                            ),
                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST: properties.Schema(
                                properties.Schema.MAP,
                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'deny', u'pass']),
                                        ],
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO: properties.Schema(
                                        properties.Schema.MAP,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE: properties.Schema(
                                                properties.Schema.STRING,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                        }
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT: properties.Schema(
                                        properties.Schema.BOOLEAN,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION: properties.Schema(
                                        properties.Schema.STRING,
                                        _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK.'),
            update_allowed=True,
            required=False,
        ),
        SECURITY_GROUP: properties.Schema(
            properties.Schema.STRING,
            _('SECURITY_GROUP.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ACCESS_CONTROL_LIST_ENTRIES: attributes.Schema(
            _('ACCESS_CONTROL_LIST_ENTRIES.'),
        ),
        VIRTUAL_NETWORK: attributes.Schema(
            _('VIRTUAL_NETWORK.'),
        ),
        SECURITY_GROUP: attributes.Schema(
            _('SECURITY_GROUP.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK):
            try:
                parent_obj = self.vnc_lib().virtual_network_read(id=self.properties.get(self.VIRTUAL_NETWORK))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_network_read(fq_name_str=self.properties.get(self.VIRTUAL_NETWORK))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.SECURITY_GROUP):
            try:
                parent_obj = self.vnc_lib().security_group_read(id=self.properties.get(self.SECURITY_GROUP))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().security_group_read(fq_name_str=self.properties.get(self.SECURITY_GROUP))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.AccessControlList(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES) is not None:
            obj_1 = vnc_api.AclEntriesType()
            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC) is not None:
                obj_1.set_dynamic(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC))
            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE))):
                    obj_2 = vnc_api.AclRuleType()
                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.MatchConditionType()
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL) is not None:
                            obj_3.set_protocol(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX))
                                if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_src_address(obj_4)
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT) is not None:
                                obj_4.set_start_port(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT) is not None:
                                obj_4.set_end_port(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT))
                            obj_3.set_src_port(obj_4)
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX))
                                if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_dst_address(obj_4)
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT) is not None:
                                obj_4.set_start_port(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT) is not None:
                                obj_4.set_end_port(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT))
                            obj_3.set_dst_port(obj_4)
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE) is not None:
                            obj_3.set_ethertype(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE))
                        obj_2.set_match_condition(obj_3)
                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST) is not None:
                        obj_3 = vnc_api.ActionListType()
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION) is not None:
                            obj_3.set_simple_action(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME) is not None:
                            obj_3.set_gateway_name(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE) is not None:
                            for index_3 in range(len(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE))):
                                obj_3.add_apply_service(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE)[index_3])
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO) is not None:
                            obj_4 = vnc_api.MirrorActionType()
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                                obj_4.set_analyzer_name(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                                obj_4.set_encapsulation(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                                obj_4.set_analyzer_ip_address(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                                obj_4.set_routing_instance(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                            if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                                obj_4.set_udp_port(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT))
                            obj_3.set_mirror_to(obj_4)
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                            obj_3.set_assign_routing_instance(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG) is not None:
                            obj_3.set_log(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT) is not None:
                            obj_3.set_alert(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT))
                        if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION) is not None:
                            obj_3.set_qos_action(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION))
                        obj_2.set_action_list(obj_3)
                    if self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(self.properties.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID))
                    obj_1.add_acl_rule(obj_2)
            obj_0.set_access_control_list_entries(obj_1)

        try:
            obj_uuid = super(ContrailAccessControlList, self).resource_create(obj_0)
        except:
            raise Exception(_('access-control-list %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().access_control_list_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('access-control-list %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES) is not None:
            obj_1 = vnc_api.AclEntriesType()
            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC) is not None:
                obj_1.set_dynamic(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_DYNAMIC))
            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE))):
                    obj_2 = vnc_api.AclRuleType()
                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.MatchConditionType()
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL) is not None:
                            obj_3.set_protocol(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_PROTOCOL))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_src_address(obj_4)
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT) is not None:
                                obj_4.set_start_port(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_START_PORT))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT) is not None:
                                obj_4.set_end_port(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_SRC_PORT_END_PORT))
                            obj_3.set_src_port(obj_4)
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_dst_address(obj_4)
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT) is not None:
                                obj_4.set_start_port(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_START_PORT))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT) is not None:
                                obj_4.set_end_port(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_DST_PORT_END_PORT))
                            obj_3.set_dst_port(obj_4)
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE) is not None:
                            obj_3.set_ethertype(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_MATCH_CONDITION_ETHERTYPE))
                        obj_2.set_match_condition(obj_3)
                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST) is not None:
                        obj_3 = vnc_api.ActionListType()
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION) is not None:
                            obj_3.set_simple_action(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_SIMPLE_ACTION))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME) is not None:
                            obj_3.set_gateway_name(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_GATEWAY_NAME))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE) is not None:
                            for index_3 in range(len(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE))):
                                obj_3.add_apply_service(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_APPLY_SERVICE)[index_3])
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO) is not None:
                            obj_4 = vnc_api.MirrorActionType()
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME) is not None:
                                obj_4.set_analyzer_name(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_NAME))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION) is not None:
                                obj_4.set_encapsulation(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ENCAPSULATION))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                                obj_4.set_analyzer_ip_address(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ANALYZER_IP_ADDRESS))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE) is not None:
                                obj_4.set_routing_instance(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_ROUTING_INSTANCE))
                            if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT) is not None:
                                obj_4.set_udp_port(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_MIRROR_TO_UDP_PORT))
                            obj_3.set_mirror_to(obj_4)
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE) is not None:
                            obj_3.set_assign_routing_instance(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ASSIGN_ROUTING_INSTANCE))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG) is not None:
                            obj_3.set_log(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_LOG))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT) is not None:
                            obj_3.set_alert(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_ALERT))
                        if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION) is not None:
                            obj_3.set_qos_action(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_ACTION_LIST_QOS_ACTION))
                        obj_2.set_action_list(obj_3)
                    if prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(prop_diff.get(self.ACCESS_CONTROL_LIST_ENTRIES, {}).get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE, {})[index_1].get(self.ACCESS_CONTROL_LIST_ENTRIES_ACL_RULE_RULE_UUID))
                    obj_1.add_acl_rule(obj_2)
            obj_0.set_access_control_list_entries(obj_1)

        try:
            self.vnc_lib().access_control_list_update(obj_0)
        except:
            raise Exception(_('access-control-list %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().access_control_list_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('access_control_list %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().access_control_list_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::AccessControlList': ContrailAccessControlList,
    }
