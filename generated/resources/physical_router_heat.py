
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


class ContrailPhysicalRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, PHYSICAL_ROUTER_MANAGEMENT_IP, PHYSICAL_ROUTER_SNMP_CREDENTIALS, PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION, PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES, PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS, PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME, DISPLAY_NAME, PHYSICAL_ROUTER_VENDOR_NAME, PHYSICAL_ROUTER_PRODUCT_NAME, PHYSICAL_ROUTER_USER_CREDENTIALS, PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME, PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD, PHYSICAL_ROUTER_VNC_MANAGED, PHYSICAL_ROUTER_DATAPLANE_IP, PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT, VIRTUAL_ROUTER_REFS, BGP_ROUTER_REFS, VIRTUAL_NETWORK_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'physical_router_management_ip', 'physical_router_snmp_credentials', 'physical_router_snmp_credentials_version', 'physical_router_snmp_credentials_local_port', 'physical_router_snmp_credentials_retries', 'physical_router_snmp_credentials_timeout', 'physical_router_snmp_credentials_v2_community', 'physical_router_snmp_credentials_v3_security_name', 'physical_router_snmp_credentials_v3_security_level', 'physical_router_snmp_credentials_v3_security_engine_id', 'physical_router_snmp_credentials_v3_context', 'physical_router_snmp_credentials_v3_context_engine_id', 'physical_router_snmp_credentials_v3_authentication_protocol', 'physical_router_snmp_credentials_v3_authentication_password', 'physical_router_snmp_credentials_v3_privacy_protocol', 'physical_router_snmp_credentials_v3_privacy_password', 'physical_router_snmp_credentials_v3_engine_id', 'physical_router_snmp_credentials_v3_engine_boots', 'physical_router_snmp_credentials_v3_engine_time', 'display_name', 'physical_router_vendor_name', 'physical_router_product_name', 'physical_router_user_credentials', 'physical_router_user_credentials_username', 'physical_router_user_credentials_password', 'physical_router_vnc_managed', 'physical_router_dataplane_ip', 'physical_router_junos_service_ports', 'physical_router_junos_service_ports_service_port', 'virtual_router_refs', 'bgp_router_refs', 'virtual_network_refs', 'global_system_config'
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
        PHYSICAL_ROUTER_MANAGEMENT_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_MANAGEMENT_IP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_SNMP_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_SNMP_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME.'),
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
        PHYSICAL_ROUTER_VENDOR_NAME: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_VENDOR_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_PRODUCT_NAME: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_PRODUCT_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_USER_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_USER_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME.'),
                    update_allowed=True,
                    required=False,
                ),
                PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        PHYSICAL_ROUTER_VNC_MANAGED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('PHYSICAL_ROUTER_VNC_MANAGED.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_DATAPLANE_IP: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER_DATAPLANE_IP.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS: properties.Schema(
            properties.Schema.MAP,
            _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS.'),
            update_allowed=True,
            required=False,
            schema={
                PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT: properties.Schema(
                    properties.Schema.LIST,
                    _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        VIRTUAL_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        BGP_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('BGP_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
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
        PHYSICAL_ROUTER_MANAGEMENT_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_MANAGEMENT_IP.'),
        ),
        PHYSICAL_ROUTER_SNMP_CREDENTIALS: attributes.Schema(
            _('PHYSICAL_ROUTER_SNMP_CREDENTIALS.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PHYSICAL_ROUTER_VENDOR_NAME: attributes.Schema(
            _('PHYSICAL_ROUTER_VENDOR_NAME.'),
        ),
        PHYSICAL_ROUTER_PRODUCT_NAME: attributes.Schema(
            _('PHYSICAL_ROUTER_PRODUCT_NAME.'),
        ),
        PHYSICAL_ROUTER_USER_CREDENTIALS: attributes.Schema(
            _('PHYSICAL_ROUTER_USER_CREDENTIALS.'),
        ),
        PHYSICAL_ROUTER_VNC_MANAGED: attributes.Schema(
            _('PHYSICAL_ROUTER_VNC_MANAGED.'),
        ),
        PHYSICAL_ROUTER_DATAPLANE_IP: attributes.Schema(
            _('PHYSICAL_ROUTER_DATAPLANE_IP.'),
        ),
        PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS: attributes.Schema(
            _('PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS.'),
        ),
        VIRTUAL_ROUTER_REFS: attributes.Schema(
            _('VIRTUAL_ROUTER_REFS.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
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

        obj_0 = vnc_api.PhysicalRouter(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP) is not None:
            obj_0.set_physical_router_management_ip(self.properties.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP))
        if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS) is not None:
            obj_1 = vnc_api.SNMPCredentials()
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION) is not None:
                obj_1.set_version(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT) is not None:
                obj_1.set_local_port(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES) is not None:
                obj_1.set_retries(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT) is not None:
                obj_1.set_timeout(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY) is not None:
                obj_1.set_v2_community(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME) is not None:
                obj_1.set_v3_security_name(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL) is not None:
                obj_1.set_v3_security_level(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID) is not None:
                obj_1.set_v3_security_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT) is not None:
                obj_1.set_v3_context(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID) is not None:
                obj_1.set_v3_context_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL) is not None:
                obj_1.set_v3_authentication_protocol(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD) is not None:
                obj_1.set_v3_authentication_password(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL) is not None:
                obj_1.set_v3_privacy_protocol(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD) is not None:
                obj_1.set_v3_privacy_password(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID) is not None:
                obj_1.set_v3_engine_id(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS) is not None:
                obj_1.set_v3_engine_boots(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS))
            if self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME) is not None:
                obj_1.set_v3_engine_time(self.properties.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME))
            obj_0.set_physical_router_snmp_credentials(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PHYSICAL_ROUTER_VENDOR_NAME) is not None:
            obj_0.set_physical_router_vendor_name(self.properties.get(self.PHYSICAL_ROUTER_VENDOR_NAME))
        if self.properties.get(self.PHYSICAL_ROUTER_PRODUCT_NAME) is not None:
            obj_0.set_physical_router_product_name(self.properties.get(self.PHYSICAL_ROUTER_PRODUCT_NAME))
        if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME))
            if self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(self.properties.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD))
            obj_0.set_physical_router_user_credentials(obj_1)
        if self.properties.get(self.PHYSICAL_ROUTER_VNC_MANAGED) is not None:
            obj_0.set_physical_router_vnc_managed(self.properties.get(self.PHYSICAL_ROUTER_VNC_MANAGED))
        if self.properties.get(self.PHYSICAL_ROUTER_DATAPLANE_IP) is not None:
            obj_0.set_physical_router_dataplane_ip(self.properties.get(self.PHYSICAL_ROUTER_DATAPLANE_IP))
        if self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS) is not None:
            obj_1 = vnc_api.JunosServicePorts()
            if self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT) is not None:
                for index_1 in range(len(self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT))):
                    obj_1.add_service_port(self.properties.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT)[index_1])
            obj_0.set_physical_router_junos_service_ports(obj_1)

        # reference to virtual_router_refs
        if self.properties.get(self.VIRTUAL_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        id=self.properties.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                obj_0.add_virtual_router(ref_obj)

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

        try:
            obj_uuid = super(ContrailPhysicalRouter, self).resource_create(obj_0)
        except:
            raise Exception(_('physical-router %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().physical_router_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('physical-router %s not found.') % self.name)

        if prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP) is not None:
            obj_0.set_physical_router_management_ip(prop_diff.get(self.PHYSICAL_ROUTER_MANAGEMENT_IP))
        if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS) is not None:
            obj_1 = vnc_api.SNMPCredentials()
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION) is not None:
                obj_1.set_version(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_VERSION))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT) is not None:
                obj_1.set_local_port(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_LOCAL_PORT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES) is not None:
                obj_1.set_retries(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_RETRIES))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT) is not None:
                obj_1.set_timeout(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_TIMEOUT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY) is not None:
                obj_1.set_v2_community(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V2_COMMUNITY))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME) is not None:
                obj_1.set_v3_security_name(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_NAME))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL) is not None:
                obj_1.set_v3_security_level(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_LEVEL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID) is not None:
                obj_1.set_v3_security_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_SECURITY_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT) is not None:
                obj_1.set_v3_context(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID) is not None:
                obj_1.set_v3_context_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_CONTEXT_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL) is not None:
                obj_1.set_v3_authentication_protocol(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PROTOCOL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD) is not None:
                obj_1.set_v3_authentication_password(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_AUTHENTICATION_PASSWORD))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL) is not None:
                obj_1.set_v3_privacy_protocol(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PROTOCOL))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD) is not None:
                obj_1.set_v3_privacy_password(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_PRIVACY_PASSWORD))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID) is not None:
                obj_1.set_v3_engine_id(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_ID))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS) is not None:
                obj_1.set_v3_engine_boots(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_BOOTS))
            if prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME) is not None:
                obj_1.set_v3_engine_time(prop_diff.get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_SNMP_CREDENTIALS_V3_ENGINE_TIME))
            obj_0.set_physical_router_snmp_credentials(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_VENDOR_NAME) is not None:
            obj_0.set_physical_router_vendor_name(prop_diff.get(self.PHYSICAL_ROUTER_VENDOR_NAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_PRODUCT_NAME) is not None:
            obj_0.set_physical_router_product_name(prop_diff.get(self.PHYSICAL_ROUTER_PRODUCT_NAME))
        if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_USERNAME))
            if prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(prop_diff.get(self.PHYSICAL_ROUTER_USER_CREDENTIALS, {}).get(self.PHYSICAL_ROUTER_USER_CREDENTIALS_PASSWORD))
            obj_0.set_physical_router_user_credentials(obj_1)
        if prop_diff.get(self.PHYSICAL_ROUTER_VNC_MANAGED) is not None:
            obj_0.set_physical_router_vnc_managed(prop_diff.get(self.PHYSICAL_ROUTER_VNC_MANAGED))
        if prop_diff.get(self.PHYSICAL_ROUTER_DATAPLANE_IP) is not None:
            obj_0.set_physical_router_dataplane_ip(prop_diff.get(self.PHYSICAL_ROUTER_DATAPLANE_IP))
        if prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS) is not None:
            obj_1 = vnc_api.JunosServicePorts()
            if prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT) is not None:
                for index_1 in range(len(prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT))):
                    obj_1.add_service_port(prop_diff.get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS, {}).get(self.PHYSICAL_ROUTER_JUNOS_SERVICE_PORTS_SERVICE_PORT)[index_1])
            obj_0.set_physical_router_junos_service_ports(obj_1)

        # reference to virtual_router_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        id=prop_diff.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_router_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_ROUTER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_router_list(ref_obj_list)
            # End: reference to virtual_router_refs

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

        try:
            self.vnc_lib().physical_router_update(obj_0)
        except:
            raise Exception(_('physical-router %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().physical_router_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('physical_router %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().physical_router_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::PhysicalRouter': ContrailPhysicalRouter,
    }
