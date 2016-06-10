
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


class ContrailGlobalSystemConfig(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, CONFIG_VERSION, USER_DEFINED_COUNTER, USER_DEFINED_COUNTER_COUNTER, USER_DEFINED_COUNTER_COUNTER_NAME, USER_DEFINED_COUNTER_COUNTER_PATTERN, ALARM_ENABLE, DISPLAY_NAME, PLUGIN_TUNING, PLUGIN_TUNING_PLUGIN_PROPERTY, PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY, PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE, IBGP_AUTO_MESH, IP_FABRIC_SUBNETS, IP_FABRIC_SUBNETS_SUBNET, IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX, IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN, AUTONOMOUS_SYSTEM, BGP_ROUTER_REFS
    ) = (
        'name', 'fq_name', 'config_version', 'user_defined_counter', 'user_defined_counter_counter', 'user_defined_counter_counter_name', 'user_defined_counter_counter_pattern', 'alarm_enable', 'display_name', 'plugin_tuning', 'plugin_tuning_plugin_property', 'plugin_tuning_plugin_property_property', 'plugin_tuning_plugin_property_value', 'ibgp_auto_mesh', 'ip_fabric_subnets', 'ip_fabric_subnets_subnet', 'ip_fabric_subnets_subnet_ip_prefix', 'ip_fabric_subnets_subnet_ip_prefix_len', 'autonomous_system', 'bgp_router_refs'
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
        CONFIG_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('CONFIG_VERSION.'),
            update_allowed=True,
            required=False,
        ),
        USER_DEFINED_COUNTER: properties.Schema(
            properties.Schema.MAP,
            _('USER_DEFINED_COUNTER.'),
            update_allowed=True,
            required=False,
            schema={
                USER_DEFINED_COUNTER_COUNTER: properties.Schema(
                    properties.Schema.LIST,
                    _('USER_DEFINED_COUNTER_COUNTER.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            USER_DEFINED_COUNTER_COUNTER_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('USER_DEFINED_COUNTER_COUNTER_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            USER_DEFINED_COUNTER_COUNTER_PATTERN: properties.Schema(
                                properties.Schema.STRING,
                                _('USER_DEFINED_COUNTER_COUNTER_PATTERN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
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
        PLUGIN_TUNING: properties.Schema(
            properties.Schema.MAP,
            _('PLUGIN_TUNING.'),
            update_allowed=True,
            required=False,
            schema={
                PLUGIN_TUNING_PLUGIN_PROPERTY: properties.Schema(
                    properties.Schema.LIST,
                    _('PLUGIN_TUNING_PLUGIN_PROPERTY.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY: properties.Schema(
                                properties.Schema.STRING,
                                _('PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        IBGP_AUTO_MESH: properties.Schema(
            properties.Schema.BOOLEAN,
            _('IBGP_AUTO_MESH.'),
            update_allowed=True,
            required=False,
        ),
        IP_FABRIC_SUBNETS: properties.Schema(
            properties.Schema.MAP,
            _('IP_FABRIC_SUBNETS.'),
            update_allowed=True,
            required=False,
            schema={
                IP_FABRIC_SUBNETS_SUBNET: properties.Schema(
                    properties.Schema.LIST,
                    _('IP_FABRIC_SUBNETS_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                properties.Schema.INTEGER,
                                _('IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
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
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        CONFIG_VERSION: attributes.Schema(
            _('CONFIG_VERSION.'),
        ),
        USER_DEFINED_COUNTER: attributes.Schema(
            _('USER_DEFINED_COUNTER.'),
        ),
        ALARM_ENABLE: attributes.Schema(
            _('ALARM_ENABLE.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PLUGIN_TUNING: attributes.Schema(
            _('PLUGIN_TUNING.'),
        ),
        IBGP_AUTO_MESH: attributes.Schema(
            _('IBGP_AUTO_MESH.'),
        ),
        IP_FABRIC_SUBNETS: attributes.Schema(
            _('IP_FABRIC_SUBNETS.'),
        ),
        AUTONOMOUS_SYSTEM: attributes.Schema(
            _('AUTONOMOUS_SYSTEM.'),
        ),
        BGP_ROUTER_REFS: attributes.Schema(
            _('BGP_ROUTER_REFS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        obj_0 = vnc_api.GlobalSystemConfig(name=self.properties[self.NAME])

        if self.properties.get(self.CONFIG_VERSION) is not None:
            obj_0.set_config_version(self.properties.get(self.CONFIG_VERSION))
        if self.properties.get(self.USER_DEFINED_COUNTER) is not None:
            obj_1 = vnc_api.UserDefinedCounterList()
            if self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER) is not None:
                for index_1 in range(len(self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER))):
                    obj_2 = vnc_api.UserDefinedCounter()
                    if self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_NAME) is not None:
                        obj_2.set_name(self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_NAME))
                    if self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_PATTERN) is not None:
                        obj_2.set_pattern(self.properties.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_PATTERN))
                    obj_1.add_counter(obj_2)
            obj_0.set_user_defined_counter(obj_1)
        if self.properties.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(self.properties.get(self.ALARM_ENABLE))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PLUGIN_TUNING) is not None:
            obj_1 = vnc_api.PluginProperties()
            if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY) is not None:
                for index_1 in range(len(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY))):
                    obj_2 = vnc_api.PluginProperty()
                    if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY) is not None:
                        obj_2.set_property(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY))
                    if self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE))
                    obj_1.add_plugin_property(obj_2)
            obj_0.set_plugin_tuning(obj_1)
        if self.properties.get(self.IBGP_AUTO_MESH) is not None:
            obj_0.set_ibgp_auto_mesh(self.properties.get(self.IBGP_AUTO_MESH))
        if self.properties.get(self.IP_FABRIC_SUBNETS) is not None:
            obj_1 = vnc_api.SubnetListType()
            if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET) is not None:
                for index_1 in range(len(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX))
                    if self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(self.properties.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_ip_fabric_subnets(obj_1)
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

        try:
            obj_uuid = super(ContrailGlobalSystemConfig, self).resource_create(obj_0)
        except:
            raise Exception(_('global-system-config %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().global_system_config_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('global-system-config %s not found.') % self.name)

        if prop_diff.get(self.CONFIG_VERSION) is not None:
            obj_0.set_config_version(prop_diff.get(self.CONFIG_VERSION))
        if prop_diff.get(self.USER_DEFINED_COUNTER) is not None:
            obj_1 = vnc_api.UserDefinedCounterList()
            if prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER) is not None:
                for index_1 in range(len(prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER))):
                    obj_2 = vnc_api.UserDefinedCounter()
                    if prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_NAME) is not None:
                        obj_2.set_name(prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_NAME))
                    if prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_PATTERN) is not None:
                        obj_2.set_pattern(prop_diff.get(self.USER_DEFINED_COUNTER, {}).get(self.USER_DEFINED_COUNTER_COUNTER, {})[index_1].get(self.USER_DEFINED_COUNTER_COUNTER_PATTERN))
                    obj_1.add_counter(obj_2)
            obj_0.set_user_defined_counter(obj_1)
        if prop_diff.get(self.ALARM_ENABLE) is not None:
            obj_0.set_alarm_enable(prop_diff.get(self.ALARM_ENABLE))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.PLUGIN_TUNING) is not None:
            obj_1 = vnc_api.PluginProperties()
            if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY) is not None:
                for index_1 in range(len(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY))):
                    obj_2 = vnc_api.PluginProperty()
                    if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY) is not None:
                        obj_2.set_property(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_PROPERTY))
                    if prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.PLUGIN_TUNING, {}).get(self.PLUGIN_TUNING_PLUGIN_PROPERTY, {})[index_1].get(self.PLUGIN_TUNING_PLUGIN_PROPERTY_VALUE))
                    obj_1.add_plugin_property(obj_2)
            obj_0.set_plugin_tuning(obj_1)
        if prop_diff.get(self.IBGP_AUTO_MESH) is not None:
            obj_0.set_ibgp_auto_mesh(prop_diff.get(self.IBGP_AUTO_MESH))
        if prop_diff.get(self.IP_FABRIC_SUBNETS) is not None:
            obj_1 = vnc_api.SubnetListType()
            if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET) is not None:
                for index_1 in range(len(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX))
                    if prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(prop_diff.get(self.IP_FABRIC_SUBNETS, {}).get(self.IP_FABRIC_SUBNETS_SUBNET, {})[index_1].get(self.IP_FABRIC_SUBNETS_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_ip_fabric_subnets(obj_1)
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

        try:
            self.vnc_lib().global_system_config_update(obj_0)
        except:
            raise Exception(_('global-system-config %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().global_system_config_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('global_system_config %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().global_system_config_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::GlobalSystemConfig': ContrailGlobalSystemConfig,
    }
