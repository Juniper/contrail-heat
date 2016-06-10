
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


class ContrailPhysicalInterface(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, PHYSICAL_INTERFACE_REFS, PHYSICAL_ROUTER
    ) = (
        'name', 'fq_name', 'display_name', 'physical_interface_refs', 'physical_router'
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
        PHYSICAL_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER: properties.Schema(
            properties.Schema.STRING,
            _('PHYSICAL_ROUTER.'),
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
        PHYSICAL_INTERFACE_REFS: attributes.Schema(
            _('PHYSICAL_INTERFACE_REFS.'),
        ),
        PHYSICAL_ROUTER: attributes.Schema(
            _('PHYSICAL_ROUTER.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PHYSICAL_ROUTER):
            try:
                parent_obj = self.vnc_lib().physical_router_read(id=self.properties.get(self.PHYSICAL_ROUTER))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().physical_router_read(fq_name_str=self.properties.get(self.PHYSICAL_ROUTER))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.PhysicalInterface(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        # reference to physical_interface_refs
        if self.properties.get(self.PHYSICAL_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.PHYSICAL_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        id=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        fq_name_str=self.properties.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                obj_0.add_physical_interface(ref_obj)

        try:
            obj_uuid = super(ContrailPhysicalInterface, self).resource_create(obj_0)
        except:
            raise Exception(_('physical-interface %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().physical_interface_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('physical-interface %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        # reference to physical_interface_refs
        ref_obj_list = []
        ref_data_list = []
        if self.PHYSICAL_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        id=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().physical_interface_read(
                        fq_name_str=prop_diff.get(self.PHYSICAL_INTERFACE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_physical_interface_list(ref_obj_list)
            # End: reference to physical_interface_refs

        try:
            self.vnc_lib().physical_interface_update(obj_0)
        except:
            raise Exception(_('physical-interface %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().physical_interface_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('physical_interface %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().physical_interface_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::PhysicalInterface': ContrailPhysicalInterface,
    }
