
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


class ContrailLoadbalancerHealthmonitor(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, LOADBALANCER_HEALTHMONITOR_PROPERTIES, LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE, LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE, LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY, LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT, LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES, LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD, LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH, LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES, DISPLAY_NAME, PROJECT
    ) = (
        'name', 'fq_name', 'loadbalancer_healthmonitor_properties', 'loadbalancer_healthmonitor_properties_admin_state', 'loadbalancer_healthmonitor_properties_monitor_type', 'loadbalancer_healthmonitor_properties_delay', 'loadbalancer_healthmonitor_properties_timeout', 'loadbalancer_healthmonitor_properties_max_retries', 'loadbalancer_healthmonitor_properties_http_method', 'loadbalancer_healthmonitor_properties_url_path', 'loadbalancer_healthmonitor_properties_expected_codes', 'display_name', 'project'
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
        LOADBALANCER_HEALTHMONITOR_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_HEALTHMONITOR_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'PING', u'TCP', u'HTTP', u'HTTPS']),
                    ],
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES.'),
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
        LOADBALANCER_HEALTHMONITOR_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_HEALTHMONITOR_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
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

        obj_0 = vnc_api.LoadbalancerHealthmonitor(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerHealthmonitorType()
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH))
            if self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(self.properties.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES))
            obj_0.set_loadbalancer_healthmonitor_properties(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        try:
            obj_uuid = super(ContrailLoadbalancerHealthmonitor, self).resource_create(obj_0)
        except:
            raise Exception(_('loadbalancer-healthmonitor %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_healthmonitor_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('loadbalancer-healthmonitor %s not found.') % self.name)

        if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerHealthmonitorType()
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE) is not None:
                obj_1.set_monitor_type(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MONITOR_TYPE))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY) is not None:
                obj_1.set_delay(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_DELAY))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT) is not None:
                obj_1.set_timeout(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_TIMEOUT))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES) is not None:
                obj_1.set_max_retries(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_MAX_RETRIES))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD) is not None:
                obj_1.set_http_method(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_HTTP_METHOD))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH) is not None:
                obj_1.set_url_path(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_URL_PATH))
            if prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES) is not None:
                obj_1.set_expected_codes(prop_diff.get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES, {}).get(self.LOADBALANCER_HEALTHMONITOR_PROPERTIES_EXPECTED_CODES))
            obj_0.set_loadbalancer_healthmonitor_properties(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        try:
            self.vnc_lib().loadbalancer_healthmonitor_update(obj_0)
        except:
            raise Exception(_('loadbalancer-healthmonitor %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_healthmonitor_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_healthmonitor %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_healthmonitor_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerHealthmonitor': ContrailLoadbalancerHealthmonitor,
    }
