
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


class ContrailCustomerAttachment(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, ATTACHMENT_ADDRESS, DISPLAY_NAME, FLOATING_IP_REFS, VIRTUAL_MACHINE_INTERFACE_REFS
    ) = (
        'name', 'fq_name', 'attachment_address', 'display_name', 'floating_ip_refs', 'virtual_machine_interface_refs'
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
        ATTACHMENT_ADDRESS: properties.Schema(
            properties.Schema.MAP,
            _('ATTACHMENT_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        FLOATING_IP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('FLOATING_IP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
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
        ATTACHMENT_ADDRESS: attributes.Schema(
            _('ATTACHMENT_ADDRESS.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        FLOATING_IP_REFS: attributes.Schema(
            _('FLOATING_IP_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        obj_0 = vnc_api.CustomerAttachment(name=self.properties[self.NAME])

        if self.properties.get(self.ATTACHMENT_ADDRESS) is not None:
            obj_0.set_attachment_address(self.properties.get(self.ATTACHMENT_ADDRESS))
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        # reference to floating_ip_refs
        if self.properties.get(self.FLOATING_IP_REFS):
            for index_0 in range(len(self.properties.get(self.FLOATING_IP_REFS))):
                try:
                    ref_obj = self.vnc_lib().floating_ip_read(
                        id=self.properties.get(self.FLOATING_IP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().floating_ip_read(
                        fq_name_str=self.properties.get(self.FLOATING_IP_REFS)[index_0]
                    )
                obj_0.add_floating_ip(ref_obj)

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
            obj_uuid = super(ContrailCustomerAttachment, self).resource_create(obj_0)
        except:
            raise Exception(_('customer-attachment %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().customer_attachment_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('customer-attachment %s not found.') % self.name)

        if prop_diff.get(self.ATTACHMENT_ADDRESS) is not None:
            obj_0.set_attachment_address(prop_diff.get(self.ATTACHMENT_ADDRESS))
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        # reference to floating_ip_refs
        ref_obj_list = []
        ref_data_list = []
        if self.FLOATING_IP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.FLOATING_IP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().floating_ip_read(
                        id=prop_diff.get(self.FLOATING_IP_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().floating_ip_read(
                        fq_name_str=prop_diff.get(self.FLOATING_IP_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_floating_ip_list(ref_obj_list)
            # End: reference to floating_ip_refs

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
            self.vnc_lib().customer_attachment_update(obj_0)
        except:
            raise Exception(_('customer-attachment %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().customer_attachment_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('customer_attachment %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().customer_attachment_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::CustomerAttachment': ContrailCustomerAttachment,
    }
