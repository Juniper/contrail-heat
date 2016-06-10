
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


class ContrailBgpRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, BGP_ROUTER_PARAMETERS, BGP_ROUTER_PARAMETERS_ADMIN_DOWN, BGP_ROUTER_PARAMETERS_VENDOR, BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM, BGP_ROUTER_PARAMETERS_IDENTIFIER, BGP_ROUTER_PARAMETERS_ADDRESS, BGP_ROUTER_PARAMETERS_PORT, BGP_ROUTER_PARAMETERS_SOURCE_PORT, BGP_ROUTER_PARAMETERS_HOLD_TIME, BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY, BGP_ROUTER_PARAMETERS_AUTH_DATA, BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE, BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID, BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY, BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM, BGP_ROUTER_PARAMETERS_ROUTER_TYPE, BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS, BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS, BGP_ROUTER_REFS, BGP_ROUTER_REFS_DATA, BGP_ROUTER_REFS_DATA_SESSION, BGP_ROUTER_REFS_DATA_SESSION_UUID, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM, ROUTING_INSTANCE
    ) = (
        'name', 'fq_name', 'display_name', 'bgp_router_parameters', 'bgp_router_parameters_admin_down', 'bgp_router_parameters_vendor', 'bgp_router_parameters_autonomous_system', 'bgp_router_parameters_identifier', 'bgp_router_parameters_address', 'bgp_router_parameters_port', 'bgp_router_parameters_source_port', 'bgp_router_parameters_hold_time', 'bgp_router_parameters_address_families', 'bgp_router_parameters_address_families_family', 'bgp_router_parameters_auth_data', 'bgp_router_parameters_auth_data_key_type', 'bgp_router_parameters_auth_data_key_items', 'bgp_router_parameters_auth_data_key_items_key_id', 'bgp_router_parameters_auth_data_key_items_key', 'bgp_router_parameters_local_autonomous_system', 'bgp_router_parameters_router_type', 'bgp_router_parameters_gateway_address', 'bgp_router_parameters_ipv6_gateway_address', 'bgp_router_refs', 'bgp_router_refs_data', 'bgp_router_refs_data_session', 'bgp_router_refs_data_session_uuid', 'bgp_router_refs_data_session_attributes', 'bgp_router_refs_data_session_attributes_bgp_router', 'bgp_router_refs_data_session_attributes_admin_down', 'bgp_router_refs_data_session_attributes_passive', 'bgp_router_refs_data_session_attributes_as_override', 'bgp_router_refs_data_session_attributes_hold_time', 'bgp_router_refs_data_session_attributes_loop_count', 'bgp_router_refs_data_session_attributes_address_families', 'bgp_router_refs_data_session_attributes_address_families_family', 'bgp_router_refs_data_session_attributes_auth_data', 'bgp_router_refs_data_session_attributes_auth_data_key_type', 'bgp_router_refs_data_session_attributes_auth_data_key_items', 'bgp_router_refs_data_session_attributes_auth_data_key_items_key_id', 'bgp_router_refs_data_session_attributes_auth_data_key_items_key', 'bgp_router_refs_data_session_attributes_family_attributes', 'bgp_router_refs_data_session_attributes_family_attributes_address_family', 'bgp_router_refs_data_session_attributes_family_attributes_loop_count', 'bgp_router_refs_data_session_attributes_family_attributes_prefix_limit', 'bgp_router_refs_data_session_attributes_family_attributes_prefix_limit_maximum', 'routing_instance'
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
        BGP_ROUTER_PARAMETERS: properties.Schema(
            properties.Schema.MAP,
            _('BGP_ROUTER_PARAMETERS.'),
            update_allowed=True,
            required=False,
            schema={
                BGP_ROUTER_PARAMETERS_ADMIN_DOWN: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGP_ROUTER_PARAMETERS_ADMIN_DOWN.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_VENDOR: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_VENDOR.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_IDENTIFIER: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_IDENTIFIER.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGP_ROUTER_PARAMETERS_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_SOURCE_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGP_ROUTER_PARAMETERS_SOURCE_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_HOLD_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGP_ROUTER_PARAMETERS_HOLD_TIME.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 65535),
                    ],
                ),
                BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES: properties.Schema(
                    properties.Schema.MAP,
                    _('BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY: properties.Schema(
                            properties.Schema.LIST,
                            _('BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet6-vpn']),
                            ],
                        ),
                    }
                ),
                BGP_ROUTER_PARAMETERS_AUTH_DATA: properties.Schema(
                    properties.Schema.MAP,
                    _('BGP_ROUTER_PARAMETERS_AUTH_DATA.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE: properties.Schema(
                            properties.Schema.STRING,
                            _('BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'md5']),
                            ],
                        ),
                        BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS: properties.Schema(
                            properties.Schema.LIST,
                            _('BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS.'),
                            update_allowed=True,
                            required=False,
                            schema=properties.Schema(
                                properties.Schema.MAP,
                                schema={
                                    BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(0, 63),
                                        ],
                                    ),
                                    BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                        properties.Schema.STRING,
                                        _('BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            )
                        ),
                    }
                ),
                BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_ROUTER_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_ROUTER_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'control-node', u'external-control-node', u'router', u'bgpaas-server', u'bgpaas-client']),
                    ],
                ),
                BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        BGP_ROUTER_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    BGP_ROUTER_REFS_DATA_SESSION: properties.Schema(
                        properties.Schema.LIST,
                        _('BGP_ROUTER_REFS_DATA_SESSION.'),
                        update_allowed=True,
                        required=False,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                BGP_ROUTER_REFS_DATA_SESSION_UUID: properties.Schema(
                                    properties.Schema.STRING,
                                    _('BGP_ROUTER_REFS_DATA_SESSION_UUID.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES: properties.Schema(
                                    properties.Schema.LIST,
                                    _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES.'),
                                    update_allowed=True,
                                    required=False,
                                    schema=properties.Schema(
                                        properties.Schema.MAP,
                                        schema={
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER: properties.Schema(
                                                properties.Schema.STRING,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE: properties.Schema(
                                                properties.Schema.BOOLEAN,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(0, 65535),
                                                ],
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                                                properties.Schema.INTEGER,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT.'),
                                                update_allowed=True,
                                                required=False,
                                                constraints=[
                                                    constraints.Range(0, 16),
                                                ],
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES: properties.Schema(
                                                properties.Schema.MAP,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY: properties.Schema(
                                                        properties.Schema.LIST,
                                                        _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        constraints=[
                                                            constraints.AllowedValues([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet6-vpn']),
                                                        ],
                                                    ),
                                                }
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA: properties.Schema(
                                                properties.Schema.MAP,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA.'),
                                                update_allowed=True,
                                                required=False,
                                                schema={
                                                    BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE: properties.Schema(
                                                        properties.Schema.STRING,
                                                        _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        constraints=[
                                                            constraints.AllowedValues([u'md5']),
                                                        ],
                                                    ),
                                                    BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS: properties.Schema(
                                                        properties.Schema.LIST,
                                                        _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS.'),
                                                        update_allowed=True,
                                                        required=False,
                                                        schema=properties.Schema(
                                                            properties.Schema.MAP,
                                                            schema={
                                                                BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                                                    properties.Schema.INTEGER,
                                                                    _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                                                    update_allowed=True,
                                                                    required=False,
                                                                    constraints=[
                                                                        constraints.Range(0, 63),
                                                                    ],
                                                                ),
                                                                BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                                                    properties.Schema.STRING,
                                                                    _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY.'),
                                                                    update_allowed=True,
                                                                    required=False,
                                                                ),
                                                            }
                                                        )
                                                    ),
                                                }
                                            ),
                                            BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES: properties.Schema(
                                                properties.Schema.LIST,
                                                _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES.'),
                                                update_allowed=True,
                                                required=False,
                                                schema=properties.Schema(
                                                    properties.Schema.MAP,
                                                    schema={
                                                        BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY: properties.Schema(
                                                            properties.Schema.STRING,
                                                            _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            constraints=[
                                                                constraints.AllowedValues([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet6-vpn']),
                                                            ],
                                                        ),
                                                        BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                                                            properties.Schema.INTEGER,
                                                            _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            constraints=[
                                                                constraints.Range(0, 16),
                                                            ],
                                                        ),
                                                        BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT: properties.Schema(
                                                            properties.Schema.MAP,
                                                            _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT.'),
                                                            update_allowed=True,
                                                            required=False,
                                                            schema={
                                                                BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM: properties.Schema(
                                                                    properties.Schema.INTEGER,
                                                                    _('BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM.'),
                                                                    update_allowed=True,
                                                                    required=False,
                                                                ),
                                                            }
                                                        ),
                                                    }
                                                )
                                            ),
                                        }
                                    )
                                ),
                            }
                        )
                    ),
                }
            )
        ),
        ROUTING_INSTANCE: properties.Schema(
            properties.Schema.STRING,
            _('ROUTING_INSTANCE.'),
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
        BGP_ROUTER_PARAMETERS: attributes.Schema(
            _('BGP_ROUTER_PARAMETERS.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
        BGP_ROUTER_REFS_DATA: attributes.Schema(
            _('BGP_ROUTER_REFS_DATA.'),
        ),
        ROUTING_INSTANCE: attributes.Schema(
            _('ROUTING_INSTANCE.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.ROUTING_INSTANCE):
            try:
                parent_obj = self.vnc_lib().routing_instance_read(id=self.properties.get(self.ROUTING_INSTANCE))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().routing_instance_read(fq_name_str=self.properties.get(self.ROUTING_INSTANCE))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.BgpRouter(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.BGP_ROUTER_PARAMETERS) is not None:
            obj_1 = vnc_api.BgpRouterParams()
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADMIN_DOWN))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_VENDOR) is not None:
                obj_1.set_vendor(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_VENDOR))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_autonomous_system(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IDENTIFIER) is not None:
                obj_1.set_identifier(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IDENTIFIER))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS) is not None:
                obj_1.set_address(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_PORT) is not None:
                obj_1.set_port(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_PORT))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_SOURCE_PORT) is not None:
                obj_1.set_source_port(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_SOURCE_PORT))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_HOLD_TIME) is not None:
                obj_1.set_hold_time(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_HOLD_TIME))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE))
                if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_local_autonomous_system(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ROUTER_TYPE) is not None:
                obj_1.set_router_type(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ROUTER_TYPE))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS) is not None:
                obj_1.set_gateway_address(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS))
            if self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS) is not None:
                obj_1.set_ipv6_gateway_address(self.properties.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS))
            obj_0.set_bgp_router_parameters(obj_1)

        # reference to bgp_router_refs
        obj_1 = None
        if self.properties.get(self.BGP_ROUTER_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA))):
                obj_1 = vnc_api.BgpPeeringAttributes()
                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION) is not None:
                    for index_1 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION))):
                        obj_2 = vnc_api.BgpSession()
                        if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_UUID) is not None:
                            obj_2.set_uuid(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_UUID))
                        if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES) is not None:
                            for index_2 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES))):
                                obj_3 = vnc_api.BgpSessionAttributes()
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                                    obj_3.set_bgp_router(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                                    obj_3.set_admin_down(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE) is not None:
                                    obj_3.set_passive(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                                    obj_3.set_as_override(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                                    obj_3.set_hold_time(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                                    obj_3.set_loop_count(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT))
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                                    obj_4 = vnc_api.AddressFamilies()
                                    if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                                        for index_4 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                                            obj_4.add_family(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_4])
                                    obj_3.set_address_families(obj_4)
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                                    obj_4 = vnc_api.AuthenticationData()
                                    if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                                        obj_4.set_key_type(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                                    if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                                        for index_4 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                                            obj_5 = vnc_api.AuthenticationKeyItem()
                                            if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                                obj_5.set_key_id(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                            if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                                obj_5.set_key(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                                            obj_4.add_key_items(obj_5)
                                    obj_3.set_auth_data(obj_4)
                                if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                                    for index_3 in range(len(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                                        obj_4 = vnc_api.BgpFamilyAttributes()
                                        if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                                            obj_4.set_address_family(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                                        if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                                            obj_4.set_loop_count(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                                        if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                                            obj_5 = vnc_api.BgpPrefixLimit()
                                            if self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                                                obj_5.set_maximum(self.properties.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                                            obj_4.set_prefix_limit(obj_5)
                                        obj_3.add_family_attributes(obj_4)
                                obj_2.add_attributes(obj_3)
                        obj_1.add_session(obj_2)

                if self.properties.get(self.BGP_ROUTER_REFS):
                    try:
                        ref_obj = self.vnc_lib().bgp_router_read(
                            id=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().bgp_router_read(
                            fq_name_str=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                        )
                    obj_0.add_bgp_router(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailBgpRouter, self).resource_create(obj_0)
        except:
            raise Exception(_('bgp-router %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().bgp_router_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('bgp-router %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.BGP_ROUTER_PARAMETERS) is not None:
            obj_1 = vnc_api.BgpRouterParams()
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADMIN_DOWN))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_VENDOR) is not None:
                obj_1.set_vendor(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_VENDOR))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_autonomous_system(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTONOMOUS_SYSTEM))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IDENTIFIER) is not None:
                obj_1.set_identifier(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IDENTIFIER))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS) is not None:
                obj_1.set_address(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_PORT) is not None:
                obj_1.set_port(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_PORT))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_SOURCE_PORT) is not None:
                obj_1.set_source_port(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_SOURCE_PORT))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_HOLD_TIME) is not None:
                obj_1.set_hold_time(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_HOLD_TIME))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_PARAMETERS_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_TYPE))
                if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA, {}).get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGP_ROUTER_PARAMETERS_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM) is not None:
                obj_1.set_local_autonomous_system(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_LOCAL_AUTONOMOUS_SYSTEM))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ROUTER_TYPE) is not None:
                obj_1.set_router_type(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_ROUTER_TYPE))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS) is not None:
                obj_1.set_gateway_address(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_GATEWAY_ADDRESS))
            if prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS) is not None:
                obj_1.set_ipv6_gateway_address(prop_diff.get(self.BGP_ROUTER_PARAMETERS, {}).get(self.BGP_ROUTER_PARAMETERS_IPV6_GATEWAY_ADDRESS))
            obj_0.set_bgp_router_parameters(obj_1)

        # reference to bgp_router
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.BGP_ROUTER_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA))):
                obj_1 = vnc_api.BgpPeeringAttributes()
                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION) is not None:
                    for index_1 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION))):
                        obj_2 = vnc_api.BgpSession()
                        if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_UUID) is not None:
                            obj_2.set_uuid(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_UUID))
                        if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES) is not None:
                            for index_2 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES))):
                                obj_3 = vnc_api.BgpSessionAttributes()
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                                    obj_3.set_bgp_router(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_BGP_ROUTER))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                                    obj_3.set_admin_down(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADMIN_DOWN))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE) is not None:
                                    obj_3.set_passive(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_PASSIVE))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                                    obj_3.set_as_override(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AS_OVERRIDE))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                                    obj_3.set_hold_time(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_HOLD_TIME))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                                    obj_3.set_loop_count(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_LOOP_COUNT))
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                                    obj_4 = vnc_api.AddressFamilies()
                                    if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                                        for index_4 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                                            obj_4.add_family(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_4])
                                    obj_3.set_address_families(obj_4)
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                                    obj_4 = vnc_api.AuthenticationData()
                                    if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                                        obj_4.set_key_type(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                                    if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                                        for index_4 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                                            obj_5 = vnc_api.AuthenticationKeyItem()
                                            if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                                                obj_5.set_key_id(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                                            if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                                                obj_5.set_key(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_4].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                                            obj_4.add_key_items(obj_5)
                                    obj_3.set_auth_data(obj_4)
                                if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                                    for index_3 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                                        obj_4 = vnc_api.BgpFamilyAttributes()
                                        if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                                            obj_4.set_address_family(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                                        if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                                            obj_4.set_loop_count(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                                        if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                                            obj_5 = vnc_api.BgpPrefixLimit()
                                            if prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                                                obj_5.set_maximum(prop_diff.get(self.BGP_ROUTER_REFS_DATA, {})[index_0].get(self.BGP_ROUTER_REFS_DATA_SESSION, {})[index_1].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES, {})[index_2].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_3].get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGP_ROUTER_REFS_DATA_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                                            obj_4.set_prefix_limit(obj_5)
                                        obj_3.add_family_attributes(obj_4)
                                obj_2.add_attributes(obj_3)
                        obj_1.add_session(obj_2)
                ref_data_list.append(obj_1)
        if self.BGP_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.BGP_ROUTER_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        id=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        fq_name_str=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_bgp_router_list(ref_obj_list, ref_data_list)
            # End: reference to bgp_router_refs

        try:
            self.vnc_lib().bgp_router_update(obj_0)
        except:
            raise Exception(_('bgp-router %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().bgp_router_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('bgp_router %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().bgp_router_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::BgpRouter': ContrailBgpRouter,
    }
