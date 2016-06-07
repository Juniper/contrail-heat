
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


class ContrailRouteTable(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ROUTES, ROUTES_ROUTE, ROUTES_ROUTE_PREFIX, ROUTES_ROUTE_NEXT_HOP, ROUTES_ROUTE_NEXT_HOP_TYPE, ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, DISPLAY_NAME, PROJECT
    ) = (
        'name', 'fq_name', 'routes', 'routes_route', 'routes_route_prefix', 'routes_route_next_hop', 'routes_route_next_hop_type', 'routes_route_community_attributes', 'routes_route_community_attributes_community_attribute', 'display_name', 'project'
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
        ROUTES: properties.Schema(
            properties.Schema.MAP,
            _('ROUTES.'),
            update_allowed=True,
            required=False,
            schema={
                ROUTES_ROUTE: properties.Schema(
                    properties.Schema.LIST,
                    _('ROUTES_ROUTE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ROUTES_ROUTE_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('ROUTES_ROUTE_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                properties.Schema.STRING,
                                _('ROUTES_ROUTE_NEXT_HOP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                properties.Schema.STRING,
                                _('ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'service-instance', u'ip-address']),
                                ],
                            ),
                            ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                properties.Schema.MAP,
                                _('ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                        }
                    )
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
        ROUTES: attributes.Schema(
            _('ROUTES.'),
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

        obj_0 = vnc_api.RouteTable(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.ROUTES) is not None:
            obj_1 = vnc_api.RouteTableType()
            if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE) is not None:
                for index_1 in range(len(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE))):
                    obj_2 = vnc_api.RouteType()
                    if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_PREFIX))
                    if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP))
                    if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                        obj_2.set_next_hop_type(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP_TYPE))
                    if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                        obj_3 = vnc_api.CommunityAttributes()
                        if self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                            for index_3 in range(len(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                obj_3.add_community_attribute(self.properties.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_3])
                        obj_2.set_community_attributes(obj_3)
                    obj_1.add_route(obj_2)
            obj_0.set_routes(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        try:
            obj_uuid = super(ContrailRouteTable, self).resource_create(obj_0)
        except:
            raise Exception(_('route-table %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().route_table_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('route-table %s not found.') % self.name)

        if prop_diff.get(self.ROUTES) is not None:
            obj_1 = vnc_api.RouteTableType()
            if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE) is not None:
                for index_1 in range(len(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE))):
                    obj_2 = vnc_api.RouteType()
                    if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_PREFIX) is not None:
                        obj_2.set_prefix(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_PREFIX))
                    if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP) is not None:
                        obj_2.set_next_hop(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP))
                    if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                        obj_2.set_next_hop_type(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_NEXT_HOP_TYPE))
                    if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                        obj_3 = vnc_api.CommunityAttributes()
                        if prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                            for index_3 in range(len(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                obj_3.add_community_attribute(prop_diff.get(self.ROUTES, {}).get(self.ROUTES_ROUTE, {})[index_1].get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_3])
                        obj_2.set_community_attributes(obj_3)
                    obj_1.add_route(obj_2)
            obj_0.set_routes(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        try:
            self.vnc_lib().route_table_update(obj_0)
        except:
            raise Exception(_('route-table %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().route_table_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('route_table %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().route_table_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::RouteTable': ContrailRouteTable,
    }
