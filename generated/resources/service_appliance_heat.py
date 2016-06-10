
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


class ContrailServiceAppliance(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, SERVICE_APPLIANCE_IP_ADDRESS, SERVICE_APPLIANCE_USER_CREDENTIALS, SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME, SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD, SERVICE_APPLIANCE_PROPERTIES, SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY, SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE, PHYSICAL_INTERFACE_REFS, PHYSICAL_INTERFACE_REFS_DATA, PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE, SERVICE_APPLIANCE_SET
    ) = (
        'name', 'fq_name', 'display_name', 'service_appliance_ip_address', 'service_appliance_user_credentials', 'service_appliance_user_credentials_username', 'service_appliance_user_credentials_password', 'service_appliance_properties', 'service_appliance_properties_key_value_pair', 'service_appliance_properties_key_value_pair_key', 'service_appliance_properties_key_value_pair_value', 'physical_interface_refs', 'physical_interface_refs_data', 'physical_interface_refs_data_interface_type', 'service_appliance_set'
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
        SERVICE_APPLIANCE_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('SERVICE_APPLIANCE_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_APPLIANCE_USER_CREDENTIALS: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_APPLIANCE_USER_CREDENTIALS.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        SERVICE_APPLIANCE_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_APPLIANCE_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        PHYSICAL_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_INTERFACE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_INTERFACE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
        ),
        SERVICE_APPLIANCE_SET: properties.Schema(
            properties.Schema.STRING,
            _('SERVICE_APPLIANCE_SET.'),
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
        SERVICE_APPLIANCE_IP_ADDRESS: attributes.Schema(
            _('SERVICE_APPLIANCE_IP_ADDRESS.'),
        ),
        SERVICE_APPLIANCE_USER_CREDENTIALS: attributes.Schema(
            _('SERVICE_APPLIANCE_USER_CREDENTIALS.'),
        ),
        SERVICE_APPLIANCE_PROPERTIES: attributes.Schema(
            _('SERVICE_APPLIANCE_PROPERTIES.'),
        ),
        PHYSICAL_INTERFACE_REFS: attributes.Schema(
            _('PHYSICAL_INTERFACE_REFS.'),
        ),
        PHYSICAL_INTERFACE_REFS_DATA: attributes.Schema(
            _('PHYSICAL_INTERFACE_REFS_DATA.'),
        ),
        SERVICE_APPLIANCE_SET: attributes.Schema(
            _('SERVICE_APPLIANCE_SET.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.SERVICE_APPLIANCE_SET):
            try:
                parent_obj = self.vnc_lib().service_appliance_set_read(id=self.properties.get(self.SERVICE_APPLIANCE_SET))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().service_appliance_set_read(fq_name_str=self.properties.get(self.SERVICE_APPLIANCE_SET))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.ServiceAppliance(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.SERVICE_APPLIANCE_IP_ADDRESS) is not None:
            obj_0.set_service_appliance_ip_address(self.properties.get(self.SERVICE_APPLIANCE_IP_ADDRESS))
        if self.properties.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if self.properties.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(self.properties.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME))
            if self.properties.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(self.properties.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD))
            obj_0.set_service_appliance_user_credentials(obj_1)
        if self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_appliance_properties(obj_1)

        # reference to physical_interface_refs
        obj_1 = None
        if self.properties.get(self.PHYSICAL_INTERFACE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.PHYSICAL_INTERFACE_REFS_DATA))):
                obj_1 = vnc_api.ServiceApplianceInterfaceType()
                if self.properties.get(self.PHYSICAL_INTERFACE_REFS_DATA, {})[index_0].get(self.PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(self.properties.get(self.PHYSICAL_INTERFACE_REFS_DATA, {})[index_0].get(self.PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE))

                if self.properties.get(self.PHYSICAL_INTERFACE_REFS):
                    try:
                        ref_obj = self.vnc_lib().physical_interface_read(
                            id=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().physical_interface_read(
                            fq_name_str=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                        )
                    obj_0.add_physical_interface(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailServiceAppliance, self).resource_create(obj_0)
        except:
            raise Exception(_('service-appliance %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().service_appliance_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('service-appliance %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SERVICE_APPLIANCE_IP_ADDRESS) is not None:
            obj_0.set_service_appliance_ip_address(prop_diff.get(self.SERVICE_APPLIANCE_IP_ADDRESS))
        if prop_diff.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS) is not None:
            obj_1 = vnc_api.UserCredentials()
            if prop_diff.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME) is not None:
                obj_1.set_username(prop_diff.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_USERNAME))
            if prop_diff.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD) is not None:
                obj_1.set_password(prop_diff.get(self.SERVICE_APPLIANCE_USER_CREDENTIALS, {}).get(self.SERVICE_APPLIANCE_USER_CREDENTIALS_PASSWORD))
            obj_0.set_service_appliance_user_credentials(obj_1)
        if prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.SERVICE_APPLIANCE_PROPERTIES, {}).get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR, {})[index_1].get(self.SERVICE_APPLIANCE_PROPERTIES_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_service_appliance_properties(obj_1)

        # reference to physical_interface
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.PHYSICAL_INTERFACE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_INTERFACE_REFS_DATA))):
                obj_1 = vnc_api.ServiceApplianceInterfaceType()
                if prop_diff.get(self.PHYSICAL_INTERFACE_REFS_DATA, {})[index_0].get(self.PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(prop_diff.get(self.PHYSICAL_INTERFACE_REFS_DATA, {})[index_0].get(self.PHYSICAL_INTERFACE_REFS_DATA_INTERFACE_TYPE))
                ref_data_list.append(obj_1)
        if self.PHYSICAL_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_INTERFACE_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        id=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        fq_name_str=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_physical_interface_list(ref_obj_list, ref_data_list)
            # End: reference to physical_interface_refs

        try:
            self.vnc_lib().service_appliance_update(obj_0)
        except:
            raise Exception(_('service-appliance %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().service_appliance_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('service_appliance %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().service_appliance_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ServiceAppliance': ContrailServiceAppliance,
    }
