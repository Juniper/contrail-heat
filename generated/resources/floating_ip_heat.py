
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


class ContrailFloatingIp(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, FLOATING_IP_ADDRESS_FAMILY, FLOATING_IP_IS_VIRTUAL_IP, FLOATING_IP_ADDRESS, DISPLAY_NAME, FLOATING_IP_FIXED_IP_ADDRESS, PROJECT_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, FLOATING_IP_POOL
    ) = (
        'name', 'fq_name', 'floating_ip_address_family', 'floating_ip_is_virtual_ip', 'floating_ip_address', 'display_name', 'floating_ip_fixed_ip_address', 'project_refs', 'virtual_machine_interface_refs', 'floating_ip_pool'
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
        FLOATING_IP_ADDRESS_FAMILY: properties.Schema(
            properties.Schema.STRING,
            _('FLOATING_IP_ADDRESS_FAMILY.'),
            update_allowed=True,
            required=False,
        ),
        FLOATING_IP_IS_VIRTUAL_IP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('FLOATING_IP_IS_VIRTUAL_IP.'),
            update_allowed=True,
            required=False,
        ),
        FLOATING_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('FLOATING_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        FLOATING_IP_FIXED_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('FLOATING_IP_FIXED_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PROJECT_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        FLOATING_IP_POOL: properties.Schema(
            properties.Schema.STRING,
            _('FLOATING_IP_POOL.'),
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
        FLOATING_IP_ADDRESS_FAMILY: attributes.Schema(
            _('FLOATING_IP_ADDRESS_FAMILY.'),
        ),
        FLOATING_IP_IS_VIRTUAL_IP: attributes.Schema(
            _('FLOATING_IP_IS_VIRTUAL_IP.'),
        ),
        FLOATING_IP_ADDRESS: attributes.Schema(
            _('FLOATING_IP_ADDRESS.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        FLOATING_IP_FIXED_IP_ADDRESS: attributes.Schema(
            _('FLOATING_IP_FIXED_IP_ADDRESS.'),
        ),
        PROJECT_REFS: attributes.Schema(
            _('PROJECT_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        FLOATING_IP_POOL: attributes.Schema(
            _('FLOATING_IP_POOL.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.FLOATING_IP_POOL):
            try:
                parent_obj = self.vnc_lib().floating_ip_pool_read(id=self.properties.get(self.FLOATING_IP_POOL))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().floating_ip_pool_read(fq_name_str=self.properties.get(self.FLOATING_IP_POOL))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.FloatingIp(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.FLOATING_IP_ADDRESS_FAMILY) is not None:
            obj_0.set_floating_ip_address_family(self.properties.get(self.FLOATING_IP_ADDRESS_FAMILY))
        if self.properties.get(self.FLOATING_IP_IS_VIRTUAL_IP) is not None:
            obj_0.set_floating_ip_is_virtual_ip(self.properties.get(self.FLOATING_IP_IS_VIRTUAL_IP))
        if self.properties.get(self.FLOATING_IP_ADDRESS) is not None:
            obj_0.set_floating_ip_address(self.properties.get(self.FLOATING_IP_ADDRESS))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.FLOATING_IP_FIXED_IP_ADDRESS) is not None:
            obj_0.set_floating_ip_fixed_ip_address(self.properties.get(self.FLOATING_IP_FIXED_IP_ADDRESS))

        # reference to project_refs
        if self.properties.get(self.PROJECT_REFS):
            for index_0 in range(len(self.properties.get(self.PROJECT_REFS))):
                try:
                    ref_obj = self.vnc_lib().project_read(
                        id=self.properties.get(self.PROJECT_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().project_read(
                        fq_name_str=self.properties.get(self.PROJECT_REFS)[index_0]
                    )
                obj_0.add_project(ref_obj)

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

        try:
            obj_uuid = super(ContrailFloatingIp, self).resource_create(obj_0)
        except:
            raise Exception(_('floating-ip %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().floating_ip_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('floating-ip %s not found.') % self.name)

        if prop_diff.get(self.FLOATING_IP_ADDRESS_FAMILY) is not None:
            obj_0.set_floating_ip_address_family(prop_diff.get(self.FLOATING_IP_ADDRESS_FAMILY))
        if prop_diff.get(self.FLOATING_IP_IS_VIRTUAL_IP) is not None:
            obj_0.set_floating_ip_is_virtual_ip(prop_diff.get(self.FLOATING_IP_IS_VIRTUAL_IP))
        if prop_diff.get(self.FLOATING_IP_ADDRESS) is not None:
            obj_0.set_floating_ip_address(prop_diff.get(self.FLOATING_IP_ADDRESS))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.FLOATING_IP_FIXED_IP_ADDRESS) is not None:
            obj_0.set_floating_ip_fixed_ip_address(prop_diff.get(self.FLOATING_IP_FIXED_IP_ADDRESS))

        # reference to project_refs
        ref_obj_list = []
        ref_data_list = []
        if self.PROJECT_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PROJECT_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().project_read(
                        id=prop_diff.get(self.PROJECT_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().project_read(
                        fq_name_str=prop_diff.get(self.PROJECT_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_project_list(ref_obj_list)
            # End: reference to project_refs

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

        try:
            self.vnc_lib().floating_ip_update(obj_0)
        except:
            raise Exception(_('floating-ip %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().floating_ip_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('floating_ip %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().floating_ip_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::FloatingIp': ContrailFloatingIp,
    }
