
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


class ContrailBgpAsAService(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, BGPAAS_SESSION_ATTRIBUTES, BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER, BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN, BGPAAS_SESSION_ATTRIBUTES_PASSIVE, BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE, BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME, BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT, BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID, BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM, DISPLAY_NAME, BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT, BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP, BGPAAS_IP_ADDRESS, AUTONOMOUS_SYSTEM, BGP_ROUTER_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'bgpaas_session_attributes', 'bgpaas_session_attributes_bgp_router', 'bgpaas_session_attributes_admin_down', 'bgpaas_session_attributes_passive', 'bgpaas_session_attributes_as_override', 'bgpaas_session_attributes_hold_time', 'bgpaas_session_attributes_loop_count', 'bgpaas_session_attributes_address_families', 'bgpaas_session_attributes_address_families_family', 'bgpaas_session_attributes_auth_data', 'bgpaas_session_attributes_auth_data_key_type', 'bgpaas_session_attributes_auth_data_key_items', 'bgpaas_session_attributes_auth_data_key_items_key_id', 'bgpaas_session_attributes_auth_data_key_items_key', 'bgpaas_session_attributes_family_attributes', 'bgpaas_session_attributes_family_attributes_address_family', 'bgpaas_session_attributes_family_attributes_loop_count', 'bgpaas_session_attributes_family_attributes_prefix_limit', 'bgpaas_session_attributes_family_attributes_prefix_limit_maximum', 'display_name', 'bgpaas_suppress_route_advertisement', 'bgpaas_ipv4_mapped_ipv6_nexthop', 'bgpaas_ip_address', 'autonomous_system', 'bgp_router_refs', 'virtual_machine_interface_refs', 'project'
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
        BGPAAS_SESSION_ATTRIBUTES: properties.Schema(
            properties.Schema.MAP,
            _('BGPAAS_SESSION_ATTRIBUTES.'),
            update_allowed=True,
            required=False,
            schema={
                BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER: properties.Schema(
                    properties.Schema.STRING,
                    _('BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_PASSIVE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_PASSIVE.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE.'),
                    update_allowed=True,
                    required=False,
                ),
                BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 65535),
                    ],
                ),
                BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 16),
                    ],
                ),
                BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES: properties.Schema(
                    properties.Schema.MAP,
                    _('BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY: properties.Schema(
                            properties.Schema.LIST,
                            _('BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet6-vpn']),
                            ],
                        ),
                    }
                ),
                BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA: properties.Schema(
                    properties.Schema.MAP,
                    _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE: properties.Schema(
                            properties.Schema.STRING,
                            _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE.'),
                            update_allowed=True,
                            required=False,
                            constraints=[
                                constraints.AllowedValues([u'md5']),
                            ],
                        ),
                        BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS: properties.Schema(
                            properties.Schema.LIST,
                            _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS.'),
                            update_allowed=True,
                            required=False,
                            schema=properties.Schema(
                                properties.Schema.MAP,
                                schema={
                                    BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.Range(0, 63),
                                        ],
                                    ),
                                    BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY: properties.Schema(
                                        properties.Schema.STRING,
                                        _('BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            )
                        ),
                    }
                ),
                BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES: properties.Schema(
                    properties.Schema.LIST,
                    _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY: properties.Schema(
                                properties.Schema.STRING,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6', u'inet6-vpn']),
                                ],
                            ),
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 16),
                                ],
                            ),
                            BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT: properties.Schema(
                                properties.Schema.MAP,
                                _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM.'),
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
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP.'),
            update_allowed=True,
            required=False,
        ),
        BGPAAS_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('BGPAAS_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        AUTONOMOUS_SYSTEM: properties.Schema(
            properties.Schema.INTEGER,
            _('AUTONOMOUS_SYSTEM.'),
            update_allowed=True,
            required=False,
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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
        BGPAAS_SESSION_ATTRIBUTES: attributes.Schema(
            _('BGPAAS_SESSION_ATTRIBUTES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT: attributes.Schema(
            _('BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT.'),
        ),
        BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP: attributes.Schema(
            _('BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP.'),
        ),
        BGPAAS_IP_ADDRESS: attributes.Schema(
            _('BGPAAS_IP_ADDRESS.'),
        ),
        AUTONOMOUS_SYSTEM: attributes.Schema(
            _('AUTONOMOUS_SYSTEM.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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

        obj_0 = vnc_api.BgpAsAService(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES) is not None:
            obj_1 = vnc_api.BgpSessionAttributes()
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE) is not None:
                obj_1.set_passive(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                obj_1.set_as_override(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                obj_1.set_hold_time(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                obj_1.set_loop_count(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT))
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                for index_1 in range(len(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                    obj_2 = vnc_api.BgpFamilyAttributes()
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                        obj_2.set_address_family(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                        obj_2.set_loop_count(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                    if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                        obj_3 = vnc_api.BgpPrefixLimit()
                        if self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                            obj_3.set_maximum(self.properties.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                        obj_2.set_prefix_limit(obj_3)
                    obj_1.add_family_attributes(obj_2)
            obj_0.set_bgpaas_session_attributes(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT) is not None:
            obj_0.set_bgpaas_suppress_route_advertisement(self.properties.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT))
        if self.properties.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP) is not None:
            obj_0.set_bgpaas_ipv4_mapped_ipv6_nexthop(self.properties.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP))
        if self.properties.get(self.BGPAAS_IP_ADDRESS) is not None:
            obj_0.set_bgpaas_ip_address(self.properties.get(self.BGPAAS_IP_ADDRESS))
        if self.properties.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(self.properties.get(self.AUTONOMOUS_SYSTEM))

        # reference to bgp_router_refs
        if self.properties.get(self.BGP_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.BGP_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        id=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        fq_name_str=self.properties.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                obj_0.add_bgp_router(ref_obj)

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

        try:
            obj_uuid = super(ContrailBgpAsAService, self).resource_create(obj_0)
        except:
            raise Exception(_('bgp-as-a-service %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().bgp_as_a_service_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('bgp-as-a-service %s not found.') % self.name)

        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES) is not None:
            obj_1 = vnc_api.BgpSessionAttributes()
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_BGP_ROUTER))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN) is not None:
                obj_1.set_admin_down(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADMIN_DOWN))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE) is not None:
                obj_1.set_passive(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_PASSIVE))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE) is not None:
                obj_1.set_as_override(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AS_OVERRIDE))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME) is not None:
                obj_1.set_hold_time(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_HOLD_TIME))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT) is not None:
                obj_1.set_loop_count(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_LOOP_COUNT))
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES) is not None:
                obj_2 = vnc_api.AddressFamilies()
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY))):
                        obj_2.add_family(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_ADDRESS_FAMILIES_FAMILY)[index_2])
                obj_1.set_address_families(obj_2)
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA) is not None:
                obj_2 = vnc_api.AuthenticationData()
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE) is not None:
                    obj_2.set_key_type(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_TYPE))
                if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS) is not None:
                    for index_2 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS))):
                        obj_3 = vnc_api.AuthenticationKeyItem()
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID) is not None:
                            obj_3.set_key_id(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY_ID))
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY) is not None:
                            obj_3.set_key(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS, {})[index_2].get(self.BGPAAS_SESSION_ATTRIBUTES_AUTH_DATA_KEY_ITEMS_KEY))
                        obj_2.add_key_items(obj_3)
                obj_1.set_auth_data(obj_2)
            if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES) is not None:
                for index_1 in range(len(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES))):
                    obj_2 = vnc_api.BgpFamilyAttributes()
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY) is not None:
                        obj_2.set_address_family(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_ADDRESS_FAMILY))
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT) is not None:
                        obj_2.set_loop_count(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_LOOP_COUNT))
                    if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT) is not None:
                        obj_3 = vnc_api.BgpPrefixLimit()
                        if prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM) is not None:
                            obj_3.set_maximum(prop_diff.get(self.BGPAAS_SESSION_ATTRIBUTES, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES, {})[index_1].get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT, {}).get(self.BGPAAS_SESSION_ATTRIBUTES_FAMILY_ATTRIBUTES_PREFIX_LIMIT_MAXIMUM))
                        obj_2.set_prefix_limit(obj_3)
                    obj_1.add_family_attributes(obj_2)
            obj_0.set_bgpaas_session_attributes(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT) is not None:
            obj_0.set_bgpaas_suppress_route_advertisement(prop_diff.get(self.BGPAAS_SUPPRESS_ROUTE_ADVERTISEMENT))
        if prop_diff.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP) is not None:
            obj_0.set_bgpaas_ipv4_mapped_ipv6_nexthop(prop_diff.get(self.BGPAAS_IPV4_MAPPED_IPV6_NEXTHOP))
        if prop_diff.get(self.BGPAAS_IP_ADDRESS) is not None:
            obj_0.set_bgpaas_ip_address(prop_diff.get(self.BGPAAS_IP_ADDRESS))
        if prop_diff.get(self.AUTONOMOUS_SYSTEM) is not None:
            obj_0.set_autonomous_system(prop_diff.get(self.AUTONOMOUS_SYSTEM))

        # reference to bgp_router_refs
        ref_obj_list = []
        ref_data_list = []
        if self.BGP_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.BGP_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        id=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().bgp_router_read(
                        fq_name_str=prop_diff.get(self.BGP_ROUTER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_bgp_router_list(ref_obj_list)
            # End: reference to bgp_router_refs

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

        try:
            self.vnc_lib().bgp_as_a_service_update(obj_0)
        except:
            raise Exception(_('bgp-as-a-service %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().bgp_as_a_service_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('bgp_as_a_service %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().bgp_as_a_service_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::BgpAsAService': ContrailBgpAsAService,
    }
