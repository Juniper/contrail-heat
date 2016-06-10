
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


class ContrailRoutingInstance(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ROUTING_INSTANCE_HAS_PNF, ROUTING_INSTANCE_IS_DEFAULT, SERVICE_CHAIN_INFORMATION, SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, SERVICE_CHAIN_INFORMATION_PREFIX, SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION, IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION_PREFIX, IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS, IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE, IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE, STATIC_ROUTE_ENTRIES, STATIC_ROUTE_ENTRIES_ROUTE, STATIC_ROUTE_ENTRIES_ROUTE_PREFIX, STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP, STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET, STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY, DEFAULT_CE_PROTOCOL, DEFAULT_CE_PROTOCOL_BGP, DEFAULT_CE_PROTOCOL_OSPF, DEFAULT_CE_PROTOCOL_OSPF_AREA, ROUTING_INSTANCE_REFS, ROUTING_INSTANCE_REFS_DATA, ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE, ROUTE_TARGET_REFS, ROUTE_TARGET_REFS_DATA, ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT, VIRTUAL_NETWORK
    ) = (
        'name', 'fq_name', 'display_name', 'routing_instance_has_pnf', 'routing_instance_is_default', 'service_chain_information', 'service_chain_information_routing_instance', 'service_chain_information_prefix', 'service_chain_information_service_chain_address', 'service_chain_information_service_instance', 'service_chain_information_source_routing_instance', 'ipv6_service_chain_information', 'ipv6_service_chain_information_routing_instance', 'ipv6_service_chain_information_prefix', 'ipv6_service_chain_information_service_chain_address', 'ipv6_service_chain_information_service_instance', 'ipv6_service_chain_information_source_routing_instance', 'static_route_entries', 'static_route_entries_route', 'static_route_entries_route_prefix', 'static_route_entries_route_next_hop', 'static_route_entries_route_route_target', 'static_route_entries_route_community', 'default_ce_protocol', 'default_ce_protocol_bgp', 'default_ce_protocol_ospf', 'default_ce_protocol_ospf_area', 'routing_instance_refs', 'routing_instance_refs_data', 'routing_instance_refs_data_destination_instance', 'route_target_refs', 'route_target_refs_data', 'route_target_refs_data_import_export', 'virtual_network'
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
        ROUTING_INSTANCE_HAS_PNF: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTING_INSTANCE_HAS_PNF.'),
            update_allowed=True,
            required=False,
        ),
        ROUTING_INSTANCE_IS_DEFAULT: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ROUTING_INSTANCE_IS_DEFAULT.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        IPV6_SERVICE_CHAIN_INFORMATION: properties.Schema(
            properties.Schema.MAP,
            _('IPV6_SERVICE_CHAIN_INFORMATION.'),
            update_allowed=True,
            required=False,
            schema={
                IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_PREFIX: properties.Schema(
                    properties.Schema.LIST,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE: properties.Schema(
                    properties.Schema.STRING,
                    _('IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        STATIC_ROUTE_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('STATIC_ROUTE_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                STATIC_ROUTE_ENTRIES_ROUTE: properties.Schema(
                    properties.Schema.LIST,
                    _('STATIC_ROUTE_ENTRIES_ROUTE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            STATIC_ROUTE_ENTRIES_ROUTE_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP: properties.Schema(
                                properties.Schema.STRING,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET: properties.Schema(
                                properties.Schema.LIST,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET.'),
                                update_allowed=True,
                                required=False,
                            ),
                            STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY: properties.Schema(
                                properties.Schema.LIST,
                                _('STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        DEFAULT_CE_PROTOCOL: properties.Schema(
            properties.Schema.MAP,
            _('DEFAULT_CE_PROTOCOL.'),
            update_allowed=True,
            required=False,
            schema={
                DEFAULT_CE_PROTOCOL_BGP: properties.Schema(
                    properties.Schema.MAP,
                    _('DEFAULT_CE_PROTOCOL_BGP.'),
                    update_allowed=True,
                    required=False,
                ),
                DEFAULT_CE_PROTOCOL_OSPF: properties.Schema(
                    properties.Schema.MAP,
                    _('DEFAULT_CE_PROTOCOL_OSPF.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        DEFAULT_CE_PROTOCOL_OSPF_AREA: properties.Schema(
                            properties.Schema.INTEGER,
                            _('DEFAULT_CE_PROTOCOL_OSPF_AREA.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
            }
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
                    ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        ROUTE_TARGET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TARGET_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TARGET_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TARGET_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT: properties.Schema(
                        properties.Schema.STRING,
                        _('ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT.'),
                        update_allowed=True,
                        required=False,
                        constraints=[
                            constraints.AllowedValues([u'import', u'export']),
                        ],
                    ),
                }
            )
        ),
        VIRTUAL_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK.'),
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
        ROUTING_INSTANCE_HAS_PNF: attributes.Schema(
            _('ROUTING_INSTANCE_HAS_PNF.'),
        ),
        ROUTING_INSTANCE_IS_DEFAULT: attributes.Schema(
            _('ROUTING_INSTANCE_IS_DEFAULT.'),
        ),
        SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('SERVICE_CHAIN_INFORMATION.'),
        ),
        IPV6_SERVICE_CHAIN_INFORMATION: attributes.Schema(
            _('IPV6_SERVICE_CHAIN_INFORMATION.'),
        ),
        STATIC_ROUTE_ENTRIES: attributes.Schema(
            _('STATIC_ROUTE_ENTRIES.'),
        ),
        DEFAULT_CE_PROTOCOL: attributes.Schema(
            _('DEFAULT_CE_PROTOCOL.'),
        ),
        ROUTING_INSTANCE_REFS: attributes.Schema(
            _('ROUTING_INSTANCE_REFS.'),
        ),
        ROUTING_INSTANCE_REFS_DATA: attributes.Schema(
            _('ROUTING_INSTANCE_REFS_DATA.'),
        ),
        ROUTE_TARGET_REFS: attributes.Schema(
            _('ROUTE_TARGET_REFS.'),
        ),
        ROUTE_TARGET_REFS_DATA: attributes.Schema(
            _('ROUTE_TARGET_REFS_DATA.'),
        ),
        VIRTUAL_NETWORK: attributes.Schema(
            _('VIRTUAL_NETWORK.'),
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

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.RoutingInstance(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ROUTING_INSTANCE_HAS_PNF) is not None:
            obj_0.set_routing_instance_has_pnf(self.properties.get(self.ROUTING_INSTANCE_HAS_PNF))
        if self.properties.get(self.ROUTING_INSTANCE_IS_DEFAULT) is not None:
            obj_0.set_routing_instance_is_default(self.properties.get(self.ROUTING_INSTANCE_IS_DEFAULT))
        if self.properties.get(self.SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            obj_0.set_service_chain_information(obj_1)
        if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(self.properties.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            obj_0.set_ipv6_service_chain_information(obj_1)
        if self.properties.get(self.STATIC_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.StaticRouteEntriesType()
            if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE))):
                    obj_2 = vnc_api.StaticRouteType()
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX))
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP))
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET) is not None:
                        for index_2 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET))):
                            obj_2.add_route_target(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET)[index_2])
                    if self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY) is not None:
                        for index_2 in range(len(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY))):
                            obj_2.add_community(self.properties.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY)[index_2])
                    obj_1.add_route(obj_2)
            obj_0.set_static_route_entries(obj_1)
        if self.properties.get(self.DEFAULT_CE_PROTOCOL) is not None:
            obj_1 = vnc_api.DefaultProtocolType()
            if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP) is not None:
                obj_1.set_bgp(self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP))
            if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF) is not None:
                obj_2 = vnc_api.ProtocolOspfType()
                if self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA) is not None:
                    obj_2.set_area(self.properties.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA))
                obj_1.set_ospf(obj_2)
            obj_0.set_default_ce_protocol(obj_1)

        # reference to routing_instance_refs
        obj_1 = None
        if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ConnectionType()
                if self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE) is not None:
                    obj_1.set_destination_instance(self.properties.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE))

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

        # reference to route_target_refs
        obj_1 = None
        if self.properties.get(self.ROUTE_TARGET_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.ROUTE_TARGET_REFS_DATA))):
                obj_1 = vnc_api.InstanceTargetType()
                if self.properties.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT) is not None:
                    obj_1.set_import_export(self.properties.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT))

                if self.properties.get(self.ROUTE_TARGET_REFS):
                    try:
                        ref_obj = self.vnc_lib().route_target_read(
                            id=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().route_target_read(
                            fq_name_str=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                        )
                    obj_0.add_route_target(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailRoutingInstance, self).resource_create(obj_0)
        except:
            raise Exception(_('routing-instance %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().routing_instance_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('routing-instance %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ROUTING_INSTANCE_HAS_PNF) is not None:
            obj_0.set_routing_instance_has_pnf(prop_diff.get(self.ROUTING_INSTANCE_HAS_PNF))
        if prop_diff.get(self.ROUTING_INSTANCE_IS_DEFAULT) is not None:
            obj_0.set_routing_instance_is_default(prop_diff.get(self.ROUTING_INSTANCE_IS_DEFAULT))
        if prop_diff.get(self.SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.SERVICE_CHAIN_INFORMATION, {}).get(self.SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            obj_0.set_service_chain_information(obj_1)
        if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION) is not None:
            obj_1 = vnc_api.ServiceChainInfo()
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE) is not None:
                obj_1.set_routing_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_ROUTING_INSTANCE))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX) is not None:
                for index_1 in range(len(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX))):
                    obj_1.add_prefix(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_PREFIX)[index_1])
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS) is not None:
                obj_1.set_service_chain_address(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_CHAIN_ADDRESS))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SERVICE_INSTANCE))
            if prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE) is not None:
                obj_1.set_source_routing_instance(prop_diff.get(self.IPV6_SERVICE_CHAIN_INFORMATION, {}).get(self.IPV6_SERVICE_CHAIN_INFORMATION_SOURCE_ROUTING_INSTANCE))
            obj_0.set_ipv6_service_chain_information(obj_1)
        if prop_diff.get(self.STATIC_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.StaticRouteEntriesType()
            if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE))):
                    obj_2 = vnc_api.StaticRouteType()
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_PREFIX))
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_NEXT_HOP))
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET) is not None:
                        for index_2 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET))):
                            obj_2.add_route_target(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_ROUTE_TARGET)[index_2])
                    if prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY) is not None:
                        for index_2 in range(len(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY))):
                            obj_2.add_community(prop_diff.get(self.STATIC_ROUTE_ENTRIES, {}).get(self.STATIC_ROUTE_ENTRIES_ROUTE, {})[index_1].get(self.STATIC_ROUTE_ENTRIES_ROUTE_COMMUNITY)[index_2])
                    obj_1.add_route(obj_2)
            obj_0.set_static_route_entries(obj_1)
        if prop_diff.get(self.DEFAULT_CE_PROTOCOL) is not None:
            obj_1 = vnc_api.DefaultProtocolType()
            if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP) is not None:
                obj_1.set_bgp(prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_BGP))
            if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF) is not None:
                obj_2 = vnc_api.ProtocolOspfType()
                if prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA) is not None:
                    obj_2.set_area(prop_diff.get(self.DEFAULT_CE_PROTOCOL, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF, {}).get(self.DEFAULT_CE_PROTOCOL_OSPF_AREA))
                obj_1.set_ospf(obj_2)
            obj_0.set_default_ce_protocol(obj_1)

        # reference to routing_instance
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ConnectionType()
                if prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE) is not None:
                    obj_1.set_destination_instance(prop_diff.get(self.ROUTING_INSTANCE_REFS_DATA, {})[index_0].get(self.ROUTING_INSTANCE_REFS_DATA_DESTINATION_INSTANCE))
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

        # reference to route_target
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.ROUTE_TARGET_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TARGET_REFS_DATA))):
                obj_1 = vnc_api.InstanceTargetType()
                if prop_diff.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT) is not None:
                    obj_1.set_import_export(prop_diff.get(self.ROUTE_TARGET_REFS_DATA, {})[index_0].get(self.ROUTE_TARGET_REFS_DATA_IMPORT_EXPORT))
                ref_data_list.append(obj_1)
        if self.ROUTE_TARGET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TARGET_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().route_target_read(
                        id=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().route_target_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_route_target_list(ref_obj_list, ref_data_list)
            # End: reference to route_target_refs

        try:
            self.vnc_lib().routing_instance_update(obj_0)
        except:
            raise Exception(_('routing-instance %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().routing_instance_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('routing_instance %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().routing_instance_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::RoutingInstance': ContrailRoutingInstance,
    }
