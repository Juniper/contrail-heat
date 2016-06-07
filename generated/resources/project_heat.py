
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


class ContrailProject(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ALARM_ENABLE, DISPLAY_NAME, QUOTA, QUOTA_DEFAULTS, QUOTA_FLOATING_IP, QUOTA_INSTANCE_IP, QUOTA_VIRTUAL_MACHINE_INTERFACE, QUOTA_VIRTUAL_NETWORK, QUOTA_VIRTUAL_ROUTER, QUOTA_VIRTUAL_DNS, QUOTA_VIRTUAL_DNS_RECORD, QUOTA_BGP_ROUTER, QUOTA_NETWORK_IPAM, QUOTA_ACCESS_CONTROL_LIST, QUOTA_NETWORK_POLICY, QUOTA_FLOATING_IP_POOL, QUOTA_SERVICE_TEMPLATE, QUOTA_SERVICE_INSTANCE, QUOTA_LOGICAL_ROUTER, QUOTA_SECURITY_GROUP, QUOTA_SECURITY_GROUP_RULE, QUOTA_SUBNET, QUOTA_GLOBAL_VROUTER_CONFIG, QUOTA_LOADBALANCER_POOL, QUOTA_LOADBALANCER_MEMBER, QUOTA_LOADBALANCER_HEALTHMONITOR, QUOTA_VIRTUAL_IP, NAMESPACE_REFS, NAMESPACE_REFS_DATA, NAMESPACE_REFS_DATA_IP_PREFIX, NAMESPACE_REFS_DATA_IP_PREFIX_LEN, FLOATING_IP_POOL_REFS, ALIAS_IP_POOL_REFS, DOMAIN
    ) = (
        'name', 'fq_name', 'alarm_enable', 'display_name', 'quota', 'quota_defaults', 'quota_floating_ip', 'quota_instance_ip', 'quota_virtual_machine_interface', 'quota_virtual_network', 'quota_virtual_router', 'quota_virtual_dns', 'quota_virtual_dns_record', 'quota_bgp_router', 'quota_network_ipam', 'quota_access_control_list', 'quota_network_policy', 'quota_floating_ip_pool', 'quota_service_template', 'quota_service_instance', 'quota_logical_router', 'quota_security_group', 'quota_security_group_rule', 'quota_subnet', 'quota_global_vrouter_config', 'quota_loadbalancer_pool', 'quota_loadbalancer_member', 'quota_loadbalancer_healthmonitor', 'quota_virtual_ip', 'namespace_refs', 'namespace_refs_data', 'namespace_refs_data_ip_prefix', 'namespace_refs_data_ip_prefix_len', 'floating_ip_pool_refs', 'alias_ip_pool_refs', 'domain'
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
        ALARM_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('ALARM_ENABLE.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        QUOTA: properties.Schema(
            properties.Schema.MAP,
            _('QUOTA.'),
            update_allowed=True,
            required=False,
            schema={
                QUOTA_DEFAULTS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_DEFAULTS.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FLOATING_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FLOATING_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_INSTANCE_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_INSTANCE_IP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_MACHINE_INTERFACE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_MACHINE_INTERFACE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_NETWORK: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_NETWORK.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_DNS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_DNS.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_DNS_RECORD: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_DNS_RECORD.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_BGP_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_BGP_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_NETWORK_IPAM: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_NETWORK_IPAM.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_ACCESS_CONTROL_LIST: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_ACCESS_CONTROL_LIST.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_NETWORK_POLICY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_NETWORK_POLICY.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_FLOATING_IP_POOL: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_FLOATING_IP_POOL.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SERVICE_TEMPLATE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SERVICE_TEMPLATE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SERVICE_INSTANCE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SERVICE_INSTANCE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOGICAL_ROUTER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOGICAL_ROUTER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SECURITY_GROUP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SECURITY_GROUP.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SECURITY_GROUP_RULE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SECURITY_GROUP_RULE.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_SUBNET: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_SUBNET.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_GLOBAL_VROUTER_CONFIG: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_GLOBAL_VROUTER_CONFIG.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_POOL: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_POOL.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_MEMBER: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_MEMBER.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_LOADBALANCER_HEALTHMONITOR: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_LOADBALANCER_HEALTHMONITOR.'),
                    update_allowed=True,
                    required=False,
                ),
                QUOTA_VIRTUAL_IP: properties.Schema(
                    properties.Schema.INTEGER,
                    _('QUOTA_VIRTUAL_IP.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        NAMESPACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NAMESPACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NAMESPACE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NAMESPACE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NAMESPACE_REFS_DATA_IP_PREFIX: properties.Schema(
                        properties.Schema.STRING,
                        _('NAMESPACE_REFS_DATA_IP_PREFIX.'),
                        update_allowed=True,
                        required=False,
                    ),
                    NAMESPACE_REFS_DATA_IP_PREFIX_LEN: properties.Schema(
                        properties.Schema.INTEGER,
                        _('NAMESPACE_REFS_DATA_IP_PREFIX_LEN.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        FLOATING_IP_POOL_REFS: properties.Schema(
            properties.Schema.LIST,
            _('FLOATING_IP_POOL_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ALIAS_IP_POOL_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ALIAS_IP_POOL_REFS.'),
            update_allowed=True,
            required=False,
        ),
        DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('DOMAIN.'),
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
        ALARM_ENABLE: attributes.Schema(
            _('ALARM_ENABLE.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        QUOTA: attributes.Schema(
            _('QUOTA.'),
        ),
        NAMESPACE_REFS: attributes.Schema(
            _('NAMESPACE_REFS.'),
        ),
        NAMESPACE_REFS_DATA: attributes.Schema(
            _('NAMESPACE_REFS_DATA.'),
        ),
        FLOATING_IP_POOL_REFS: attributes.Schema(
            _('FLOATING_IP_POOL_REFS.'),
        ),
        ALIAS_IP_POOL_REFS: attributes.Schema(
            _('ALIAS_IP_POOL_REFS.'),
        ),
        DOMAIN: attributes.Schema(
            _('DOMAIN.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.DOMAIN):
            try:
                parent_obj = self.vnc_lib().domain_read(id=self.properties.get(self.DOMAIN))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().domain_read(fq_name_str=self.properties.get(self.DOMAIN))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.Project(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(self.properties.get(self.ALARM_ENABLE))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.QUOTA) is not None:
            obj_1 = vnc_api.QuotaType()
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS) is not None:
                obj_1.set_defaults(self.properties.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP) is not None:
                obj_1.set_floating_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP) is not None:
                obj_1.set_instance_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE) is not None:
                obj_1.set_virtual_machine_interface(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER) is not None:
                obj_1.set_virtual_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS) is not None:
                obj_1.set_virtual_DNS(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD) is not None:
                obj_1.set_virtual_DNS_record(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM) is not None:
                obj_1.set_network_ipam(self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST) is not None:
                obj_1.set_access_control_list(self.properties.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY) is not None:
                obj_1.set_network_policy(self.properties.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL) is not None:
                obj_1.set_floating_ip_pool(self.properties.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE) is not None:
                obj_1.set_service_template(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER) is not None:
                obj_1.set_logical_router(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP) is not None:
                obj_1.set_security_group(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE) is not None:
                obj_1.set_security_group_rule(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_SUBNET) is not None:
                obj_1.set_subnet(self.properties.get(self.QUOTA, {}).get(self.QUOTA_SUBNET))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG) is not None:
                obj_1.set_global_vrouter_config(self.properties.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL) is not None:
                obj_1.set_loadbalancer_pool(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER) is not None:
                obj_1.set_loadbalancer_member(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR) is not None:
                obj_1.set_loadbalancer_healthmonitor(self.properties.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR))
            if self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP) is not None:
                obj_1.set_virtual_ip(self.properties.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP))
            obj_0.set_quota(obj_1)

        # reference to namespace_refs
        obj_1 = None
        if self.properties.get(self.NAMESPACE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NAMESPACE_REFS_DATA))):
                obj_1 = vnc_api.SubnetType()
                if self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX) is not None:
                    obj_1.set_ip_prefix(self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX))
                if self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN) is not None:
                    obj_1.set_ip_prefix_len(self.properties.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN))

                if self.properties.get(self.NAMESPACE_REFS):
                    try:
                        ref_obj = self.vnc_lib().namespace_read(
                            id=self.properties.get(self.NAMESPACE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().namespace_read(
                            fq_name_str=self.properties.get(self.NAMESPACE_REFS)[index_0]
                        )
                    obj_0.add_namespace(ref_obj, obj_1)

        # reference to floating_ip_pool_refs
        if self.properties.get(self.FLOATING_IP_POOL_REFS):
            for index_0 in range(len(self.properties.get(self.FLOATING_IP_POOL_REFS))):
                try:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        id=self.properties.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        fq_name_str=self.properties.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                obj_0.add_floating_ip_pool(ref_obj)

        # reference to alias_ip_pool_refs
        if self.properties.get(self.ALIAS_IP_POOL_REFS):
            for index_0 in range(len(self.properties.get(self.ALIAS_IP_POOL_REFS))):
                try:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        id=self.properties.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        fq_name_str=self.properties.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                obj_0.add_alias_ip_pool(ref_obj)

        try:
            obj_uuid = super(ContrailProject, self).resource_create(obj_0)
        except:
            raise Exception(_('project %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().project_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('project %s not found.') % self.name)

        if prop_diff.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(prop_diff.get(self.ALARM_ENABLE))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.QUOTA) is not None:
            obj_1 = vnc_api.QuotaType()
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS) is not None:
                obj_1.set_defaults(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_DEFAULTS))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP) is not None:
                obj_1.set_floating_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP) is not None:
                obj_1.set_instance_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_INSTANCE_IP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE) is not None:
                obj_1.set_virtual_machine_interface(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_MACHINE_INTERFACE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK) is not None:
                obj_1.set_virtual_network(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_NETWORK))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER) is not None:
                obj_1.set_virtual_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS) is not None:
                obj_1.set_virtual_DNS(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD) is not None:
                obj_1.set_virtual_DNS_record(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_DNS_RECORD))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER) is not None:
                obj_1.set_bgp_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_BGP_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM) is not None:
                obj_1.set_network_ipam(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_IPAM))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST) is not None:
                obj_1.set_access_control_list(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_ACCESS_CONTROL_LIST))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY) is not None:
                obj_1.set_network_policy(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_NETWORK_POLICY))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL) is not None:
                obj_1.set_floating_ip_pool(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_FLOATING_IP_POOL))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE) is not None:
                obj_1.set_service_template(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_TEMPLATE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE) is not None:
                obj_1.set_service_instance(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SERVICE_INSTANCE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER) is not None:
                obj_1.set_logical_router(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOGICAL_ROUTER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP) is not None:
                obj_1.set_security_group(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE) is not None:
                obj_1.set_security_group_rule(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SECURITY_GROUP_RULE))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SUBNET) is not None:
                obj_1.set_subnet(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_SUBNET))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG) is not None:
                obj_1.set_global_vrouter_config(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_GLOBAL_VROUTER_CONFIG))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL) is not None:
                obj_1.set_loadbalancer_pool(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_POOL))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER) is not None:
                obj_1.set_loadbalancer_member(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_MEMBER))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR) is not None:
                obj_1.set_loadbalancer_healthmonitor(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_LOADBALANCER_HEALTHMONITOR))
            if prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP) is not None:
                obj_1.set_virtual_ip(prop_diff.get(self.QUOTA, {}).get(self.QUOTA_VIRTUAL_IP))
            obj_0.set_quota(obj_1)

        # reference to namespace
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.NAMESPACE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NAMESPACE_REFS_DATA))):
                obj_1 = vnc_api.SubnetType()
                if prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX) is not None:
                    obj_1.set_ip_prefix(prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX))
                if prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN) is not None:
                    obj_1.set_ip_prefix_len(prop_diff.get(self.NAMESPACE_REFS_DATA, {})[index_0].get(self.NAMESPACE_REFS_DATA_IP_PREFIX_LEN))
                ref_data_list.append(obj_1)
        if self.NAMESPACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NAMESPACE_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().namespace_read(
                        id=prop_diff.get(self.NAMESPACE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().namespace_read(
                        fq_name_str=prop_diff.get(self.NAMESPACE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_namespace_list(ref_obj_list, ref_data_list)
            # End: reference to namespace_refs

        # reference to floating_ip_pool_refs
        ref_obj_list = []
        ref_data_list = []
        if self.FLOATING_IP_POOL_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.FLOATING_IP_POOL_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        id=prop_diff.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().floating_ip_pool_read(
                        fq_name_str=prop_diff.get(self.FLOATING_IP_POOL_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_floating_ip_pool_list(ref_obj_list)
            # End: reference to floating_ip_pool_refs

        # reference to alias_ip_pool_refs
        ref_obj_list = []
        ref_data_list = []
        if self.ALIAS_IP_POOL_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ALIAS_IP_POOL_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        id=prop_diff.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().alias_ip_pool_read(
                        fq_name_str=prop_diff.get(self.ALIAS_IP_POOL_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_alias_ip_pool_list(ref_obj_list)
            # End: reference to alias_ip_pool_refs

        try:
            self.vnc_lib().project_update(obj_0)
        except:
            raise Exception(_('project %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().project_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('project %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().project_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Project': ContrailProject,
    }
