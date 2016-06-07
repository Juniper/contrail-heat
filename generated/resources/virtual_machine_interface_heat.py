
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


class ContrailVirtualMachineInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ECMP_HASHING_INCLUDE_FIELDS, ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP, ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS, VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME, VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE, VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES, VIRTUAL_MACHINE_INTERFACE_BINDINGS, VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY, VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE, VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC, VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE, VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL, VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT, VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER, VRF_ASSIGN_TABLE, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE, VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL, VIRTUAL_MACHINE_INTERFACE_PROPERTIES, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE, VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG, DISPLAY_NAME, SERVICE_HEALTH_CHECK_REFS, ROUTING_INSTANCE_REFS, ROUTING_INSTANCE_REFS_DATA, ROUTING_INSTANCE_REFS_DATA_DIRECTION, ROUTING_INSTANCE_REFS_DATA_VLAN_TAG, ROUTING_INSTANCE_REFS_DATA_SRC_MAC, ROUTING_INSTANCE_REFS_DATA_DST_MAC, ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL, ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS, ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS, ROUTING_INSTANCE_REFS_DATA_PROTOCOL, SECURITY_GROUP_REFS, PHYSICAL_INTERFACE_REFS, PORT_TUPLE_REFS, INTERFACE_ROUTE_TABLE_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, VIRTUAL_NETWORK_REFS, VIRTUAL_MACHINE_REFS, QOS_CONFIG_REFS, VIRTUAL_MACHINE, PROJECT
    ) = (
        'name', 'fq_name', 'ecmp_hashing_include_fields', 'ecmp_hashing_include_fields_hashing_configured', 'ecmp_hashing_include_fields_source_ip', 'ecmp_hashing_include_fields_destination_ip', 'ecmp_hashing_include_fields_ip_protocol', 'ecmp_hashing_include_fields_source_port', 'ecmp_hashing_include_fields_destination_port', 'virtual_machine_interface_host_routes', 'virtual_machine_interface_host_routes_route', 'virtual_machine_interface_host_routes_route_prefix', 'virtual_machine_interface_host_routes_route_next_hop', 'virtual_machine_interface_host_routes_route_next_hop_type', 'virtual_machine_interface_host_routes_route_community_attributes', 'virtual_machine_interface_host_routes_route_community_attributes_community_attribute', 'virtual_machine_interface_mac_addresses', 'virtual_machine_interface_mac_addresses_mac_address', 'virtual_machine_interface_dhcp_option_list', 'virtual_machine_interface_dhcp_option_list_dhcp_option', 'virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_name', 'virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value', 'virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value_bytes', 'virtual_machine_interface_bindings', 'virtual_machine_interface_bindings_key_value_pair', 'virtual_machine_interface_bindings_key_value_pair_key', 'virtual_machine_interface_bindings_key_value_pair_value', 'virtual_machine_interface_disable_policy', 'virtual_machine_interface_allowed_address_pairs', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair_mac', 'virtual_machine_interface_allowed_address_pairs_allowed_address_pair_address_mode', 'virtual_machine_interface_fat_flow_protocols', 'virtual_machine_interface_fat_flow_protocols_fat_flow_protocol', 'virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_protocol', 'virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_port', 'virtual_machine_interface_device_owner', 'vrf_assign_table', 'vrf_assign_table_vrf_assign_rule', 'vrf_assign_table_vrf_assign_rule_match_condition', 'vrf_assign_table_vrf_assign_rule_match_condition_protocol', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet_ip_prefix', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet_ip_prefix_len', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_virtual_network', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_security_group', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_network_policy', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet_list', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet_list_ip_prefix', 'vrf_assign_table_vrf_assign_rule_match_condition_src_address_subnet_list_ip_prefix_len', 'vrf_assign_table_vrf_assign_rule_match_condition_src_port', 'vrf_assign_table_vrf_assign_rule_match_condition_src_port_start_port', 'vrf_assign_table_vrf_assign_rule_match_condition_src_port_end_port', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet_ip_prefix', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet_ip_prefix_len', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_virtual_network', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_security_group', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_network_policy', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet_list', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet_list_ip_prefix', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_address_subnet_list_ip_prefix_len', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_port', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_port_start_port', 'vrf_assign_table_vrf_assign_rule_match_condition_dst_port_end_port', 'vrf_assign_table_vrf_assign_rule_match_condition_ethertype', 'vrf_assign_table_vrf_assign_rule_vlan_tag', 'vrf_assign_table_vrf_assign_rule_routing_instance', 'vrf_assign_table_vrf_assign_rule_ignore_acl', 'virtual_machine_interface_properties', 'virtual_machine_interface_properties_service_interface_type', 'virtual_machine_interface_properties_interface_mirror', 'virtual_machine_interface_properties_interface_mirror_traffic_direction', 'virtual_machine_interface_properties_interface_mirror_mirror_to', 'virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_name', 'virtual_machine_interface_properties_interface_mirror_mirror_to_encapsulation', 'virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_ip_address', 'virtual_machine_interface_properties_interface_mirror_mirror_to_routing_instance', 'virtual_machine_interface_properties_interface_mirror_mirror_to_udp_port', 'virtual_machine_interface_properties_local_preference', 'virtual_machine_interface_properties_sub_interface_vlan_tag', 'display_name', 'service_health_check_refs', 'routing_instance_refs', 'routing_instance_refs_data', 'routing_instance_refs_data_direction', 'routing_instance_refs_data_vlan_tag', 'routing_instance_refs_data_src_mac', 'routing_instance_refs_data_dst_mac', 'routing_instance_refs_data_mpls_label', 'routing_instance_refs_data_service_chain_address', 'routing_instance_refs_data_ipv6_service_chain_address', 'routing_instance_refs_data_protocol', 'security_group_refs', 'physical_interface_refs', 'port_tuple_refs', 'interface_route_table_refs', 'virtual_machine_interface_refs', 'virtual_network_refs', 'virtual_machine_refs', 'qos_config_refs', 'virtual_machine', 'project'
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
        ECMP_HASHING_INCLUDE_FIELDS: properties.Schema(
            properties.Schema.MAP,
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
            update_allowed=True,
            required=False,
            schema={
                ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'service-instance', u'ip-address']),
                                ],
                            ),
                            VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_BINDINGS: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_BINDINGS.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY: properties.Schema(
            properties.Schema.BOOLEAN,
            _('VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP: properties.Schema(
                                properties.Schema.MAP,
                                _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'active-active', u'active-standby']),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL: properties.Schema(
                    properties.Schema.LIST,
                    _('VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER.'),
            update_allowed=True,
            required=False,
        ),
        VRF_ASSIGN_TABLE: properties.Schema(
            properties.Schema.MAP,
            _('VRF_ASSIGN_TABLE.'),
            update_allowed=True,
            required=False,
            schema={
                VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION: properties.Schema(
                                properties.Schema.MAP,
                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET: properties.Schema(
                                                properties.Schema.MAP,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST: properties.Schema(
                                                properties.Schema.LIST,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                        }
                                    ),
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET: properties.Schema(
                                                properties.Schema.MAP,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                                        properties.Schema.INTEGER,
                                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY: properties.Schema(
                                                properties.Schema.STRING,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST: properties.Schema(
                                                properties.Schema.LIST,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                        VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    ),
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT: properties.Schema(
                                        properties.Schema.MAP,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(-1, 65535),
                                                ],
                                            ),
                                        }
                                    ),
                                    VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'IPv4', u'IPv6']),
                                        ],
                                    ),
                                }
                            ),
                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE: properties.Schema(
                                properties.Schema.STRING,
                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL: properties.Schema(
                                properties.Schema.BOOLEAN,
                                _('VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_MACHINE_INTERFACE_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR: properties.Schema(
                    properties.Schema.MAP,
                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION: properties.Schema(
                            properties.Schema.STRING,
                            _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'ingress', u'egress', u'both']),
                            ],
                        ),
                        VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO: properties.Schema(
                            properties.Schema.MAP,
                            _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO.'),
                            update_allowed=True,
                            required=False,
                            schema={
                                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME: properties.Schema(
                                    properties.Schema.STRING,
                                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION: properties.Schema(
                                    properties.Schema.STRING,
                                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS: properties.Schema(
                                    properties.Schema.STRING,
                                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE: properties.Schema(
                                    properties.Schema.STRING,
                                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        ),
                    }
                ),
                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_HEALTH_CHECK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_HEALTH_CHECK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_INSTANCE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTING_INSTANCE_REFS_DATA_DIRECTION: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_DIRECTION.'),
                        update_allowed=True,
                        required=False,
                        constraints=[
                            constraints.AllowedValues([u'ingress', u'egress', u'both']),
                        ],
                    ),
                    ROUTING_INSTANCE_REFS_DATA_VLAN_TAG: properties.Schema(
                        properties.Schema.INTEGER,
                        _('ROUTING_INSTANCE_REFS_DATA_VLAN_TAG.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_SRC_MAC: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_SRC_MAC.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_DST_MAC: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_DST_MAC.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL: properties.Schema(
                        properties.Schema.INTEGER,
                        _('ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS.'),
                        update_allowed=True,
                        required=False,
                    ),
                    ROUTING_INSTANCE_REFS_DATA_PROTOCOL: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_PROTOCOL.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        SECURITY_GROUP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_GROUP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PORT_TUPLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PORT_TUPLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        INTERFACE_ROUTE_TABLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('INTERFACE_ROUTE_TABLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        QOS_CONFIG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('QOS_CONFIG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_MACHINE.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
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
        ECMP_HASHING_INCLUDE_FIELDS: attributes.Schema(
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_BINDINGS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_BINDINGS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER.'),
        ),
        VRF_ASSIGN_TABLE: attributes.Schema(
            _('VRF_ASSIGN_TABLE.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_PROPERTIES: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        SERVICE_HEALTH_CHECK_REFS: attributes.Schema(
            _('SERVICE_HEALTH_CHECK_REFS.'),
        ),
        ROUTING_INSTANCE_REFS: attributes.Schema(
            _('ROUTING_INSTANCE_REFS.'),
        ),
        ROUTING_INSTANCE_REFS_DATA: attributes.Schema(
            _('ROUTING_INSTANCE_REFS_DATA.'),
        ),
        SECURITY_GROUP_REFS: attributes.Schema(
            _('SECURITY_GROUP_REFS.'),
        ),
        PHYSICAL_INTERFACE_REFS: attributes.Schema(
            _('PHYSICAL_INTERFACE_REFS.'),
        ),
        PORT_TUPLE_REFS: attributes.Schema(
            _('PORT_TUPLE_REFS.'),
        ),
        INTERFACE_ROUTE_TABLE_REFS: attributes.Schema(
            _('INTERFACE_ROUTE_TABLE_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        VIRTUAL_MACHINE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_REFS.'),
        ),
        QOS_CONFIG_REFS: attributes.Schema(
            _('QOS_CONFIG_REFS.'),
        ),
        VIRTUAL_MACHINE: attributes.Schema(
            _('VIRTUAL_MACHINE.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_MACHINE):
            try:
                parent_obj = self.vnc_lib().virtual_machine_read(id=self.properties.get(self.VIRTUAL_MACHINE))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_machine_read(fq_name_str=self.properties.get(self.VIRTUAL_MACHINE))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT):
            try:
                parent_obj = self.vnc_lib().project_read(id=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except:
                parent_obj = None

        if parent_obj is None:
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.VirtualMachineInterface(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS) is not None:
            obj_1 = vnc_api.EcmpHashingIncludeFields()
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED) is not None:
                obj_1.set_hashing_configured(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP) is not None:
                obj_1.set_source_ip(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP) is not None:
                obj_1.set_destination_ip(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL) is not None:
                obj_1.set_ip_protocol(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT) is not None:
                obj_1.set_source_port(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT))
            if self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT) is not None:
                obj_1.set_destination_port(self.properties.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT))
            obj_0.set_ecmp_hashing_include_fields(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES) is not None:
            obj_1 = vnc_api.RouteTableType()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE))):
                    obj_2 = vnc_api.RouteType()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                        obj_2.set_next_hop_type(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                        obj_3 = vnc_api.CommunityAttributes()
                        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                            for index_3 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                obj_3.add_community_attribute(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_3])
                        obj_2.set_community_attributes(obj_3)
                    obj_1.add_route(obj_2)
            obj_0.set_virtual_machine_interface_host_routes(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES) is not None:
            obj_1 = vnc_api.MacAddressesType()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS))):
                    obj_1.add_mac_address(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS)[index_1])
            obj_0.set_virtual_machine_interface_mac_addresses(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST) is not None:
            obj_1 = vnc_api.DhcpOptionsListType()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION))):
                    obj_2 = vnc_api.DhcpOptionType()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                        obj_2.set_dhcp_option_name(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                        obj_2.set_dhcp_option_value(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                        obj_2.set_dhcp_option_value_bytes(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                    obj_1.add_dhcp_option(obj_2)
            obj_0.set_virtual_machine_interface_dhcp_option_list(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_virtual_machine_interface_bindings(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY) is not None:
            obj_0.set_virtual_machine_interface_disable_policy(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY))
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS) is not None:
            obj_1 = vnc_api.AllowedAddressPairs()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR))):
                    obj_2 = vnc_api.AllowedAddressPair()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX))
                        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN))
                        obj_2.set_ip(obj_3)
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC) is not None:
                        obj_2.set_mac(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE) is not None:
                        obj_2.set_address_mode(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE))
                    obj_1.add_allowed_address_pair(obj_2)
            obj_0.set_virtual_machine_interface_allowed_address_pairs(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS) is not None:
            obj_1 = vnc_api.FatFlowProtocols()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL) is not None:
                for index_1 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL))):
                    obj_2 = vnc_api.ProtocolType()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT) is not None:
                        obj_2.set_port(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT))
                    obj_1.add_fat_flow_protocol(obj_2)
            obj_0.set_virtual_machine_interface_fat_flow_protocols(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER) is not None:
            obj_0.set_virtual_machine_interface_device_owner(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER))
        if self.properties.get(self.VRF_ASSIGN_TABLE) is not None:
            obj_1 = vnc_api.VrfAssignTableType()
            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE))):
                    obj_2 = vnc_api.VrfAssignRuleType()
                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.MatchConditionType()
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL) is not None:
                            obj_3.set_protocol(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL))
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX))
                                if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_src_address(obj_4)
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT) is not None:
                                obj_4.set_start_port(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT) is not None:
                                obj_4.set_end_port(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT))
                            obj_3.set_src_port(obj_4)
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX))
                                if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_dst_address(obj_4)
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT) is not None:
                                obj_4.set_start_port(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT))
                            if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT) is not None:
                                obj_4.set_end_port(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT))
                            obj_3.set_dst_port(obj_4)
                        if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE) is not None:
                            obj_3.set_ethertype(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE))
                        obj_2.set_match_condition(obj_3)
                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG) is not None:
                        obj_2.set_vlan_tag(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG))
                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE) is not None:
                        obj_2.set_routing_instance(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE))
                    if self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL) is not None:
                        obj_2.set_ignore_acl(self.properties.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL))
                    obj_1.add_vrf_assign_rule(obj_2)
            obj_0.set_vrf_assign_table(obj_1)
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualMachineInterfacePropertiesType()
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE) is not None:
                obj_1.set_service_interface_type(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE))
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR) is not None:
                obj_2 = vnc_api.InterfaceMirrorType()
                if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION) is not None:
                    obj_2.set_traffic_direction(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION))
                if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO) is not None:
                    obj_3 = vnc_api.MirrorActionType()
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME) is not None:
                        obj_3.set_analyzer_name(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION) is not None:
                        obj_3.set_encapsulation(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                        obj_3.set_analyzer_ip_address(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE) is not None:
                        obj_3.set_routing_instance(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE))
                    if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT) is not None:
                        obj_3.set_udp_port(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT))
                    obj_2.set_mirror_to(obj_3)
                obj_1.set_interface_mirror(obj_2)
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE) is not None:
                obj_1.set_local_preference(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE))
            if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG) is not None:
                obj_1.set_sub_interface_vlan_tag(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG))
            obj_0.set_virtual_machine_interface_properties(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        # reference to service_health_check_refs
        if self.properties.get(self.SERVICE_HEALTH_CHECK_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_HEALTH_CHECK_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        id=self.properties.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        fq_name_str=self.properties.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                obj_0.add_service_health_check(ref_obj)

        # reference to routing_instance_refs
        obj_1 = None
        if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.PolicyBasedForwardingRuleType()
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DIRECTION) is not None:
                    obj_1.set_direction(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DIRECTION))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_VLAN_TAG) is not None:
                    obj_1.set_vlan_tag(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_VLAN_TAG))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SRC_MAC) is not None:
                    obj_1.set_src_mac(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SRC_MAC))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DST_MAC) is not None:
                    obj_1.set_dst_mac(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DST_MAC))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL) is not None:
                    obj_1.set_mpls_label(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS) is not None:
                    obj_1.set_service_chain_address(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS) is not None:
                    obj_1.set_ipv6_service_chain_address(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS))
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_PROTOCOL) is not None:
                    obj_1.set_protocol(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_PROTOCOL))

                if self.properties.get(self.ROUTING_INSTANCE_REFS):
                    try:
                        ref_obj = self.vnc_lib().routing_instance_read(
                            id=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().routing_instance_read(
                            fq_name_str=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                        )
                    obj_0.add_routing_instance(ref_obj, obj_1)

        # reference to security_group_refs
        if self.properties.get(self.SECURITY_GROUP_REFS):
            for index_0 in range(len(self.properties.get(self.SECURITY_GROUP_REFS))):
                try:
                    ref_obj = self.vnc_lib().security_group_read(
                        id=self.properties.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().security_group_read(
                        fq_name_str=self.properties.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                obj_0.add_security_group(ref_obj)

        # reference to physical_interface_refs
        if self.properties.get(self.PHYSICAL_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.PHYSICAL_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        id=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        fq_name_str=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                obj_0.add_physical_interface(ref_obj)

        # reference to port_tuple_refs
        if self.properties.get(self.PORT_TUPLE_REFS):
            for index_0 in range(len(self.properties.get(self.PORT_TUPLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().port_tuple_read(
                        id=self.properties.get(self.PORT_TUPLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().port_tuple_read(
                        fq_name_str=self.properties.get(self.PORT_TUPLE_REFS)[index_0]
                    )
                obj_0.add_port_tuple(ref_obj)

        # reference to interface_route_table_refs
        if self.properties.get(self.INTERFACE_ROUTE_TABLE_REFS):
            for index_0 in range(len(self.properties.get(self.INTERFACE_ROUTE_TABLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().interface_route_table_read(
                        id=self.properties.get(self.INTERFACE_ROUTE_TABLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().interface_route_table_read(
                        fq_name_str=self.properties.get(self.INTERFACE_ROUTE_TABLE_REFS)[index_0]
                    )
                obj_0.add_interface_route_table(ref_obj)

        # reference to virtual_machine_interface_refs
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                obj_0.add_virtual_machine_interface(ref_obj)

        # reference to virtual_network_refs
        if self.properties.get(self.VIRTUAL_NETWORK_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_NETWORK_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                obj_0.add_virtual_network(ref_obj)

        # reference to virtual_machine_refs
        if self.properties.get(self.VIRTUAL_MACHINE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                obj_0.add_virtual_machine(ref_obj)

        # reference to qos_config_refs
        if self.properties.get(self.QOS_CONFIG_REFS):
            for index_0 in range(len(self.properties.get(self.QOS_CONFIG_REFS))):
                try:
                    ref_obj = self.vnc_lib().qos_config_read(
                        id=self.properties.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().qos_config_read(
                        fq_name_str=self.properties.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                obj_0.add_qos_config(ref_obj)

        try:
            obj_uuid = super(ContrailVirtualMachineInterface, self).resource_create(obj_0)
        except:
            raise Exception(_('virtual-machine-interface %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_machine_interface_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('virtual-machine-interface %s not found.') % self.name)

        if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS) is not None:
            obj_1 = vnc_api.EcmpHashingIncludeFields()
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED) is not None:
                obj_1.set_hashing_configured(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP) is not None:
                obj_1.set_source_ip(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP) is not None:
                obj_1.set_destination_ip(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL) is not None:
                obj_1.set_ip_protocol(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT) is not None:
                obj_1.set_source_port(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT))
            if prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT) is not None:
                obj_1.set_destination_port(prop_diff.get(self.ECMP_HASHING_INCLUDE_FIELDS, {}).get(self.ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT))
            obj_0.set_ecmp_hashing_include_fields(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES) is not None:
            obj_1 = vnc_api.RouteTableType()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE))):
                    obj_2 = vnc_api.RouteType()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_PREFIX))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                        obj_2.set_next_hop_type(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                        obj_3 = vnc_api.CommunityAttributes()
                        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                            for index_3 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                obj_3.add_community_attribute(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_3])
                        obj_2.set_community_attributes(obj_3)
                    obj_1.add_route(obj_2)
            obj_0.set_virtual_machine_interface_host_routes(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES) is not None:
            obj_1 = vnc_api.MacAddressesType()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS))):
                    obj_1.add_mac_address(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_MAC_ADDRESSES_MAC_ADDRESS)[index_1])
            obj_0.set_virtual_machine_interface_mac_addresses(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST) is not None:
            obj_1 = vnc_api.DhcpOptionsListType()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION))):
                    obj_2 = vnc_api.DhcpOptionType()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                        obj_2.set_dhcp_option_name(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                        obj_2.set_dhcp_option_value(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                        obj_2.set_dhcp_option_value_bytes(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST, {}).get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                    obj_1.add_dhcp_option(obj_2)
            obj_0.set_virtual_machine_interface_dhcp_option_list(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_BINDINGS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_virtual_machine_interface_bindings(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY) is not None:
            obj_0.set_virtual_machine_interface_disable_policy(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DISABLE_POLICY))
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS) is not None:
            obj_1 = vnc_api.AllowedAddressPairs()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR))):
                    obj_2 = vnc_api.AllowedAddressPair()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX))
                        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_IP_IP_PREFIX_LEN))
                        obj_2.set_ip(obj_3)
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC) is not None:
                        obj_2.set_mac(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_MAC))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE) is not None:
                        obj_2.set_address_mode(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_ALLOWED_ADDRESS_PAIRS_ALLOWED_ADDRESS_PAIR_ADDRESS_MODE))
                    obj_1.add_allowed_address_pair(obj_2)
            obj_0.set_virtual_machine_interface_allowed_address_pairs(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS) is not None:
            obj_1 = vnc_api.FatFlowProtocols()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL) is not None:
                for index_1 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL))):
                    obj_2 = vnc_api.ProtocolType()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PROTOCOL))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT) is not None:
                        obj_2.set_port(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS, {}).get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL, {})[index_1].get(self.VIRTUAL_MACHINE_INTERFACE_FAT_FLOW_PROTOCOLS_FAT_FLOW_PROTOCOL_PORT))
                    obj_1.add_fat_flow_protocol(obj_2)
            obj_0.set_virtual_machine_interface_fat_flow_protocols(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER) is not None:
            obj_0.set_virtual_machine_interface_device_owner(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_DEVICE_OWNER))
        if prop_diff.get(self.VRF_ASSIGN_TABLE) is not None:
            obj_1 = vnc_api.VrfAssignTableType()
            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE))):
                    obj_2 = vnc_api.VrfAssignRuleType()
                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION) is not None:
                        obj_3 = vnc_api.MatchConditionType()
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL) is not None:
                            obj_3.set_protocol(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_PROTOCOL))
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_VIRTUAL_NETWORK))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SECURITY_GROUP))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_NETWORK_POLICY))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_src_address(obj_4)
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT) is not None:
                                obj_4.set_start_port(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_START_PORT))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT) is not None:
                                obj_4.set_end_port(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_SRC_PORT_END_PORT))
                            obj_3.set_src_port(obj_4)
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS) is not None:
                            obj_4 = vnc_api.AddressType()
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET) is not None:
                                obj_5 = vnc_api.SubnetType()
                                if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX) is not None:
                                    obj_5.set_ip_prefix(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX))
                                if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN) is not None:
                                    obj_5.set_ip_prefix_len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_IP_PREFIX_LEN))
                                obj_4.set_subnet(obj_5)
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK) is not None:
                                obj_4.set_virtual_network(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_VIRTUAL_NETWORK))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP) is not None:
                                obj_4.set_security_group(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SECURITY_GROUP))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY) is not None:
                                obj_4.set_network_policy(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_NETWORK_POLICY))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST) is not None:
                                for index_4 in range(len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST))):
                                    obj_5 = vnc_api.SubnetType()
                                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX) is not None:
                                        obj_5.set_ip_prefix(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX))
                                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN) is not None:
                                        obj_5.set_ip_prefix_len(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST, {})[index_4].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_ADDRESS_SUBNET_LIST_IP_PREFIX_LEN))
                                    obj_4.add_subnet_list(obj_5)
                            obj_3.set_dst_address(obj_4)
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT) is not None:
                            obj_4 = vnc_api.PortType()
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT) is not None:
                                obj_4.set_start_port(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_START_PORT))
                            if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT) is not None:
                                obj_4.set_end_port(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_DST_PORT_END_PORT))
                            obj_3.set_dst_port(obj_4)
                        if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE) is not None:
                            obj_3.set_ethertype(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_MATCH_CONDITION_ETHERTYPE))
                        obj_2.set_match_condition(obj_3)
                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG) is not None:
                        obj_2.set_vlan_tag(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_VLAN_TAG))
                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE) is not None:
                        obj_2.set_routing_instance(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_ROUTING_INSTANCE))
                    if prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL) is not None:
                        obj_2.set_ignore_acl(prop_diff.get(self.VRF_ASSIGN_TABLE, {}).get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE, {})[index_1].get(self.VRF_ASSIGN_TABLE_VRF_ASSIGN_RULE_IGNORE_ACL))
                    obj_1.add_vrf_assign_rule(obj_2)
            obj_0.set_vrf_assign_table(obj_1)
        if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualMachineInterfacePropertiesType()
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE) is not None:
                obj_1.set_service_interface_type(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SERVICE_INTERFACE_TYPE))
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR) is not None:
                obj_2 = vnc_api.InterfaceMirrorType()
                if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION) is not None:
                    obj_2.set_traffic_direction(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_TRAFFIC_DIRECTION))
                if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO) is not None:
                    obj_3 = vnc_api.MirrorActionType()
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME) is not None:
                        obj_3.set_analyzer_name(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_NAME))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION) is not None:
                        obj_3.set_encapsulation(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ENCAPSULATION))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS) is not None:
                        obj_3.set_analyzer_ip_address(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ANALYZER_IP_ADDRESS))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE) is not None:
                        obj_3.set_routing_instance(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_ROUTING_INSTANCE))
                    if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT) is not None:
                        obj_3.set_udp_port(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_INTERFACE_MIRROR_MIRROR_TO_UDP_PORT))
                    obj_2.set_mirror_to(obj_3)
                obj_1.set_interface_mirror(obj_2)
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE) is not None:
                obj_1.set_local_preference(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_LOCAL_PREFERENCE))
            if prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG) is not None:
                obj_1.set_sub_interface_vlan_tag(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES, {}).get(self.VIRTUAL_MACHINE_INTERFACE_PROPERTIES_SUB_INTERFACE_VLAN_TAG))
            obj_0.set_virtual_machine_interface_properties(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        # reference to service_health_check_refs
        ref_obj_list = []
        ref_data_list = []
        if self.SERVICE_HEALTH_CHECK_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        id=prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().service_health_check_read(
                        fq_name_str=prop_diff.get(self.SERVICE_HEALTH_CHECK_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_service_health_check_list(ref_obj_list)
            # End: reference to service_health_check_refs

        # reference to routing_instance
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.PolicyBasedForwardingRuleType()
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DIRECTION) is not None:
                    obj_1.set_direction(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DIRECTION))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_VLAN_TAG) is not None:
                    obj_1.set_vlan_tag(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_VLAN_TAG))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SRC_MAC) is not None:
                    obj_1.set_src_mac(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SRC_MAC))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DST_MAC) is not None:
                    obj_1.set_dst_mac(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DST_MAC))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL) is not None:
                    obj_1.set_mpls_label(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_MPLS_LABEL))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS) is not None:
                    obj_1.set_service_chain_address(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_SERVICE_CHAIN_ADDRESS))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS) is not None:
                    obj_1.set_ipv6_service_chain_address(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_IPV6_SERVICE_CHAIN_ADDRESS))
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_PROTOCOL) is not None:
                    obj_1.set_protocol(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_PROTOCOL))
                ref_data_list.append(obj_1)
        if self.ROUTING_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        id=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        fq_name_str=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_routing_instance_list(ref_obj_list, ref_data_list)
            # End: reference to routing_instance_refs

        # reference to security_group_refs
        ref_obj_list = []
        ref_data_list = []
        if self.SECURITY_GROUP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SECURITY_GROUP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().security_group_read(
                        id=prop_diff.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().security_group_read(
                        fq_name_str=prop_diff.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_security_group_list(ref_obj_list)
            # End: reference to security_group_refs

        # reference to physical_interface_refs
        ref_obj_list = []
        ref_data_list = []
        if self.PHYSICAL_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        id=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        fq_name_str=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_physical_interface_list(ref_obj_list)
            # End: reference to physical_interface_refs

        # reference to port_tuple_refs
        ref_obj_list = []
        ref_data_list = []
        if self.PORT_TUPLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PORT_TUPLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().port_tuple_read(
                        id=prop_diff.get(self.PORT_TUPLE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().port_tuple_read(
                        fq_name_str=prop_diff.get(self.PORT_TUPLE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_port_tuple_list(ref_obj_list)
            # End: reference to port_tuple_refs

        # reference to interface_route_table_refs
        ref_obj_list = []
        ref_data_list = []
        if self.INTERFACE_ROUTE_TABLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.INTERFACE_ROUTE_TABLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().interface_route_table_read(
                        id=prop_diff.get(self.INTERFACE_ROUTE_TABLE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().interface_route_table_read(
                        fq_name_str=prop_diff.get(self.INTERFACE_ROUTE_TABLE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_interface_route_table_list(ref_obj_list)
            # End: reference to interface_route_table_refs

        # reference to virtual_machine_interface_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_MACHINE_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_machine_interface_list(ref_obj_list)
            # End: reference to virtual_machine_interface_refs

        # reference to virtual_network_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_NETWORK_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_network_list(ref_obj_list)
            # End: reference to virtual_network_refs

        # reference to virtual_machine_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_MACHINE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_machine_list(ref_obj_list)
            # End: reference to virtual_machine_refs

        # reference to qos_config_refs
        ref_obj_list = []
        ref_data_list = []
        if self.QOS_CONFIG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.QOS_CONFIG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().qos_config_read(
                        id=prop_diff.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().qos_config_read(
                        fq_name_str=prop_diff.get(self.QOS_CONFIG_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_qos_config_list(ref_obj_list)
            # End: reference to qos_config_refs

        try:
            self.vnc_lib().virtual_machine_interface_update(obj_0)
        except:
            raise Exception(_('virtual-machine-interface %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_machine_interface_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_machine_interface %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().virtual_machine_interface_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualMachineInterface': ContrailVirtualMachineInterface,
    }
