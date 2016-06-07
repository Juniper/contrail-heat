
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


class ContrailVirtualRouter(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, VIRTUAL_ROUTER_IP_ADDRESS, VIRTUAL_ROUTER_DPDK_ENABLED, VIRTUAL_ROUTER_TYPE, VIRTUAL_MACHINE_REFS, GLOBAL_SYSTEM_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'virtual_router_ip_address', 'virtual_router_dpdk_enabled', 'virtual_router_type', 'virtual_machine_refs', 'global_system_config'
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
        VIRTUAL_ROUTER_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_ROUTER_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_ROUTER_DPDK_ENABLED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('VIRTUAL_ROUTER_DPDK_ENABLED.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_ROUTER_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_ROUTER_TYPE.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
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
        VIRTUAL_ROUTER_IP_ADDRESS: attributes.Schema(
            _('VIRTUAL_ROUTER_IP_ADDRESS.'),
        ),
        VIRTUAL_ROUTER_DPDK_ENABLED: attributes.Schema(
            _('VIRTUAL_ROUTER_DPDK_ENABLED.'),
        ),
        VIRTUAL_ROUTER_TYPE: attributes.Schema(
            _('VIRTUAL_ROUTER_TYPE.'),
        ),
        VIRTUAL_MACHINE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_REFS.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_system_config_read(id=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.VirtualRouter(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.VIRTUAL_ROUTER_IP_ADDRESS) is not None:
            obj_0.set_virtual_router_ip_address(self.properties.get(self.VIRTUAL_ROUTER_IP_ADDRESS))
        if self.properties.get(self.VIRTUAL_ROUTER_DPDK_ENABLED) is not None:
            obj_0.set_virtual_router_dpdk_enabled(self.properties.get(self.VIRTUAL_ROUTER_DPDK_ENABLED))
        if self.properties.get(self.VIRTUAL_ROUTER_TYPE) is not None:
            obj_0.set_virtual_router_type(self.properties.get(self.VIRTUAL_ROUTER_TYPE))

        # reference to virtual_machine_refs
        if self.properties.get(self.VIRTUAL_MACHINE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                obj_0.add_virtual_machine(ref_obj)

        try:
            obj_uuid = super(ContrailVirtualRouter, self).resource_create(obj_0)
        except:
            raise Exception(_('virtual-router %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_router_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('virtual-router %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.VIRTUAL_ROUTER_IP_ADDRESS) is not None:
            obj_0.set_virtual_router_ip_address(prop_diff.get(self.VIRTUAL_ROUTER_IP_ADDRESS))
        if prop_diff.get(self.VIRTUAL_ROUTER_DPDK_ENABLED) is not None:
            obj_0.set_virtual_router_dpdk_enabled(prop_diff.get(self.VIRTUAL_ROUTER_DPDK_ENABLED))
        if prop_diff.get(self.VIRTUAL_ROUTER_TYPE) is not None:
            obj_0.set_virtual_router_type(prop_diff.get(self.VIRTUAL_ROUTER_TYPE))

        # reference to virtual_machine_refs
        ref_obj_list = []
        ref_data_list = []
        if self.VIRTUAL_MACHINE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_machine_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_virtual_machine_list(ref_obj_list)
            # End: reference to virtual_machine_refs

        try:
            self.vnc_lib().virtual_router_update(obj_0)
        except:
            raise Exception(_('virtual-router %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_router_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_router %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().virtual_router_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualRouter': ContrailVirtualRouter,
    }
