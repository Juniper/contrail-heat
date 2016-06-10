
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


class ContrailServiceHealthCheck(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, SERVICE_HEALTH_CHECK_PROPERTIES, SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED, SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE, SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE, SERVICE_HEALTH_CHECK_PROPERTIES_DELAY, SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT, SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES, SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD, SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH, SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES, DISPLAY_NAME, SERVICE_INSTANCE_REFS, SERVICE_INSTANCE_REFS_DATA, SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE, PROJECT
    ) = (
        'name', 'fq_name', 'service_health_check_properties', 'service_health_check_properties_enabled', 'service_health_check_properties_health_check_type', 'service_health_check_properties_monitor_type', 'service_health_check_properties_delay', 'service_health_check_properties_timeout', 'service_health_check_properties_max_retries', 'service_health_check_properties_http_method', 'service_health_check_properties_url_path', 'service_health_check_properties_expected_codes', 'display_name', 'service_instance_refs', 'service_instance_refs_data', 'service_instance_refs_data_interface_type', 'project'
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
        SERVICE_HEALTH_CHECK_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_HEALTH_CHECK_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'link-local', u'end-to-end']),
                    ],
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'PING', u'HTTP']),
                    ],
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_DELAY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_DELAY.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES.'),
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
        SERVICE_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE.'),
                        update_allowed=True,
                        required=False,
                    ),
                }
            )
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
        SERVICE_HEALTH_CHECK_PROPERTIES: attributes.Schema(
            _('SERVICE_HEALTH_CHECK_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        SERVICE_INSTANCE_REFS_DATA: attributes.Schema(
            _('SERVICE_INSTANCE_REFS_DATA.'),
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

        obj_0 = vnc_api.ServiceHealthCheck(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceHealthCheckType()
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED) is not None:
                obj_1.set_enabled(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE) is not None:
                obj_1.set_health_check_type(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_DELAY))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH))
            if self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(self.properties.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES))
            obj_0.set_service_health_check_properties(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        # reference to service_instance_refs
        obj_1 = None
        if self.properties.get(self.SERVICE_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ServiceInterfaceTag()
                if self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(self.properties.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE))

                if self.properties.get(self.SERVICE_INSTANCE_REFS):
                    try:
                        ref_obj = self.vnc_lib().service_instance_read(
                            id=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().service_instance_read(
                            fq_name_str=self.properties.get(self.SERVICE_INSTANCE_REFS)[index_0]
                        )
                    obj_0.add_service_instance(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailServiceHealthCheck, self).resource_create(obj_0)
        except:
            raise Exception(_('service-health-check %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().service_health_check_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('service-health-check %s not found.') % self.name)

        if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceHealthCheckType()
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED) is not None:
                obj_1.set_enabled(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_ENABLED))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE) is not None:
                obj_1.set_health_check_type(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HEALTH_CHECK_TYPE))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MONITOR_TYPE))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_DELAY))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_TIMEOUT))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_MAX_RETRIES))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_HTTP_METHOD))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_URL_PATH))
            if prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(prop_diff.get(self.SERVICE_HEALTH_CHECK_PROPERTIES, {}).get(self.SERVICE_HEALTH_CHECK_PROPERTIES_EXPECTED_CODES))
            obj_0.set_service_health_check_properties(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        # reference to service_instance
        ref_obj_list = []
        ref_data_list = []
        if prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA))):
                obj_1 = vnc_api.ServiceInterfaceTag()
                if prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE) is not None:
                    obj_1.set_interface_type(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA, {})[index_0].get(self.SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE))
                ref_data_list.append(obj_1)
        if self.SERVICE_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_INSTANCE_REFS_DATA) or [])):
                try:
                    ref_obj = self.vnc_lib().service_instance_read(
                        id=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().service_instance_read(
                        fq_name_str=prop_diff.get(self.SERVICE_INSTANCE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_service_instance_list(ref_obj_list, ref_data_list)
            # End: reference to service_instance_refs

        try:
            self.vnc_lib().service_health_check_update(obj_0)
        except:
            raise Exception(_('service-health-check %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().service_health_check_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('service_health_check %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().service_health_check_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ServiceHealthCheck': ContrailServiceHealthCheck,
    }
