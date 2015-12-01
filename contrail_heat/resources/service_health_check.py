try:
    from heat.common.i18n import _
except ImportError:
    pass
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
        NAME, SERVICE_INSTANCE, SERVICE_PORT_TAG
    ) = (
        'name', 'service_instance', 'service_port_tag'
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
    }

    attributes_schema = {
        "name": _("The name of the Service Health Check."),
        "fq_name": _("The FQ name of the Service Health Check."),
        "service_instance": _("Service Instance for the Service Health Check."),
        "service_port_tag": _("Tag for attaching to the corresponding port."),
        "tenant_id": _("Tenant id of the Service Instance."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        try:
            si_obj = self.vnc_lib().service_instance_read(
                id=self.properties[self.SERVICE_INSTANCE])
        except vnc_api.NoIdError:
            si_obj = self.vnc_lib().service_instance_read(
                fq_name_str=self.properties[self.SERVICE_INSTANCE])

        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        health_obj = vnc_api.ServiceHealthCheck(
            name=self.properties[self.NAME], parent_obj=proj_obj)
        health_uuid = self.vnc_lib().service_health_check_create(health_obj)
        self.resource_id_set(health_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        pass

    def handle_delete(self):
        try:
            self.vnc_lib().service_health_check_delete(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Service Health Check %s not found.") % self.name)
        except:
            LOG.warn(_("Unknown error."))
            raise

    def _show_resource(self):
        health_obj = self.vnc_lib().service_health_check_read(id=self.resource_id)
        si_list = health_obj.get_service_instance_refs()
        dict = {}
        dict['name'] = pt_obj.get_display_name()
        dict['fq_name'] = pt_obj.get_fq_name_str()
        dict['tenant_id'] = si_obj.parent_uuid
        if si_list:
            dict['service_instance'] = ':'.join(si_list[0]['fq_name'])
        return dict


def resource_mapping():
    return {
        'OS::Contrail::ServiceHealthCheck': HeatServiceHealthCheck,
    }
