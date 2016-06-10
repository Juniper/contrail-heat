
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


class ContrailServiceApplianceSet(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, SERVICE_APPLIANCE_DRIVER, SERVICE_APPLIANCE_SET_PROPERTIES, SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY, SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE, SERVICE_APPLIANCE_HA_MODE, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'service_appliance_driver', 'service_appliance_set_properties', 'service_appliance_set_properties_key_value_pair', 'service_appliance_set_properties_key_value_pair_key', 'service_appliance_set_properties_key_value_pair_value', 'service_appliance_ha_mode', 'global_system_config'
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
        SERVICE_APPLIANCE_DRIVER: properties.Schema(
            properties.Schema.STRING,
            _('SERVICE_APPLIANCE_DRIVER.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_APPLIANCE_SET_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_APPLIANCE_SET_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        SERVICE_APPLIANCE_HA_MODE: properties.Schema(
            properties.Schema.STRING,
            _('SERVICE_APPLIANCE_HA_MODE.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        SERVICE_APPLIANCE_DRIVER: attributes.Schema(
            _('SERVICE_APPLIANCE_DRIVER.'),
        ),
        SERVICE_APPLIANCE_SET_PROPERTIES: attributes.Schema(
            _('SERVICE_APPLIANCE_SET_PROPERTIES.'),
        ),
        SERVICE_APPLIANCE_HA_MODE: attributes.Schema(
            _('SERVICE_APPLIANCE_HA_MODE.'),
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

        obj_0 = vnc_api.ServiceApplianceSet(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.SERVICE_APPLIANCE_DRIVER) is not None:
            obj_0.set_service_appliance_driver(self.properties.get(self.SERVICE_APPLIANCE_DRIVER))
        if self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_appliance_set_properties(obj_1)
        if self.properties.get(self.SERVICE_APPLIANCE_HA_MODE) is not None:
            obj_0.set_service_appliance_ha_mode(self.properties.get(self.SERVICE_APPLIANCE_HA_MODE))

        try:
            obj_uuid = super(ContrailServiceApplianceSet, self).resource_create(obj_0)
        except:
            raise Exception(_('service-appliance-set %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().service_appliance_set_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('service-appliance-set %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SERVICE_APPLIANCE_DRIVER) is not None:
            obj_0.set_service_appliance_driver(prop_diff.get(self.SERVICE_APPLIANCE_DRIVER))
        if prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.SERVICE_APPLIANCE_SET_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_SET_PROPERTIES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_appliance_set_properties(obj_1)
        if prop_diff.get(self.SERVICE_APPLIANCE_HA_MODE) is not None:
            obj_0.set_service_appliance_ha_mode(prop_diff.get(self.SERVICE_APPLIANCE_HA_MODE))

        try:
            self.vnc_lib().service_appliance_set_update(obj_0)
        except:
            raise Exception(_('service-appliance-set %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().service_appliance_set_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('service_appliance_set %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().service_appliance_set_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ServiceApplianceSet': ContrailServiceApplianceSet,
    }
