
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


class ContrailLoadbalancer(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, LOADBALANCER_PROPERTIES, LOADBALANCER_PROPERTIES_STATUS, LOADBALANCER_PROPERTIES_PROVISIONING_STATUS, LOADBALANCER_PROPERTIES_OPERATING_STATUS, LOADBALANCER_PROPERTIES_VIP_SUBNET_ID, LOADBALANCER_PROPERTIES_VIP_ADDRESS, LOADBALANCER_PROPERTIES_ADMIN_STATE, LOADBALANCER_PROVIDER, DISPLAY_NAME, SERVICE_INSTANCE_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'loadbalancer_properties', 'loadbalancer_properties_status', 'loadbalancer_properties_provisioning_status', 'loadbalancer_properties_operating_status', 'loadbalancer_properties_vip_subnet_id', 'loadbalancer_properties_vip_address', 'loadbalancer_properties_admin_state', 'loadbalancer_provider', 'display_name', 'service_instance_refs', 'virtual_machine_interface_refs', 'project'
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
        LOADBALANCER_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_PROPERTIES_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_PROPERTIES_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_PROPERTIES_PROVISIONING_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_PROPERTIES_PROVISIONING_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_PROPERTIES_OPERATING_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_PROPERTIES_OPERATING_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_PROPERTIES_VIP_SUBNET_ID: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_PROPERTIES_VIP_SUBNET_ID.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_PROPERTIES_VIP_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_PROPERTIES_VIP_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        LOADBALANCER_PROVIDER: properties.Schema(
            properties.Schema.STRING,
            _('LOADBALANCER_PROVIDER.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_INSTANCE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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
        LOADBALANCER_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_PROPERTIES.'),
        ),
        LOADBALANCER_PROVIDER: attributes.Schema(
            _('LOADBALANCER_PROVIDER.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        SERVICE_INSTANCE_REFS: attributes.Schema(
            _('SERVICE_INSTANCE_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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

        obj_0 = vnc_api.Loadbalancer(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.LOADBALANCER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerType()
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_STATUS) is not None:
                obj_1.set_status(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_STATUS))
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_PROVISIONING_STATUS) is not None:
                obj_1.set_provisioning_status(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_PROVISIONING_STATUS))
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_OPERATING_STATUS) is not None:
                obj_1.set_operating_status(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_OPERATING_STATUS))
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_SUBNET_ID) is not None:
                obj_1.set_vip_subnet_id(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_SUBNET_ID))
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_ADDRESS) is not None:
                obj_1.set_vip_address(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_ADDRESS))
            if self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_ADMIN_STATE))
            obj_0.set_loadbalancer_properties(obj_1)
        if self.properties.get(self.LOADBALANCER_PROVIDER) is not None:
            obj_0.set_loadbalancer_provider(self.properties.get(self.LOADBALANCER_PROVIDER))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

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
            obj_uuid = super(ContrailLoadbalancer, self).resource_create(obj_0)
        except:
            raise Exception(_('loadbalancer %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('loadbalancer %s not found.') % self.name)

        if prop_diff.get(self.LOADBALANCER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerType()
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_STATUS) is not None:
                obj_1.set_status(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_STATUS))
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_PROVISIONING_STATUS) is not None:
                obj_1.set_provisioning_status(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_PROVISIONING_STATUS))
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_OPERATING_STATUS) is not None:
                obj_1.set_operating_status(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_OPERATING_STATUS))
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_SUBNET_ID) is not None:
                obj_1.set_vip_subnet_id(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_SUBNET_ID))
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_ADDRESS) is not None:
                obj_1.set_vip_address(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_VIP_ADDRESS))
            if prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_PROPERTIES, {}).get(self.LOADBALANCER_PROPERTIES_ADMIN_STATE))
            obj_0.set_loadbalancer_properties(obj_1)
        if prop_diff.get(self.LOADBALANCER_PROVIDER) is not None:
            obj_0.set_loadbalancer_provider(prop_diff.get(self.LOADBALANCER_PROVIDER))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

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
            self.vnc_lib().loadbalancer_update(obj_0)
        except:
            raise Exception(_('loadbalancer %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Loadbalancer': ContrailLoadbalancer,
    }
