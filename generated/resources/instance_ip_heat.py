
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


class ContrailInstanceIp(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, SERVICE_HEALTH_CHECK_IP, SECONDARY_IP_TRACKING_IP, SECONDARY_IP_TRACKING_IP_IP_PREFIX, SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN, INSTANCE_IP_ADDRESS, INSTANCE_IP_MODE, SUBNET_UUID, INSTANCE_IP_FAMILY, SERVICE_INSTANCE_IP, INSTANCE_IP_SECONDARY, PHYSICAL_ROUTER_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, VIRTUAL_NETWORK_REFS
    ) = (
        'name', 'fq_name', 'display_name', 'service_health_check_ip', 'secondary_ip_tracking_ip', 'secondary_ip_tracking_ip_ip_prefix', 'secondary_ip_tracking_ip_ip_prefix_len', 'instance_ip_address', 'instance_ip_mode', 'subnet_uuid', 'instance_ip_family', 'service_instance_ip', 'instance_ip_secondary', 'physical_router_refs', 'virtual_machine_interface_refs', 'virtual_network_refs'
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
        SERVICE_HEALTH_CHECK_IP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('SERVICE_HEALTH_CHECK_IP.'),
            update_allowed=True,
            required=False,
        ),
        SECONDARY_IP_TRACKING_IP: properties.Schema(
            properties.Schema.MAP,
            _('SECONDARY_IP_TRACKING_IP.'),
            update_allowed=True,
            required=False,
            schema={
                SECONDARY_IP_TRACKING_IP_IP_PREFIX: properties.Schema(
                    properties.Schema.STRING,
                    _('SECONDARY_IP_TRACKING_IP_IP_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        INSTANCE_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('INSTANCE_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        INSTANCE_IP_MODE: properties.Schema(
            properties.Schema.STRING,
            _('INSTANCE_IP_MODE.'),
            update_allowed=True,
            required=False,
        ),
        SUBNET_UUID: properties.Schema(
            properties.Schema.STRING,
            _('SUBNET_UUID.'),
            update_allowed=True,
            required=False,
        ),
        INSTANCE_IP_FAMILY: properties.Schema(
            properties.Schema.STRING,
            _('INSTANCE_IP_FAMILY.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_INSTANCE_IP: properties.Schema(
            properties.Schema.BOOLEAN,
            _('SERVICE_INSTANCE_IP.'),
            update_allowed=True,
            required=False,
        ),
        INSTANCE_IP_SECONDARY: properties.Schema(
            properties.Schema.BOOLEAN,
            _('INSTANCE_IP_SECONDARY.'),
            update_allowed=True,
            required=False,
        ),
        PHYSICAL_ROUTER_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PHYSICAL_ROUTER_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_NETWORK_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_NETWORK_REFS.'),
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
        SERVICE_HEALTH_CHECK_IP: attributes.Schema(
            _('SERVICE_HEALTH_CHECK_IP.'),
        ),
        SECONDARY_IP_TRACKING_IP: attributes.Schema(
            _('SECONDARY_IP_TRACKING_IP.'),
        ),
        INSTANCE_IP_ADDRESS: attributes.Schema(
            _('INSTANCE_IP_ADDRESS.'),
        ),
        INSTANCE_IP_MODE: attributes.Schema(
            _('INSTANCE_IP_MODE.'),
        ),
        SUBNET_UUID: attributes.Schema(
            _('SUBNET_UUID.'),
        ),
        INSTANCE_IP_FAMILY: attributes.Schema(
            _('INSTANCE_IP_FAMILY.'),
        ),
        SERVICE_INSTANCE_IP: attributes.Schema(
            _('SERVICE_INSTANCE_IP.'),
        ),
        INSTANCE_IP_SECONDARY: attributes.Schema(
            _('INSTANCE_IP_SECONDARY.'),
        ),
        PHYSICAL_ROUTER_REFS: attributes.Schema(
            _('PHYSICAL_ROUTER_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        VIRTUAL_NETWORK_REFS: attributes.Schema(
            _('VIRTUAL_NETWORK_REFS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        obj_0 = vnc_api.InstanceIp(name=self.properties[self.NAME])

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.SERVICE_HEALTH_CHECK_IP) is not None:
            obj_0.set_service_health_check_ip(self.properties.get(self.SERVICE_HEALTH_CHECK_IP))
        if self.properties.get(self.SECONDARY_IP_TRACKING_IP) is not None:
            obj_1 = vnc_api.SubnetType()
            if self.properties.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX) is not None:
                obj_1.set_ip_prefix(self.properties.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX))
            if self.properties.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN) is not None:
                obj_1.set_ip_prefix_len(self.properties.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN))
            obj_0.set_secondary_ip_tracking_ip(obj_1)
        if self.properties.get(self.INSTANCE_IP_ADDRESS) is not None:
            obj_0.set_instance_ip_address(self.properties.get(self.INSTANCE_IP_ADDRESS))
        if self.properties.get(self.INSTANCE_IP_MODE) is not None:
            obj_0.set_instance_ip_mode(self.properties.get(self.INSTANCE_IP_MODE))
        if self.properties.get(self.SUBNET_UUID) is not None:
            obj_0.set_subnet_uuid(self.properties.get(self.SUBNET_UUID))
        if self.properties.get(self.INSTANCE_IP_FAMILY) is not None:
            obj_0.set_instance_ip_family(self.properties.get(self.INSTANCE_IP_FAMILY))
        if self.properties.get(self.SERVICE_INSTANCE_IP) is not None:
            obj_0.set_service_instance_ip(self.properties.get(self.SERVICE_INSTANCE_IP))
        if self.properties.get(self.INSTANCE_IP_SECONDARY) is not None:
            obj_0.set_instance_ip_secondary(self.properties.get(self.INSTANCE_IP_SECONDARY))

        # reference to physical_router_refs
        if self.properties.get(self.PHYSICAL_ROUTER_REFS):
            for index_0 in range(len(self.properties.get(self.PHYSICAL_ROUTER_REFS))):
                try:
                    ref_obj = self.vnc_lib().physical_router_read(
                        id=self.properties.get(self.PHYSICAL_ROUTER_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().physical_router_read(
                        fq_name_str=self.properties.get(self.PHYSICAL_ROUTER_REFS)[index_0]
                    )
                obj_0.add_physical_router(ref_obj)

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

        try:
            obj_uuid = super(ContrailInstanceIp, self).resource_create(obj_0)
        except:
            raise Exception(_('instance-ip %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().instance_ip_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('instance-ip %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SERVICE_HEALTH_CHECK_IP) is not None:
            obj_0.set_service_health_check_ip(prop_diff.get(self.SERVICE_HEALTH_CHECK_IP))
        if prop_diff.get(self.SECONDARY_IP_TRACKING_IP) is not None:
            obj_1 = vnc_api.SubnetType()
            if prop_diff.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX) is not None:
                obj_1.set_ip_prefix(prop_diff.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX))
            if prop_diff.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN) is not None:
                obj_1.set_ip_prefix_len(prop_diff.get(self.SECONDARY_IP_TRACKING_IP, {}).get(self.SECONDARY_IP_TRACKING_IP_IP_PREFIX_LEN))
            obj_0.set_secondary_ip_tracking_ip(obj_1)
        if prop_diff.get(self.INSTANCE_IP_ADDRESS) is not None:
            obj_0.set_instance_ip_address(prop_diff.get(self.INSTANCE_IP_ADDRESS))
        if prop_diff.get(self.INSTANCE_IP_MODE) is not None:
            obj_0.set_instance_ip_mode(prop_diff.get(self.INSTANCE_IP_MODE))
        if prop_diff.get(self.SUBNET_UUID) is not None:
            obj_0.set_subnet_uuid(prop_diff.get(self.SUBNET_UUID))
        if prop_diff.get(self.INSTANCE_IP_FAMILY) is not None:
            obj_0.set_instance_ip_family(prop_diff.get(self.INSTANCE_IP_FAMILY))
        if prop_diff.get(self.SERVICE_INSTANCE_IP) is not None:
            obj_0.set_service_instance_ip(prop_diff.get(self.SERVICE_INSTANCE_IP))
        if prop_diff.get(self.INSTANCE_IP_SECONDARY) is not None:
            obj_0.set_instance_ip_secondary(prop_diff.get(self.INSTANCE_IP_SECONDARY))

        # reference to physical_router_refs
        ref_obj_list = []
        ref_data_list = []
        if self.PHYSICAL_ROUTER_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PHYSICAL_ROUTER_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().physical_router_read(
                        id=prop_diff.get(self.PHYSICAL_ROUTER_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().physical_router_read(
                        fq_name_str=prop_diff.get(self.PHYSICAL_ROUTER_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_physical_router_list(ref_obj_list)
            # End: reference to physical_router_refs

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

        try:
            self.vnc_lib().instance_ip_update(obj_0)
        except:
            raise Exception(_('instance-ip %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().instance_ip_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('instance_ip %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().instance_ip_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::InstanceIp': ContrailInstanceIp,
    }
