
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


class ContrailLogicalRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, CONFIGURED_ROUTE_TARGET_LIST, CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET, VIRTUAL_NETWORK_REFS, SERVICE_INSTANCE_REFS, ROUTE_TABLE_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, ROUTE_TARGET_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'configured_route_target_list', 'configured_route_target_list_route_target', 'virtual_network_refs', 'service_instance_refs', 'route_table_refs', 'virtual_machine_interface_refs', 'route_target_refs', 'project'
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
        CONFIGURED_ROUTE_TARGET_LIST: properties.Schema(
            properties.Schema.MAP,
            _('CONFIGURED_ROUTE_TARGET_LIST.'),
            update_allowed=True,
            required=False,
            schema={
                CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET: properties.Schema(
                    properties.Schema.LIST,
                    _('CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TABLE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TABLE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ROUTE_TARGET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTE_TARGET_REFS.'),
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
        CONFIGURED_ROUTE_TARGET_LIST: attributes.Schema(
            _('CONFIGURED_ROUTE_TARGET_LIST.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        ROUTE_TABLE_REFS: attributes.Schema(
            _('ROUTE_TABLE_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        ROUTE_TARGET_REFS: attributes.Schema(
            _('ROUTE_TARGET_REFS.'),
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

        obj_0 = vnc_api.LogicalRouter(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.CONFIGURED_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if self.properties.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(self.properties.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(self.properties.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_configured_route_target_list(obj_1)

        # reference to virtual_network_refs
        if self.properties.get(self.VIRTUAL_NETWORK_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_NETWORK_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                obj_0.add_virtual_network(ref_obj)

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

        # reference to route_table_refs
        if self.properties.get(self.ROUTE_TABLE_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTE_TABLE_REFS))):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=self.properties.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                obj_0.add_route_table(ref_obj)

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

        # reference to route_target_refs
        if self.properties.get(self.ROUTE_TARGET_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTE_TARGET_REFS))):
                try:
                    ref_obj = self.vnc_lib().route_target_read(
                        id=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().route_target_read(
                        fq_name_str=self.properties.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                obj_0.add_route_target(ref_obj)

        try:
            obj_uuid = super(ContrailLogicalRouter, self).resource_create(obj_0)
        except:
            raise Exception(_('logical-router %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().logical_router_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('logical-router %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.CONFIGURED_ROUTE_TARGET_LIST) is not None:
            obj_1 = vnc_api.RouteTargetList()
            if prop_diff.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET) is not None:
                for index_1 in range(len(prop_diff.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET))):
                    obj_1.add_route_target(prop_diff.get(self.CONFIGURED_ROUTE_TARGET_LIST, {}).get(self.CONFIGURED_ROUTE_TARGET_LIST_ROUTE_TARGET)[index_1])
            obj_0.set_configured_route_target_list(obj_1)

        # reference to virtual_network_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_NETWORK_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_NETWORK_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        id=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_network_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_NETWORK_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_network_list(ref_obj_list)
            # End: reference to virtual_network_refs

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

        # reference to route_table_refs
        ref_obj_list = []
        ref_data_list = []
        if self.ROUTE_TABLE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TABLE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().route_table_read(
                        id=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().route_table_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TABLE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_route_table_list(ref_obj_list)
            # End: reference to route_table_refs

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

        # reference to route_target_refs
        ref_obj_list = []
        ref_data_list = []
        if self.ROUTE_TARGET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTE_TARGET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().route_target_read(
                        id=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().route_target_read(
                        fq_name_str=prop_diff.get(self.ROUTE_TARGET_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_route_target_list(ref_obj_list)
            # End: reference to route_target_refs

        try:
            self.vnc_lib().logical_router_update(obj_0)
        except:
            raise Exception(_('logical-router %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().logical_router_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('logical_router %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().logical_router_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LogicalRouter': ContrailLogicalRouter,
    }
