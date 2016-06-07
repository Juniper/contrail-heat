
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


class ContrailGlobalVrouterConfig(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ECMP_HASHING_INCLUDE_FIELDS, ECMP_HASHING_INCLUDE_FIELDS_HASHING_CONFIGURED, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_IP, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_IP, ECMP_HASHING_INCLUDE_FIELDS_IP_PROTOCOL, ECMP_HASHING_INCLUDE_FIELDS_SOURCE_PORT, ECMP_HASHING_INCLUDE_FIELDS_DESTINATION_PORT, FLOW_AGING_TIMEOUT_LIST, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT, FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS, DISPLAY_NAME, FORWARDING_MODE, FLOW_EXPORT_RATE, LINKLOCAL_SERVICES, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT, LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP, ENCAPSULATION_PRIORITIES, ENCAPSULATION_PRIORITIES_ENCAPSULATION, VXLAN_NETWORK_IDENTIFIER_MODE, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'ecmp_hashing_include_fields', 'ecmp_hashing_include_fields_hashing_configured', 'ecmp_hashing_include_fields_source_ip', 'ecmp_hashing_include_fields_destination_ip', 'ecmp_hashing_include_fields_ip_protocol', 'ecmp_hashing_include_fields_source_port', 'ecmp_hashing_include_fields_destination_port', 'flow_aging_timeout_list', 'flow_aging_timeout_list_flow_aging_timeout', 'flow_aging_timeout_list_flow_aging_timeout_protocol', 'flow_aging_timeout_list_flow_aging_timeout_port', 'flow_aging_timeout_list_flow_aging_timeout_timeout_in_seconds', 'display_name', 'forwarding_mode', 'flow_export_rate', 'linklocal_services', 'linklocal_services_linklocal_service_entry', 'linklocal_services_linklocal_service_entry_linklocal_service_name', 'linklocal_services_linklocal_service_entry_linklocal_service_ip', 'linklocal_services_linklocal_service_entry_linklocal_service_port', 'linklocal_services_linklocal_service_entry_ip_fabric_dns_service_name', 'linklocal_services_linklocal_service_entry_ip_fabric_service_port', 'linklocal_services_linklocal_service_entry_ip_fabric_service_ip', 'encapsulation_priorities', 'encapsulation_priorities_encapsulation', 'vxlan_network_identifier_mode', 'global_system_config'
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
        FLOW_AGING_TIMEOUT_LIST: properties.Schema(
            properties.Schema.MAP,
            _('FLOW_AGING_TIMEOUT_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT: properties.Schema(
                    properties.Schema.LIST,
                    _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL: properties.Schema(
                                properties.Schema.STRING,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS.'),
                                update_allowed=True,
                                required=False,
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
        FORWARDING_MODE: properties.Schema(
            properties.Schema.STRING,
            _('FORWARDING_MODE.'),
            update_allowed=True,
            required=False,
        ),
        FLOW_EXPORT_RATE: properties.Schema(
            properties.Schema.INTEGER,
            _('FLOW_EXPORT_RATE.'),
            update_allowed=True,
            required=False,
        ),
        LINKLOCAL_SERVICES: properties.Schema(
            properties.Schema.MAP,
            _('LINKLOCAL_SERVICES.'),
            update_allowed=True,
            required=False,
            schema={
                LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY: properties.Schema(
                    properties.Schema.LIST,
                    _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP: properties.Schema(
                                properties.Schema.LIST,
                                _('LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        ENCAPSULATION_PRIORITIES: properties.Schema(
            properties.Schema.MAP,
            _('ENCAPSULATION_PRIORITIES.'),
            update_allowed=True,
            required=False,
            schema={
                ENCAPSULATION_PRIORITIES_ENCAPSULATION: properties.Schema(
                    properties.Schema.LIST,
                    _('ENCAPSULATION_PRIORITIES_ENCAPSULATION.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'MPLSoGRE', u'MPLSoUDP', u'VXLAN']),
                    ],
                ),
            }
        ),
        VXLAN_NETWORK_IDENTIFIER_MODE: properties.Schema(
            properties.Schema.STRING,
            _('VXLAN_NETWORK_IDENTIFIER_MODE.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
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
        FLOW_AGING_TIMEOUT_LIST: attributes.Schema(
            _('FLOW_AGING_TIMEOUT_LIST.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        FORWARDING_MODE: attributes.Schema(
            _('FORWARDING_MODE.'),
        ),
        FLOW_EXPORT_RATE: attributes.Schema(
            _('FLOW_EXPORT_RATE.'),
        ),
        LINKLOCAL_SERVICES: attributes.Schema(
            _('LINKLOCAL_SERVICES.'),
        ),
        ENCAPSULATION_PRIORITIES: attributes.Schema(
            _('ENCAPSULATION_PRIORITIES.'),
        ),
        VXLAN_NETWORK_IDENTIFIER_MODE: attributes.Schema(
            _('VXLAN_NETWORK_IDENTIFIER_MODE.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_system_config_read(id=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.GlobalVrouterConfig(name=self.properties[self.NAME],
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
        if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST) is not None:
            obj_1 = vnc_api.FlowAgingTimeoutList()
            if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT) is not None:
                for index_1 in range(len(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT))):
                    obj_2 = vnc_api.FlowAgingTimeout()
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL) is not None:
                        obj_2.set_protocol(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL))
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT) is not None:
                        obj_2.set_port(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT))
                    if self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS) is not None:
                        obj_2.set_timeout_in_seconds(self.properties.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS))
                    obj_1.add_flow_aging_timeout(obj_2)
            obj_0.set_flow_aging_timeout_list(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.FORWARDING_MODE) is not None:
            obj_0.set_forwarding_mode(self.properties.get(self.FORWARDING_MODE))
        if self.properties.get(self.FLOW_EXPORT_RATE) is not None:
            obj_0.set_flow_export_rate(self.properties.get(self.FLOW_EXPORT_RATE))
        if self.properties.get(self.LINKLOCAL_SERVICES) is not None:
            obj_1 = vnc_api.LinklocalServicesTypes()
            if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY) is not None:
                for index_1 in range(len(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY))):
                    obj_2 = vnc_api.LinklocalServiceEntryType()
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME) is not None:
                        obj_2.set_linklocal_service_name(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP) is not None:
                        obj_2.set_linklocal_service_ip(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT) is not None:
                        obj_2.set_linklocal_service_port(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME) is not None:
                        obj_2.set_ip_fabric_DNS_service_name(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT) is not None:
                        obj_2.set_ip_fabric_service_port(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT))
                    if self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP) is not None:
                        for index_2 in range(len(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP))):
                            obj_2.add_ip_fabric_service_ip(self.properties.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP)[index_2])
                    obj_1.add_linklocal_service_entry(obj_2)
            obj_0.set_linklocal_services(obj_1)
        if self.properties.get(self.ENCAPSULATION_PRIORITIES) is not None:
            obj_1 = vnc_api.EncapsulationPrioritiesType()
            if self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION) is not None:
                for index_1 in range(len(self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION))):
                    obj_1.add_encapsulation(self.properties.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION)[index_1])
            obj_0.set_encapsulation_priorities(obj_1)
        if self.properties.get(self.VXLAN_NETWORK_IDENTIFIER_MODE) is not None:
            obj_0.set_vxlan_network_identifier_mode(self.properties.get(self.VXLAN_NETWORK_IDENTIFIER_MODE))

        try:
            obj_uuid = super(ContrailGlobalVrouterConfig, self).resource_create(obj_0)
        except:
            raise Exception(_('global-vrouter-config %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().global_vrouter_config_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('global-vrouter-config %s not found.') % self.name)

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
        if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST) is not None:
            obj_1 = vnc_api.FlowAgingTimeoutList()
            if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT) is not None:
                for index_1 in range(len(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT))):
                    obj_2 = vnc_api.FlowAgingTimeout()
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL) is not None:
                        obj_2.set_protocol(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PROTOCOL))
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT) is not None:
                        obj_2.set_port(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_PORT))
                    if prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS) is not None:
                        obj_2.set_timeout_in_seconds(prop_diff.get(self.FLOW_AGING_TIMEOUT_LIST, {}).get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT, {})[index_1].get(self.FLOW_AGING_TIMEOUT_LIST_FLOW_AGING_TIMEOUT_TIMEOUT_IN_SECONDS))
                    obj_1.add_flow_aging_timeout(obj_2)
            obj_0.set_flow_aging_timeout_list(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.FORWARDING_MODE) is not None:
            obj_0.set_forwarding_mode(prop_diff.get(self.FORWARDING_MODE))
        if prop_diff.get(self.FLOW_EXPORT_RATE) is not None:
            obj_0.set_flow_export_rate(prop_diff.get(self.FLOW_EXPORT_RATE))
        if prop_diff.get(self.LINKLOCAL_SERVICES) is not None:
            obj_1 = vnc_api.LinklocalServicesTypes()
            if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY) is not None:
                for index_1 in range(len(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY))):
                    obj_2 = vnc_api.LinklocalServiceEntryType()
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME) is not None:
                        obj_2.set_linklocal_service_name(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_NAME))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP) is not None:
                        obj_2.set_linklocal_service_ip(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_IP))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT) is not None:
                        obj_2.set_linklocal_service_port(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_LINKLOCAL_SERVICE_PORT))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME) is not None:
                        obj_2.set_ip_fabric_DNS_service_name(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_DNS_SERVICE_NAME))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT) is not None:
                        obj_2.set_ip_fabric_service_port(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_PORT))
                    if prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP) is not None:
                        for index_2 in range(len(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP))):
                            obj_2.add_ip_fabric_service_ip(prop_diff.get(self.LINKLOCAL_SERVICES, {}).get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY, {})[index_1].get(self.LINKLOCAL_SERVICES_LINKLOCAL_SERVICE_ENTRY_IP_FABRIC_SERVICE_IP)[index_2])
                    obj_1.add_linklocal_service_entry(obj_2)
            obj_0.set_linklocal_services(obj_1)
        if prop_diff.get(self.ENCAPSULATION_PRIORITIES) is not None:
            obj_1 = vnc_api.EncapsulationPrioritiesType()
            if prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION) is not None:
                for index_1 in range(len(prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION))):
                    obj_1.add_encapsulation(prop_diff.get(self.ENCAPSULATION_PRIORITIES, {}).get(self.ENCAPSULATION_PRIORITIES_ENCAPSULATION)[index_1])
            obj_0.set_encapsulation_priorities(obj_1)
        if prop_diff.get(self.VXLAN_NETWORK_IDENTIFIER_MODE) is not None:
            obj_0.set_vxlan_network_identifier_mode(prop_diff.get(self.VXLAN_NETWORK_IDENTIFIER_MODE))

        try:
            self.vnc_lib().global_vrouter_config_update(obj_0)
        except:
            raise Exception(_('global-vrouter-config %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().global_vrouter_config_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('global_vrouter_config %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().global_vrouter_config_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::GlobalVrouterConfig': ContrailGlobalVrouterConfig,
    }
