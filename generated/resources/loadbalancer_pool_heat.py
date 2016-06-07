
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


class ContrailLoadbalancerPool(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, LOADBALANCER_POOL_PROVIDER, LOADBALANCER_POOL_PROPERTIES, LOADBALANCER_POOL_PROPERTIES_STATUS, LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION, LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE, LOADBALANCER_POOL_PROPERTIES_PROTOCOL, LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD, LOADBALANCER_POOL_PROPERTIES_SUBNET_ID, LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE, LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY, LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE, LOADBALANCER_LISTENER_REFS, LOADBALANCER_HEALTHMONITOR_REFS, SERVICE_INSTANCE_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, SERVICE_APPLIANCE_SET_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'loadbalancer_pool_provider', 'loadbalancer_pool_properties', 'loadbalancer_pool_properties_status', 'loadbalancer_pool_properties_status_description', 'loadbalancer_pool_properties_admin_state', 'loadbalancer_pool_properties_protocol', 'loadbalancer_pool_properties_loadbalancer_method', 'loadbalancer_pool_properties_subnet_id', 'loadbalancer_pool_properties_session_persistence', 'loadbalancer_pool_properties_persistence_cookie_name', 'loadbalancer_pool_custom_attributes', 'loadbalancer_pool_custom_attributes_key_value_pair', 'loadbalancer_pool_custom_attributes_key_value_pair_key', 'loadbalancer_pool_custom_attributes_key_value_pair_value', 'loadbalancer_listener_refs', 'loadbalancer_healthmonitor_refs', 'service_instance_refs', 'virtual_machine_interface_refs', 'service_appliance_set_refs', 'project'
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
        LOADBALANCER_POOL_PROVIDER: properties.Schema(
            properties.Schema.STRING,
            _('LOADBALANCER_POOL_PROVIDER.'),
            update_allowed=True,
            required=False,
        ),
        LOADBALANCER_POOL_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_POOL_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_POOL_PROPERTIES_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'HTTP', u'HTTPS', u'TCP', u'TERMINATED_HTTPS']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'ROUND_ROBIN', u'LEAST_CONNECTIONS', u'SOURCE_IP']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_SUBNET_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_SUBNET_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE']),
                    ],
                ),
                LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        LOADBALANCER_POOL_CUSTOM_ATTRIBUTES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        LOADBALANCER_LISTENER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_LISTENER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        LOADBALANCER_HEALTHMONITOR_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_HEALTHMONITOR_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_APPLIANCE_SET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_APPLIANCE_SET_REFS.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        LOADBALANCER_POOL_PROVIDER: attributes.Schema(
            _('LOADBALANCER_POOL_PROVIDER.'),
        ),
        LOADBALANCER_POOL_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_POOL_PROPERTIES.'),
        ),
        LOADBALANCER_POOL_CUSTOM_ATTRIBUTES: attributes.Schema(
            _('LOADBALANCER_POOL_CUSTOM_ATTRIBUTES.'),
        ),
        LOADBALANCER_LISTENER_REFS: attributes.Schema(
            _('LOADBALANCER_LISTENER_REFS.'),
        ),
        LOADBALANCER_HEALTHMONITOR_REFS: attributes.Schema(
            _('LOADBALANCER_HEALTHMONITOR_REFS.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        SERVICE_APPLIANCE_SET_REFS: attributes.Schema(
            _('SERVICE_APPLIANCE_SET_REFS.'),
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

        obj_0 = vnc_api.LoadbalancerPool(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.LOADBALANCER_POOL_PROVIDER) is not None:
            obj_0.set_loadbalancer_pool_provider(self.properties.get(self.LOADBALANCER_POOL_PROVIDER))
        if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerPoolType()
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS) is not None:
                obj_1.set_status(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD) is not None:
                obj_1.set_loadbalancer_method(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE) is not None:
                obj_1.set_session_persistence(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE))
            if self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(self.properties.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            obj_0.set_loadbalancer_pool_properties(obj_1)
        if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_loadbalancer_pool_custom_attributes(obj_1)

        # reference to loadbalancer_listener_refs
        if self.properties.get(self.LOADBALANCER_LISTENER_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_LISTENER_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        id=self.properties.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                obj_0.add_loadbalancer_listener(ref_obj)

        # reference to loadbalancer_healthmonitor_refs
        if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        id=self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                obj_0.add_loadbalancer_healthmonitor(ref_obj)

        # reference to service_instance_refs
        if self.properties.get(self.SERVICE_INSTANCE_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_INSTANCE_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_instance_read(
                        id=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_instance_read(
                        fq_name_str=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                obj_0.add_service_instance(ref_obj)

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

        # reference to service_appliance_set_refs
        if self.properties.get(self.SERVICE_APPLIANCE_SET_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_APPLIANCE_SET_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                obj_0.add_service_appliance_set(ref_obj)

        try:
            obj_uuid = super(ContrailLoadbalancerPool, self).resource_create(obj_0)
        except:
            raise Exception(_('loadbalancer-pool %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_pool_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('loadbalancer-pool %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.LOADBALANCER_POOL_PROVIDER) is not None:
            obj_0.set_loadbalancer_pool_provider(prop_diff.get(self.LOADBALANCER_POOL_PROVIDER))
        if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerPoolType()
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS) is not None:
                obj_1.set_status(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_STATUS_DESCRIPTION))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PROTOCOL))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD) is not None:
                obj_1.set_loadbalancer_method(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_LOADBALANCER_METHOD))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID) is not None:
                obj_1.set_subnet_id(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SUBNET_ID))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE) is not None:
                obj_1.set_session_persistence(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_SESSION_PERSISTENCE))
            if prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME) is not None:
                obj_1.set_persistence_cookie_name(prop_diff.get(self.LOADBALANCER_POOL_PROPERTIES, {}).get(self.LOADBALANCER_POOL_PROPERTIES_PERSISTENCE_COOKIE_NAME))
            obj_0.set_loadbalancer_pool_properties(obj_1)
        if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES, {}).get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR, {})[index_1].get(self.LOADBALANCER_POOL_CUSTOM_ATTRIBUTES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_loadbalancer_pool_custom_attributes(obj_1)

        # reference to loadbalancer_listener_refs
        ref_obj_list = []
        ref_data_list = []
        if self.LOADBALANCER_LISTENER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_LISTENER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        id=prop_diff.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().loadbalancer_listener_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_LISTENER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_loadbalancer_listener_list(ref_obj_list)
            # End: reference to loadbalancer_listener_refs

        # reference to loadbalancer_healthmonitor_refs
        ref_obj_list = []
        ref_data_list = []
        if self.LOADBALANCER_HEALTHMONITOR_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        id=prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().loadbalancer_healthmonitor_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_loadbalancer_healthmonitor_list(ref_obj_list)
            # End: reference to loadbalancer_healthmonitor_refs

        # reference to service_instance_refs
        ref_obj_list = []
        ref_data_list = []
        if self.SERVICE_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_INSTANCE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_instance_read(
                        id=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().service_instance_read(
                        fq_name_str=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_service_instance_list(ref_obj_list)
            # End: reference to service_instance_refs

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

        # reference to service_appliance_set_refs
        ref_obj_list = []
        ref_data_list = []
        if self.SERVICE_APPLIANCE_SET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_service_appliance_set_list(ref_obj_list)
            # End: reference to service_appliance_set_refs

        try:
            self.vnc_lib().loadbalancer_pool_update(obj_0)
        except:
            raise Exception(_('loadbalancer-pool %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_pool_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_pool %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_pool_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerPool': ContrailLoadbalancerPool,
    }
