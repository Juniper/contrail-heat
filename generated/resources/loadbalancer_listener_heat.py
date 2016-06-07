
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


class ContrailLoadbalancerListener(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, LOADBALANCER_LISTENER_PROPERTIES, LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL, LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT, LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE, LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT, LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER, LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS, DISPLAY_NAME, LOADBALANCER_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'loadbalancer_listener_properties', 'loadbalancer_listener_properties_protocol', 'loadbalancer_listener_properties_protocol_port', 'loadbalancer_listener_properties_admin_state', 'loadbalancer_listener_properties_connection_limit', 'loadbalancer_listener_properties_default_tls_container', 'loadbalancer_listener_properties_sni_containers', 'display_name', 'loadbalancer_refs', 'project'
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
        LOADBALANCER_LISTENER_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_LISTENER_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'HTTP', u'HTTPS', u'TCP', u'TERMINATED_HTTPS']),
                    ],
                ),
                LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS: properties.Schema(
                    properties.Schema.LIST,
                    _('LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS.'),
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
        LOADBALANCER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('LOADBALANCER_REFS.'),
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
        LOADBALANCER_LISTENER_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_LISTENER_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        LOADBALANCER_REFS: attributes.Schema(
            _('LOADBALANCER_REFS.'),
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

        obj_0 = vnc_api.LoadbalancerListener(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerListenerType()
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL))
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT))
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT) is not None:
                obj_1.set_connection_limit(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT))
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER) is not None:
                obj_1.set_default_tls_container(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER))
            if self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS) is not None:
                for index_1 in range(len(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS))):
                    obj_1.add_sni_containers(self.properties.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS)[index_1])
            obj_0.set_loadbalancer_listener_properties(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        # reference to loadbalancer_refs
        if self.properties.get(self.LOADBALANCER_REFS):
            for index_0 in range(len(self.properties.get(self.LOADBALANCER_REFS))):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_read(
                        id=self.properties.get(self.LOADBALANCER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().loadbalancer_read(
                        fq_name_str=self.properties.get(self.LOADBALANCER_REFS)[index_0]
                    )
                obj_0.add_loadbalancer(ref_obj)

        try:
            obj_uuid = super(ContrailLoadbalancerListener, self).resource_create(obj_0)
        except:
            raise Exception(_('loadbalancer-listener %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_listener_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('loadbalancer-listener %s not found.') % self.name)

        if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerListenerType()
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL) is not None:
                obj_1.set_protocol(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL))
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_PROTOCOL_PORT))
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT) is not None:
                obj_1.set_connection_limit(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_CONNECTION_LIMIT))
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER) is not None:
                obj_1.set_default_tls_container(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_DEFAULT_TLS_CONTAINER))
            if prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS) is not None:
                for index_1 in range(len(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS))):
                    obj_1.add_sni_containers(prop_diff.get(self.LOADBALANCER_LISTENER_PROPERTIES, {}).get(self.LOADBALANCER_LISTENER_PROPERTIES_SNI_CONTAINERS)[index_1])
            obj_0.set_loadbalancer_listener_properties(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        # reference to loadbalancer_refs
        ref_obj_list = []
        ref_data_list = []
        if self.LOADBALANCER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.LOADBALANCER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().loadbalancer_read(
                        id=prop_diff.get(self.LOADBALANCER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().loadbalancer_read(
                        fq_name_str=prop_diff.get(self.LOADBALANCER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_loadbalancer_list(ref_obj_list)
            # End: reference to loadbalancer_refs

        try:
            self.vnc_lib().loadbalancer_listener_update(obj_0)
        except:
            raise Exception(_('loadbalancer-listener %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_listener_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_listener %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_listener_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerListener': ContrailLoadbalancerListener,
    }
