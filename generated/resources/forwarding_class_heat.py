
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


class ContrailForwardingClass(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, FORWARDING_CLASS_VLAN_PRIORITY, FORWARDING_CLASS_MPLS_EXP, FORWARDING_CLASS_ID, FORWARDING_CLASS_DSCP, QOS_QUEUE_REFS, GLOBAL_QOS_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'forwarding_class_vlan_priority', 'forwarding_class_mpls_exp', 'forwarding_class_id', 'forwarding_class_dscp', 'qos_queue_refs', 'global_qos_config'
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
        FORWARDING_CLASS_VLAN_PRIORITY: properties.Schema(
            properties.Schema.INTEGER,
            _('FORWARDING_CLASS_VLAN_PRIORITY.'),
            update_allowed=True,
            required=False,
        ),
        FORWARDING_CLASS_MPLS_EXP: properties.Schema(
            properties.Schema.INTEGER,
            _('FORWARDING_CLASS_MPLS_EXP.'),
            update_allowed=True,
            required=False,
        ),
        FORWARDING_CLASS_ID: properties.Schema(
            properties.Schema.INTEGER,
            _('FORWARDING_CLASS_ID.'),
            update_allowed=True,
            required=False,
        ),
        FORWARDING_CLASS_DSCP: properties.Schema(
            properties.Schema.INTEGER,
            _('FORWARDING_CLASS_DSCP.'),
            update_allowed=True,
            required=False,
        ),
        QOS_QUEUE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('QOS_QUEUE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_QOS_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_QOS_CONFIG.'),
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
        FORWARDING_CLASS_VLAN_PRIORITY: attributes.Schema(
            _('FORWARDING_CLASS_VLAN_PRIORITY.'),
        ),
        FORWARDING_CLASS_MPLS_EXP: attributes.Schema(
            _('FORWARDING_CLASS_MPLS_EXP.'),
        ),
        FORWARDING_CLASS_ID: attributes.Schema(
            _('FORWARDING_CLASS_ID.'),
        ),
        FORWARDING_CLASS_DSCP: attributes.Schema(
            _('FORWARDING_CLASS_DSCP.'),
        ),
        QOS_QUEUE_REFS: attributes.Schema(
            _('QOS_QUEUE_REFS.'),
        ),
        GLOBAL_QOS_CONFIG: attributes.Schema(
            _('GLOBAL_QOS_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_QOS_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_qos_config_read(id=self.properties.get(self.GLOBAL_QOS_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_qos_config_read(fq_name_str=self.properties.get(self.GLOBAL_QOS_CONFIG))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.ForwardingClass(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.FORWARDING_CLASS_VLAN_PRIORITY) is not None:
            obj_0.set_forwarding_class_vlan_priority(self.properties.get(self.FORWARDING_CLASS_VLAN_PRIORITY))
        if self.properties.get(self.FORWARDING_CLASS_MPLS_EXP) is not None:
            obj_0.set_forwarding_class_mpls_exp(self.properties.get(self.FORWARDING_CLASS_MPLS_EXP))
        if self.properties.get(self.FORWARDING_CLASS_ID) is not None:
            obj_0.set_forwarding_class_id(self.properties.get(self.FORWARDING_CLASS_ID))
        if self.properties.get(self.FORWARDING_CLASS_DSCP) is not None:
            obj_0.set_forwarding_class_dscp(self.properties.get(self.FORWARDING_CLASS_DSCP))

        # reference to qos_queue_refs
        if self.properties.get(self.QOS_QUEUE_REFS):
            for index_0 in range(len(self.properties.get(self.QOS_QUEUE_REFS))):
                try:
                    ref_obj = self.vnc_lib().qos_queue_read(
                        id=self.properties.get(self.QOS_QUEUE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().qos_queue_read(
                        fq_name_str=self.properties.get(self.QOS_QUEUE_REFS)[index_0]
                    )
                obj_0.add_qos_queue(ref_obj)

        try:
            obj_uuid = super(ContrailForwardingClass, self).resource_create(obj_0)
        except:
            raise Exception(_('forwarding-class %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().forwarding_class_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('forwarding-class %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.FORWARDING_CLASS_VLAN_PRIORITY) is not None:
            obj_0.set_forwarding_class_vlan_priority(prop_diff.get(self.FORWARDING_CLASS_VLAN_PRIORITY))
        if prop_diff.get(self.FORWARDING_CLASS_MPLS_EXP) is not None:
            obj_0.set_forwarding_class_mpls_exp(prop_diff.get(self.FORWARDING_CLASS_MPLS_EXP))
        if prop_diff.get(self.FORWARDING_CLASS_ID) is not None:
            obj_0.set_forwarding_class_id(prop_diff.get(self.FORWARDING_CLASS_ID))
        if prop_diff.get(self.FORWARDING_CLASS_DSCP) is not None:
            obj_0.set_forwarding_class_dscp(prop_diff.get(self.FORWARDING_CLASS_DSCP))

        # reference to qos_queue_refs
        ref_obj_list = []
        ref_data_list = []
        if self.QOS_QUEUE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.QOS_QUEUE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().qos_queue_read(
                        id=prop_diff.get(self.QOS_QUEUE_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().qos_queue_read(
                        fq_name_str=prop_diff.get(self.QOS_QUEUE_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_qos_queue_list(ref_obj_list)
            # End: reference to qos_queue_refs

        try:
            self.vnc_lib().forwarding_class_update(obj_0)
        except:
            raise Exception(_('forwarding-class %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().forwarding_class_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('forwarding_class %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().forwarding_class_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ForwardingClass': ContrailForwardingClass,
    }
