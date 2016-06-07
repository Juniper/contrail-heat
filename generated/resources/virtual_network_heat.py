
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


class ContrailVirtualNetwork(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, VIRTUAL_NETWORK_PROPERTIES, VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT, VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID, VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER, VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE, VIRTUAL_NETWORK_PROPERTIES_RPF, ECMP_HASHING_INCLUDE_FIELDS, ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP, ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT, DISPLAY_NAME, VIRTUAL_NETWORK_NETWORK_ID, ROUTER_EXTERNAL, IMPORT_ROUTE_TARGET_LIST, IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET, PROVIDER_PROPERTIES, PROVIDER_PROPERTIES_SEGMENTATION_ID, PROVIDER_PROPERTIES_PHYSICAL_NETWORK, ROUTE_TARGET_LIST, ROUTE_TARGET_LIST_ROUTE_TARGET, EXPORT_ROUTE_TARGET_LIST, EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET, FLOOD_UNKNOWN_UNICAST, EXTERNAL_IPAM, MULTI_POLICY_SERVICE_CHAINS_ENABLED, IS_SHARED, ROUTE_TABLE_REFS, NETWORK_IPAM_REFS, NETWORK_IPAM_REFS_DATA, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME, NETWORK_IPAM_REFS_DATA_HOST_ROUTES, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, QOS_CONFIG_REFS, NETWORK_POLICY_REFS, NETWORK_POLICY_REFS_DATA, NETWORK_POLICY_REFS_DATA_SEQUENCE, NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR, NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR, NETWORK_POLICY_REFS_DATA_TIMER, NETWORK_POLICY_REFS_DATA_TIMER_START_TIME, NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL, NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL, NETWORK_POLICY_REFS_DATA_TIMER_END_TIME, PROJECT
    ) = (
        'name', 'fq_name', 'virtual_network_properties', 'virtual_network_properties_allow_transit', 'virtual_network_properties_network_id', 'virtual_network_properties_vxlan_network_identifier', 'virtual_network_properties_forwarding_mode', 'virtual_network_properties_rpf', 'ecmp_hashing_include_fields', 'ecmp_hashing_include_fields_hashing_configured', 'ecmp_hashing_include_fields_source_ip', 'ecmp_hashing_include_fields_destination_ip', 'ecmp_hashing_include_fields_ip_protocol', 'ecmp_hashing_include_fields_source_port', 'ecmp_hashing_include_fields_destination_port', 'display_name', 'virtual_network_network_id', 'router_external', 'import_route_target_list', 'import_route_target_list_route_target', 'provider_properties', 'provider_properties_segmentation_id', 'provider_properties_physical_network', 'route_target_list', 'route_target_list_route_target', 'export_route_target_list', 'export_route_target_list_route_target', 'flood_unknown_unicast', 'external_ipam', 'multi_policy_service_chains_enabled', 'is_shared', 'route_table_refs', 'network_ipam_refs', 'network_ipam_refs_data', 'network_ipam_refs_data_ipam_subnets', 'network_ipam_refs_data_ipam_subnets_subnet', 'network_ipam_refs_data_ipam_subnets_subnet_ip_prefix', 'network_ipam_refs_data_ipam_subnets_subnet_ip_prefix_len', 'network_ipam_refs_data_ipam_subnets_default_gateway', 'network_ipam_refs_data_ipam_subnets_dns_server_address', 'network_ipam_refs_data_ipam_subnets_subnet_uuid', 'network_ipam_refs_data_ipam_subnets_enable_dhcp', 'network_ipam_refs_data_ipam_subnets_dns_nameservers', 'network_ipam_refs_data_ipam_subnets_allocation_pools', 'network_ipam_refs_data_ipam_subnets_allocation_pools_start', 'network_ipam_refs_data_ipam_subnets_allocation_pools_end', 'network_ipam_refs_data_ipam_subnets_addr_from_start', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_name', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_value', 'network_ipam_refs_data_ipam_subnets_dhcp_option_list_dhcp_option_dhcp_option_value_bytes', 'network_ipam_refs_data_ipam_subnets_host_routes', 'network_ipam_refs_data_ipam_subnets_host_routes_route', 'network_ipam_refs_data_ipam_subnets_host_routes_route_prefix', 'network_ipam_refs_data_ipam_subnets_host_routes_route_next_hop', 'network_ipam_refs_data_ipam_subnets_host_routes_route_next_hop_type', 'network_ipam_refs_data_ipam_subnets_host_routes_route_community_attributes', 'network_ipam_refs_data_ipam_subnets_host_routes_route_community_attributes_community_attribute', 'network_ipam_refs_data_ipam_subnets_subnet_name', 'network_ipam_refs_data_host_routes', 'network_ipam_refs_data_host_routes_route', 'network_ipam_refs_data_host_routes_route_prefix', 'network_ipam_refs_data_host_routes_route_next_hop', 'network_ipam_refs_data_host_routes_route_next_hop_type', 'network_ipam_refs_data_host_routes_route_community_attributes', 'network_ipam_refs_data_host_routes_route_community_attributes_community_attribute', 'qos_config_refs', 'network_policy_refs', 'network_policy_refs_data', 'network_policy_refs_data_sequence', 'network_policy_refs_data_sequence_major', 'network_policy_refs_data_sequence_minor', 'network_policy_refs_data_timer', 'network_policy_refs_data_timer_start_time', 'network_policy_refs_data_timer_on_interval', 'network_policy_refs_data_timer_off_interval', 'network_policy_refs_data_timer_end_time', 'project'
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
        VIRTUAL_NETWORK_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_NETWORK_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(1, 16777215),
                    ],
                ),
                VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'l2_l3', u'l2', u'l3']),
                    ],
                ),
                VIRTUAL_NETWORK_PROPERTIES_RPF: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_NETWORK_PROPERTIES_RPF.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'enable', u'disable']),
                    ],
                ),
            }
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
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_NETWORK_ID: properties.Schema(
            properties.Schema.INTEGER,
            _('VIRTUAL_NETWORK_NETWORK_ID.'),
            update_allowed=True,
            required=False,
        ),
        ROUTER_EXTERNAL: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTER_EXTERNAL.'),
            update_allowed=True,
            required=False,
        ),
        IMPORT_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('IMPORT_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PROVIDER_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('PROVIDER_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                PROVIDER_PROPERTIES_SEGMENTATION_ID: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PROVIDER_PROPERTIES_SEGMENTATION_ID.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(1, 4094),
                    ],
                ),
                PROVIDER_PROPERTIES_PHYSICAL_NETWORK: properties.Schema(
                    properties.Schema.STRING,
                    _('PROVIDER_PROPERTIES_PHYSICAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        EXPORT_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('EXPORT_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        FLOOD_UNKNOWN_UNICAST: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FLOOD_UNKNOWN_UNICAST.'),
            update_allowed=True,
            required=False,
        ),
        EXTERNAL_IPAM: properties.Schema(
            properties.Schema.BOOLEAN,
            _('EXTERNAL_IPAM.'),
            update_allowed=True,
            required=False,
        ),
        MULTI_POLICY_SERVICE_CHAINS_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('MULTI_POLICY_SERVICE_CHAINS_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        IS_SHARED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IS_SHARED.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TABLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TABLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_IPAM_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_IPAM_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_IPAM_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_IPAM_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS: properties.Schema(
                        properties.Schema.LIST,
                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS.'),
                        update_allowed=True,
                        required=False,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                            properties.Schema.INTEGER,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                    }
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP: properties.Schema(
                                    properties.Schema.BOOLEAN,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS.'),
                                    update_allowed=True,
                                    required=False,
                                    schema=properties.Schema(
                                        properties.Schema.MAP,
                                        schema={
                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END: properties.Schema(
                                                properties.Schema.STRING,
                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                        }
                                    )
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START: properties.Schema(
                                    properties.Schema.BOOLEAN,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                }
                                            )
                                        ),
                                    }
                                ),
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES: properties.Schema(
                                    properties.Schema.MAP,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES.'),
                                    update_allowed=True,
                                    required=False,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE: properties.Schema(
                                            properties.Schema.LIST,
                                            _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE.'),
                                            update_allowed=True,
                                            required=False,
                                            schema=properties.Schema(
                                                properties.Schema.MAP,
                                                schema={
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                                        update_allowed=True,
                                                        required=False,
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        constraints=[
                                                            constraints.AllowedValues([u'service-instance', u'ip-address']),
                                                        ],
                                                    ),
                                                    NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                                        properties.Schema.MAP,
                                                        _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema={
                                                            NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                                properties.Schema.LIST,
                                                                _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
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
                                NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        )
                    ),
                    NETWORK_IPAM_REFS_DATA_HOST_ROUTES: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE: properties.Schema(
                                properties.Schema.LIST,
                                _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                            properties.Schema.STRING,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.AllowedValues([u'service-instance', u'ip-address']),
                                            ],
                                        ),
                                        NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                            properties.Schema.MAP,
                                            _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                            update_allowed=True,
                                            required=False,
                                            schema={
                                                NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                    properties.Schema.LIST,
                                                    _('NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
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
                }
            )
        ),
        QOS_CONFIG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('QOS_CONFIG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NETWORK_POLICY_REFS_DATA_SEQUENCE: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_POLICY_REFS_DATA_SEQUENCE.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    ),
                    NETWORK_POLICY_REFS_DATA_TIMER: properties.Schema(
                        properties.Schema.MAP,
                        _('NETWORK_POLICY_REFS_DATA_TIMER.'),
                        update_allowed=True,
                        required=False,
                        schema={
                            NETWORK_POLICY_REFS_DATA_TIMER_START_TIME: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_START_TIME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            NETWORK_POLICY_REFS_DATA_TIMER_END_TIME: properties.Schema(
                                properties.Schema.INTEGER,
                                _('NETWORK_POLICY_REFS_DATA_TIMER_END_TIME.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    ),
                }
            )
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
        VIRTUAL_NETWORK_PROPERTIES: attributes.Schema(
            _('VIRTUAL_NETWORK_PROPERTIES.'),
        ),
        ECMP_HASHING_INCLUDE_FIELDS: attributes.Schema(
            _('ECMP_HASHING_INCLUDE_FIELDS.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        VIRTUAL_NETWORK_NETWORK_ID: attributes.Schema(
            _('VIRTUAL_NETWORK_NETWORK_ID.'),
        ),
        ROUTER_EXTERNAL: attributes.Schema(
            _('ROUTER_EXTERNAL.'),
        ),
        IMPORT_ROUTE_TARGET_LIST: attributes.Schema(
            _('IMPORT_ROUTE_TARGET_LIST.'),
        ),
        PROVIDER_PROPERTIES: attributes.Schema(
            _('PROVIDER_PROPERTIES.'),
        ),
        ROUTE_TARGET_LIST: attributes.Schema(
            _('ROUTE_TARGET_LIST.'),
        ),
        EXPORT_ROUTE_TARGET_LIST: attributes.Schema(
            _('EXPORT_ROUTE_TARGET_LIST.'),
        ),
        FLOOD_UNKNOWN_UNICAST: attributes.Schema(
            _('FLOOD_UNKNOWN_UNICAST.'),
        ),
        EXTERNAL_IPAM: attributes.Schema(
            _('EXTERNAL_IPAM.'),
        ),
        MULTI_POLICY_SERVICE_CHAINS_ENABLED: attributes.Schema(
            _('MULTI_POLICY_SERVICE_CHAINS_ENABLED.'),
        ),
        IS_SHARED: attributes.Schema(
            _('IS_SHARED.'),
        ),
        ROUTE_TABLE_REFS: attributes.Schema(
            _('ROUTE_TABLE_REFS.'),
        ),
        NETWORK_IPAM_REFS: attributes.Schema(
            _('NETWORK_IPAM_REFS.'),
        ),
        NETWORK_IPAM_REFS_DATA: attributes.Schema(
            _('NETWORK_IPAM_REFS_DATA.'),
        ),
        QOS_CONFIG_REFS: attributes.Schema(
            _('QOS_CONFIG_REFS.'),
        ),
        NETWORK_POLICY_REFS: attributes.Schema(
            _('NETWORK_POLICY_REFS.'),
        ),
        NETWORK_POLICY_REFS_DATA: attributes.Schema(
            _('NETWORK_POLICY_REFS_DATA.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
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

        obj_0 = vnc_api.VirtualNetwork(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkType()
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT) is not None:
                obj_1.set_allow_transit(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID) is not None:
                obj_1.set_network_id(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER) is not None:
                obj_1.set_vxlan_network_identifier(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE) is not None:
                obj_1.set_forwarding_mode(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE))
            if self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF) is not None:
                obj_1.set_rpf(self.properties.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF))
            obj_0.set_virtual_network_properties(obj_1)
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
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.VIRTUAL_NETWORK_NETWORK_ID) is not None:
            obj_0.set_virtual_network_network_id(self.properties.get(self.VIRTUAL_NETWORK_NETWORK_ID))
        if self.properties.get(self.ROUTER_EXTERNAL) is not None:
            obj_0.set_router_external(self.properties.get(self.ROUTER_EXTERNAL))
        if self.properties.get(self.IMPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_import_route_target_list(obj_1)
        if self.properties.get(self.PROVIDER_PROPERTIES) is not None:
            obj_1 = vnc_api.ProviderDetails()
            if self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID) is not None:
                obj_1.set_segmentation_id(self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID))
            if self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK) is not None:
                obj_1.set_physical_network(self.properties.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK))
            obj_0.set_provider_properties(obj_1)
        if self.properties.get(self.ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_route_target_list(obj_1)
        if self.properties.get(self.EXPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_export_route_target_list(obj_1)
        if self.properties.get(self.FLOOD_UNKNOWN_UNICAST) is not None:
            obj_0.set_flood_unknown_unicast(self.properties.get(self.FLOOD_UNKNOWN_UNICAST))
        if self.properties.get(self.EXTERNAL_IPAM) is not None:
            obj_0.set_external_ipam(self.properties.get(self.EXTERNAL_IPAM))
        if self.properties.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED) is not None:
            obj_0.set_multi_policy_service_chains_enabled(self.properties.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED))
        if self.properties.get(self.IS_SHARED) is not None:
            obj_0.set_is_shared(self.properties.get(self.IS_SHARED))

        # reference to route_table_refs
        if self.properties.get(self.ROUTE_TABLE_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTE_TABLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                obj_0.add_route_table(ref_obj)

        # reference to network_ipam_refs
        obj_1 = None
        if self.properties.get(self.NETWORK_IPAM_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA))):
                obj_1 = vnc_api.VnSubnetsType()
                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS) is not None:
                    for index_1 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS))):
                        obj_2 = vnc_api.IpamSubnetType()
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET) is not None:
                            obj_3 = vnc_api.SubnetType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX) is not None:
                                obj_3.set_ip_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                                obj_3.set_ip_prefix_len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN))
                            obj_2.set_subnet(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY) is not None:
                            obj_2.set_default_gateway(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                            obj_2.set_dns_server_address(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID) is not None:
                            obj_2.set_subnet_uuid(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP) is not None:
                            obj_2.set_enable_dhcp(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS) is not None:
                            for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS))):
                                obj_2.add_dns_nameservers(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS)[index_2])
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS) is not None:
                            for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS))):
                                obj_3 = vnc_api.AllocationPoolType()
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                    obj_3.set_start(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START))
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                    obj_3.set_end(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END))
                                obj_2.add_allocation_pools(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START) is not None:
                            obj_2.set_addr_from_start(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START))
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST) is not None:
                            obj_3 = vnc_api.DhcpOptionsListType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                    obj_4 = vnc_api.DhcpOptionType()
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                        obj_4.set_dhcp_option_name(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                        obj_4.set_dhcp_option_value(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                        obj_4.set_dhcp_option_value_bytes(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                    obj_3.add_dhcp_option(obj_4)
                            obj_2.set_dhcp_option_list(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES) is not None:
                            obj_3 = vnc_api.RouteTableType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                                for index_3 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE))):
                                    obj_4 = vnc_api.RouteType()
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                        obj_4.set_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                        obj_4.set_next_hop(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                        obj_4.set_next_hop_type(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                        obj_5 = vnc_api.CommunityAttributes()
                                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                            for index_5 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                                obj_5.add_community_attribute(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                        obj_4.set_community_attributes(obj_5)
                                    obj_3.add_route(obj_4)
                            obj_2.set_host_routes(obj_3)
                        if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME) is not None:
                            obj_2.set_subnet_name(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME))
                        obj_1.add_ipam_subnets(obj_2)
                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES) is not None:
                    obj_2 = vnc_api.RouteTableType()
                    if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE) is not None:
                        for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE))):
                            obj_3 = vnc_api.RouteType()
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                obj_3.set_prefix(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                obj_3.set_next_hop(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                obj_3.set_next_hop_type(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                            if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                obj_4 = vnc_api.CommunityAttributes()
                                if self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                    for index_4 in range(len(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                        obj_4.add_community_attribute(self.properties.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                                obj_3.set_community_attributes(obj_4)
                            obj_2.add_route(obj_3)
                    obj_1.set_host_routes(obj_2)

                if self.properties.get(self.NETWORK_IPAM_REFS):
                    try:
                        ref_obj = self.vnc_lib().network_ipam_read(
                            id=self.properties.get(self.NETWORK_IPAM_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().network_ipam_read(
                            fq_name_str=self.properties.get(self.NETWORK_IPAM_REFS)[index_0]
                        )
                    obj_0.add_network_ipam(ref_obj, obj_1)

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

        # reference to network_policy_refs
        obj_1 = None
        if self.properties.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.VirtualNetworkPolicyType()
                if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_2 = vnc_api.SequenceType()
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR) is not None:
                        obj_2.set_major(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR) is not None:
                        obj_2.set_minor(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR))
                    obj_1.set_sequence(obj_2)
                if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER) is not None:
                    obj_2 = vnc_api.TimerType()
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME) is not None:
                        obj_2.set_start_time(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL) is not None:
                        obj_2.set_on_interval(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL) is not None:
                        obj_2.set_off_interval(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL))
                    if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME) is not None:
                        obj_2.set_end_time(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME))
                    obj_1.set_timer(obj_2)

                if self.properties.get(self.NETWORK_POLICY_REFS):
                    try:
                        ref_obj = self.vnc_lib().network_policy_read(
                            id=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().network_policy_read(
                            fq_name_str=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    obj_0.add_network_policy(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailVirtualNetwork, self).resource_create(obj_0)
        except:
            raise Exception(_('virtual-network %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_network_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('virtual-network %s not found.') % self.name)

        if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES) is not None:
            obj_1 = vnc_api.VirtualNetworkType()
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT) is not None:
                obj_1.set_allow_transit(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_ALLOW_TRANSIT))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID) is not None:
                obj_1.set_network_id(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_NETWORK_ID))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER) is not None:
                obj_1.set_vxlan_network_identifier(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_VXLAN_NETWORK_IDENTIFIER))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE) is not None:
                obj_1.set_forwarding_mode(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_FORWARDING_MODE))
            if prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF) is not None:
                obj_1.set_rpf(prop_diff.get(self.VIRTUAL_NETWORK_PROPERTIES, {}).get(self.VIRTUAL_NETWORK_PROPERTIES_RPF))
            obj_0.set_virtual_network_properties(obj_1)
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
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.VIRTUAL_NETWORK_NETWORK_ID) is not None:
            obj_0.set_virtual_network_network_id(prop_diff.get(self.VIRTUAL_NETWORK_NETWORK_ID))
        if prop_diff.get(self.ROUTER_EXTERNAL) is not None:
            obj_0.set_router_external(prop_diff.get(self.ROUTER_EXTERNAL))
        if prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.IMPORT_ROUTE_TARGET_LIST, {}).get(self.IMPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_import_route_target_list(obj_1)
        if prop_diff.get(self.PROVIDER_PROPERTIES) is not None:
            obj_1 = vnc_api.ProviderDetails()
            if prop_diff.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID) is not None:
                obj_1.set_segmentation_id(prop_diff.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_SEGMENTATION_ID))
            if prop_diff.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK) is not None:
                obj_1.set_physical_network(prop_diff.get(self.PROVIDER_PROPERTIES, {}).get(self.PROVIDER_PROPERTIES_PHYSICAL_NETWORK))
            obj_0.set_provider_properties(obj_1)
        if prop_diff.get(self.ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.ROUTE_TARGET_LIST, {}).get(self.ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_route_target_list(obj_1)
        if prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.EXPORT_ROUTE_TARGET_LIST, {}).get(self.EXPORT_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_export_route_target_list(obj_1)
        if prop_diff.get(self.FLOOD_UNKNOWN_UNICAST) is not None:
            obj_0.set_flood_unknown_unicast(prop_diff.get(self.FLOOD_UNKNOWN_UNICAST))
        if prop_diff.get(self.EXTERNAL_IPAM) is not None:
            obj_0.set_external_ipam(prop_diff.get(self.EXTERNAL_IPAM))
        if prop_diff.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED) is not None:
            obj_0.set_multi_policy_service_chains_enabled(prop_diff.get(self.MULTI_POLICY_SERVICE_CHAINS_ENABLED))
        if prop_diff.get(self.IS_SHARED) is not None:
            obj_0.set_is_shared(prop_diff.get(self.IS_SHARED))

        # reference to route_table_refs
        ref_obj_list = []
        ref_data_list = []
        if self.ROUTE_TABLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TABLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_route_table_list(ref_obj_list)
            # End: reference to route_table_refs

        # reference to network_ipam
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA))):
                obj_1 = vnc_api.VnSubnetsType()
                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS) is not None:
                    for index_1 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS))):
                        obj_2 = vnc_api.IpamSubnetType()
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET) is not None:
                            obj_3 = vnc_api.SubnetType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX) is not None:
                                obj_3.set_ip_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                                obj_3.set_ip_prefix_len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_IP_PREFIX_LEN))
                            obj_2.set_subnet(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY) is not None:
                            obj_2.set_default_gateway(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DEFAULT_GATEWAY))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                            obj_2.set_dns_server_address(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_SERVER_ADDRESS))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID) is not None:
                            obj_2.set_subnet_uuid(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_UUID))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP) is not None:
                            obj_2.set_enable_dhcp(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ENABLE_DHCP))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS) is not None:
                            for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS))):
                                obj_2.add_dns_nameservers(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DNS_NAMESERVERS)[index_2])
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS) is not None:
                            for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS))):
                                obj_3 = vnc_api.AllocationPoolType()
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                    obj_3.set_start(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_START))
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                    obj_3.set_end(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ALLOCATION_POOLS_END))
                                obj_2.add_allocation_pools(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START) is not None:
                            obj_2.set_addr_from_start(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_ADDR_FROM_START))
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST) is not None:
                            obj_3 = vnc_api.DhcpOptionsListType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                    obj_4 = vnc_api.DhcpOptionType()
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                        obj_4.set_dhcp_option_name(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                        obj_4.set_dhcp_option_value(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                        obj_4.set_dhcp_option_value_bytes(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                    obj_3.add_dhcp_option(obj_4)
                            obj_2.set_dhcp_option_list(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES) is not None:
                            obj_3 = vnc_api.RouteTableType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                                for index_3 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE))):
                                    obj_4 = vnc_api.RouteType()
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                        obj_4.set_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                        obj_4.set_next_hop(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                        obj_4.set_next_hop_type(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                        obj_5 = vnc_api.CommunityAttributes()
                                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                            for index_5 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                                obj_5.add_community_attribute(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                        obj_4.set_community_attributes(obj_5)
                                    obj_3.add_route(obj_4)
                            obj_2.set_host_routes(obj_3)
                        if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME) is not None:
                            obj_2.set_subnet_name(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS, {})[index_1].get(self.NETWORK_IPAM_REFS_DATA_IPAM_SUBNETS_SUBNET_NAME))
                        obj_1.add_ipam_subnets(obj_2)
                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES) is not None:
                    obj_2 = vnc_api.RouteTableType()
                    if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE) is not None:
                        for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE))):
                            obj_3 = vnc_api.RouteType()
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                obj_3.set_prefix(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_PREFIX))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                obj_3.set_next_hop(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                obj_3.set_next_hop_type(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                            if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                obj_4 = vnc_api.CommunityAttributes()
                                if prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                    for index_4 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                        obj_4.add_community_attribute(prop_diff.get(self.NETWORK_IPAM_REFS_DATA, {})[index_0].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_REFS_DATA_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                                obj_3.set_community_attributes(obj_4)
                            obj_2.add_route(obj_3)
                    obj_1.set_host_routes(obj_2)
                ref_data_list.append(obj_1)
        if self.NETWORK_IPAM_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NETWORK_IPAM_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().network_ipam_read(
                        id=prop_diff.get(self.NETWORK_IPAM_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().network_ipam_read(
                        fq_name_str=prop_diff.get(self.NETWORK_IPAM_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_network_ipam_list(ref_obj_list, ref_data_list)
            # End: reference to network_ipam_refs

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

        # reference to network_policy
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.VirtualNetworkPolicyType()
                if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE) is not None:
                    obj_2 = vnc_api.SequenceType()
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR) is not None:
                        obj_2.set_major(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MAJOR))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR) is not None:
                        obj_2.set_minor(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE, {}).get(self.NETWORK_POLICY_REFS_DATA_SEQUENCE_MINOR))
                    obj_1.set_sequence(obj_2)
                if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER) is not None:
                    obj_2 = vnc_api.TimerType()
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME) is not None:
                        obj_2.set_start_time(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_START_TIME))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL) is not None:
                        obj_2.set_on_interval(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_ON_INTERVAL))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL) is not None:
                        obj_2.set_off_interval(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_OFF_INTERVAL))
                    if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME) is not None:
                        obj_2.set_end_time(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_TIMER, {}).get(self.NETWORK_POLICY_REFS_DATA_TIMER_END_TIME))
                    obj_1.set_timer(obj_2)
                ref_data_list.append(obj_1)
        if self.NETWORK_POLICY_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().network_policy_read(
                        id=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().network_policy_read(
                        fq_name_str=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_network_policy_list(ref_obj_list, ref_data_list)
            # End: reference to network_policy_refs

        try:
            self.vnc_lib().virtual_network_update(obj_0)
        except:
            raise Exception(_('virtual-network %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_network_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_network %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().virtual_network_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualNetwork': ContrailVirtualNetwork,
    }
