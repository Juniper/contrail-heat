try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from novaclient import exceptions as nova_exceptions
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from heat.engine import scheduler
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource
import uuid

LOG = logging.getLogger(__name__)


class HeatServiceHealthCheck(ContrailResource):
    PROPERTIES = (
        NAME, SERVICE_INSTANCE, SERVICE_PORT_TAG, MONITOR_TYPE,
        DELAY, TIMEOUT, MAX_RETRIES, HTTP_METHOD, URL_PATH,
        EXPECTED_CODES, ENABLED
    ) = (
        'name', 'service_instance', 'service_port_tag', 'monitor_type',
        'delay', 'timeout', 'max_retries', 'http_method', 'url_path',
        'expected_codes', 'enabled'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Service health check name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_INSTANCE: properties.Schema(
            properties.Schema.STRING,
            _('Service instance name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_PORT_TAG: properties.Schema(
            properties.Schema.STRING,
            _('Service port tag.'),
            required=True,
            update_allowed=False
        ),
        MONITOR_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('Monitor type ping or http.'),
            required=True,
            constraints=[
                constraints.AllowedValues(['PING', 'HTTP']),
            ],
            update_allowed=True
        ),
        DELAY: properties.Schema(
            properties.Schema.INTEGER,
            _('Delay in seconds.'),
            required=True,
            update_allowed=True
        ),
        TIMEOUT: properties.Schema(
            properties.Schema.INTEGER,
            _('Timeout in seconds.'),
            required=True,
            update_allowed=True
        ),
        MAX_RETRIES: properties.Schema(
            properties.Schema.INTEGER,
            _('Max number of retries.'),
            required=True,
            update_allowed=True
        ),
        HTTP_METHOD: properties.Schema(
            properties.Schema.STRING,
            _('HTTP method to query.'),
            default=None,
            required=False,
            update_allowed=True
        ),
        URL_PATH: properties.Schema(
            properties.Schema.STRING,
            _('URL path to query.'),
            default=None,
            required=False,
            update_allowed=True
        ),
        EXPECTED_CODES: properties.Schema(
            properties.Schema.STRING,
            _('Expected codes for health check.'),
            default=None,
            required=False,
            update_allowed=True
        ),
        ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Health check enabled.'),
            required=True,
            update_allowed=True
        ),
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the Service Health Check.'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the Service Health Check.'),
        ),
        "service_instance": attributes.Schema(
            _('Service Instance for the Service Health Check.'),
        ),
        "service_port_tag": attributes.Schema(
            _('Tag for attaching to the corresponding port.'),
        ),
        "monitor_type": attributes.Schema(
            _('Monitor type of http or ping.'),
        ),
        "delay": attributes.Schema(
            _('Delay between health checks.'),
        ),
        "timeout": attributes.Schema(
            _('Timeout wait for response.'),
        ),
        "max_retries": attributes.Schema(
            _('Max retries for health check.'),
        ),
        "http_method": attributes.Schema(
            _('HTTP method for health check.'),
        ),
        "url_path": attributes.Schema(
            _('URL path for health HTTP health check.'),
        ),
        "expected_codes": attributes.Schema(
            _('Expected HTTP codes.'),
        ),
        "enabled": attributes.Schema(
            _('Health check enabled.'),
        ),
        "tenant_id": attributes.Schema(
            _('Tenant id of the Service Instance.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        try:
            si_obj = self.vnc_lib().service_instance_read(
                id=self.properties[self.SERVICE_INSTANCE])
        except vnc_api.NoIdError:
            si_name = project_obj.fq_name + \
                [self.properties[self.SERVICE_INSTANCE]]
            si_obj = self.vnc_lib().service_instance_read(fq_name=si_name)

        health_props = vnc_api.ServiceHealthCheckType(enabled=self.properties[self.ENABLED],
            monitor_type=self.properties[self.MONITOR_TYPE],
            delay=self.properties[self.DELAY], timeout=self.properties[self.TIMEOUT],
            max_retries=self.properties[self.MAX_RETRIES],
            http_method=self.properties[self.HTTP_METHOD],
            url_path=self.properties[self.URL_PATH],
            expected_codes=self.properties[self.EXPECTED_CODES])
        health_obj = vnc_api.ServiceHealthCheck(
            name=self.properties[self.NAME], parent_obj=project_obj,
            service_health_check_properties=health_props)
        health_obj.set_service_instance(si_obj,
            vnc_api.ServiceInterfaceTag(self.properties[self.SERVICE_PORT_TAG]))
        health_uuid = self.vnc_lib().service_health_check_create(health_obj)
        self.resource_id_set(health_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            health_obj = self.vnc_lib().service_health_check_read(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Service health check %s not found.") % self.name)
            raise
        except Exception as e:
            LOG.warn(_("Unknown error %s.") % str(e))
            raise

        health_props = vnc_api.ServiceHealthCheckType()
        if self.ENABLED in prop_diff:
            health_props.set_enabled(prop_diff.get(self.ENABLED))
        if self.MONITOR_TYPE in prop_diff:
            health_props.set_monitor_type(prop_diff.get(self.MONITOR_TYPE))
        if self.DELAY in prop_diff:
            health_props.set_delay(prop_diff.get(self.DELAY))
        if self.TIMEOUT in prop_diff:
            health_props.set_timeout(prop_diff.get(self.TIMEOUT))
        if self.MAX_RETRIES in prop_diff:
            health_props.set_max_retries(prop_diff.get(self.MAX_RETRIES))
        if self.HTTP_METHOD in prop_diff:
            health_props.set_http_method(prop_diff.get(self.HTTP_METHOD))
        if self.URL_PATH in prop_diff:
            health_props.set_url_path(prop_diff.get(self.URL_PATH))
        if self.EXPECTED_CODES in prop_diff:
            health_props.set_expected_codes(prop_diff.get(self.EXPECTED_CODES))

        health_obj.set_service_health_check_properties(health_props)
        self.vnc_lib().service_health_check_update(health_obj)

    def handle_delete(self):
        if not self.resource_id:
            return

        try:
            health_obj = self.vnc_lib().service_health_check_read(id=self.resource_id)
        except vnc_api.NoIdError:
            return

        # drop all references
        si_refs = health_obj.get_service_instance_refs()
        for si in si_refs or []:
            self._vnc_lib.ref_update('service-health-check', health_obj.uuid,
                'service-instance', si['uuid'], None, 'DELETE')
        vmi_back_refs = health_obj.get_virtual_machine_interface_back_refs()
        for vmi in vmi_back_refs or []:
            self._vnc_lib.ref_update('virtual-machine-interface', vmi['uuid'],
                'service-health-check', health_obj.uuid, None, 'DELETE')

        # delete health check
        try:
            self.vnc_lib().service_health_check_delete(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Health check %s not found.") % self.name)
        except Exception as e:
            LOG.warn(_("Unknown error %s.") % str(e))
            raise

    def _show_resource(self):
        health_obj = self.vnc_lib().service_health_check_read(id=self.resource_id)
        health_props = health_obj.get_service_health_check_properties()
        si_list = health_obj.get_service_instance_refs()
        dict = {}
        dict['name'] = health_obj.get_display_name()
        dict['fq_name'] = health_obj.get_fq_name_str()
        dict['tenant_id'] = health_obj.parent_uuid
        dict['enabled'] = health_props.get_enabled()
        dict['monitor_type'] = health_props.get_monitor_type()
        dict['delay'] = health_props.get_delay()
        dict['timeout'] = health_props.get_timeout()
        dict['max_retries'] = health_props.get_max_retries()
        dict['http_method'] = health_props.get_http_method()
        dict['url_path'] = health_props.get_url_path()
        dict['expected_codes'] = health_props.get_expected_codes()
        if si_list:
            dict['service_interface_tag'] = si_list[0]['attr'].get_interface_type()
            dict['service_instance'] = si_list[0]['to'][-1]
        return dict


def resource_mapping():
    return {
        'OS::Contrail::ServiceHealthCheck': HeatServiceHealthCheck,
    }
