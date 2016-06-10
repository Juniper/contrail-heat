
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


class ContrailRouteAggregate(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, AGGREGATE_ROUTE_ENTRIES, AGGREGATE_ROUTE_ENTRIES_ROUTE, DISPLAY_NAME, AGGREGATE_ROUTE_NEXTHOP, SERVICE_INSTANCE_REFS, SERVICE_INSTANCE_REFS_DATA, SERVICE_INSTANCE_REFS_DATA_INTERFACE_TYPE, ROUTING_INSTANCE_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'aggregate_route_entries', 'aggregate_route_entries_route', 'display_name', 'aggregate_route_nexthop', 'service_instance_refs', 'service_instance_refs_data', 'service_instance_refs_data_interface_type', 'routing_instance_refs', 'project'
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
        AGGREGATE_ROUTE_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('AGGREGATE_ROUTE_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                AGGREGATE_ROUTE_ENTRIES_ROUTE: properties.Schema(
                    properties.Schema.LIST,
                    _('AGGREGATE_ROUTE_ENTRIES_ROUTE.'),
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
        AGGREGATE_ROUTE_NEXTHOP: properties.Schema(
            properties.Schema.STRING,
            _('AGGREGATE_ROUTE_NEXTHOP.'),
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
        ROUTING_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('ROUTING_INSTANCE_REFS.'),
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
        AGGREGATE_ROUTE_ENTRIES: attributes.Schema(
            _('AGGREGATE_ROUTE_ENTRIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        AGGREGATE_ROUTE_NEXTHOP: attributes.Schema(
            _('AGGREGATE_ROUTE_NEXTHOP.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        SERVICE_INSTANCE_REFS_DATA: attributes.Schema(
            _('SERVICE_INSTANCE_REFS_DATA.'),
        ),
        ROUTING_INSTANCE_REFS: attributes.Schema(
            _('ROUTING_INSTANCE_REFS.'),
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

        obj_0 = vnc_api.RouteAggregate(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.AGGREGATE_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.RouteListType()
            if self.properties.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(self.properties.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE))):
                    obj_1.add_route(self.properties.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE)[index_1])
            obj_0.set_aggregate_route_entries(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.AGGREGATE_ROUTE_NEXTHOP) is not None:
            obj_0.set_aggregate_route_nexthop(self.properties.get(self.AGGREGATE_ROUTE_NEXTHOP))

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

        # reference to routing_instance_refs
        if self.properties.get(self.ROUTING_INSTANCE_REFS):
            for index_0 in range(len(self.properties.get(self.ROUTING_INSTANCE_REFS))):
                try:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        id=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        fq_name_str=self.properties.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                obj_0.add_routing_instance(ref_obj)

        try:
            obj_uuid = super(ContrailRouteAggregate, self).resource_create(obj_0)
        except:
            raise Exception(_('route-aggregate %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().route_aggregate_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('route-aggregate %s not found.') % self.name)

        if prop_diff.get(self.AGGREGATE_ROUTE_ENTRIES) is not None:
            obj_1 = vnc_api.RouteListType()
            if prop_diff.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE) is not None:
                for index_1 in range(len(prop_diff.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE))):
                    obj_1.add_route(prop_diff.get(self.AGGREGATE_ROUTE_ENTRIES, {}).get(self.AGGREGATE_ROUTE_ENTRIES_ROUTE)[index_1])
            obj_0.set_aggregate_route_entries(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.AGGREGATE_ROUTE_NEXTHOP) is not None:
            obj_0.set_aggregate_route_nexthop(prop_diff.get(self.AGGREGATE_ROUTE_NEXTHOP))

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

        # reference to routing_instance_refs
        ref_obj_list = []
        ref_data_list = []
        if self.ROUTING_INSTANCE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.ROUTING_INSTANCE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        id=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().routing_instance_read(
                        fq_name_str=prop_diff.get(self.ROUTING_INSTANCE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_routing_instance_list(ref_obj_list)
            # End: reference to routing_instance_refs

        try:
            self.vnc_lib().route_aggregate_update(obj_0)
        except:
            raise Exception(_('route-aggregate %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().route_aggregate_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('route_aggregate %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().route_aggregate_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::RouteAggregate': ContrailRouteAggregate,
    }
