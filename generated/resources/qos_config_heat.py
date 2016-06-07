
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


class ContrailQosConfig(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, QOS_CONFIG_TYPE, VLAN_PRIORITY_ENTRIES, VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY, VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID, DISPLAY_NAME, MPLS_EXP_ENTRIES, MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY, MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID, DSCP_ENTRIES, DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY, DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID, TRUSTED, GLOBAL_QOS_CONFIG, PROJECT
    ) = (
        'name', 'fq_name', 'qos_config_type', 'vlan_priority_entries', 'vlan_priority_entries_qos_id_forwarding_class_pair', 'vlan_priority_entries_qos_id_forwarding_class_pair_key', 'vlan_priority_entries_qos_id_forwarding_class_pair_forwarding_class_id', 'display_name', 'mpls_exp_entries', 'mpls_exp_entries_qos_id_forwarding_class_pair', 'mpls_exp_entries_qos_id_forwarding_class_pair_key', 'mpls_exp_entries_qos_id_forwarding_class_pair_forwarding_class_id', 'dscp_entries', 'dscp_entries_qos_id_forwarding_class_pair', 'dscp_entries_qos_id_forwarding_class_pair_key', 'dscp_entries_qos_id_forwarding_class_pair_forwarding_class_id', 'trusted', 'global_qos_config', 'project'
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
        QOS_CONFIG_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('QOS_CONFIG_TYPE.'),
            update_allowed=True,
            required=False,
        ),
        VLAN_PRIORITY_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('VLAN_PRIORITY_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID: properties.Schema(
                                properties.Schema.INTEGER,
                                _('VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID.'),
                                update_allowed=True,
                                required=False,
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
        MPLS_EXP_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('MPLS_EXP_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY: properties.Schema(
                                properties.Schema.INTEGER,
                                _('MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID: properties.Schema(
                                properties.Schema.INTEGER,
                                _('MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        DSCP_ENTRIES: properties.Schema(
            properties.Schema.MAP,
            _('DSCP_ENTRIES.'),
            update_allowed=True,
            required=False,
            schema={
                DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY: properties.Schema(
                                properties.Schema.INTEGER,
                                _('DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID: properties.Schema(
                                properties.Schema.INTEGER,
                                _('DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        TRUSTED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('TRUSTED.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_QOS_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_QOS_CONFIG.'),
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
        QOS_CONFIG_TYPE: attributes.Schema(
            _('QOS_CONFIG_TYPE.'),
        ),
        VLAN_PRIORITY_ENTRIES: attributes.Schema(
            _('VLAN_PRIORITY_ENTRIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        MPLS_EXP_ENTRIES: attributes.Schema(
            _('MPLS_EXP_ENTRIES.'),
        ),
        DSCP_ENTRIES: attributes.Schema(
            _('DSCP_ENTRIES.'),
        ),
        TRUSTED: attributes.Schema(
            _('TRUSTED.'),
        ),
        GLOBAL_QOS_CONFIG: attributes.Schema(
            _('GLOBAL_QOS_CONFIG.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
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

        obj_0 = vnc_api.QosConfig(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.QOS_CONFIG_TYPE) is not None:
            obj_0.set_qos_config_type(self.properties.get(self.QOS_CONFIG_TYPE))
        if self.properties.get(self.VLAN_PRIORITY_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(self.properties.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_vlan_priority_entries(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.MPLS_EXP_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(self.properties.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_mpls_exp_entries(obj_1)
        if self.properties.get(self.DSCP_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(self.properties.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_dscp_entries(obj_1)
        if self.properties.get(self.TRUSTED) is not None:
            obj_0.set_trusted(self.properties.get(self.TRUSTED))

        try:
            obj_uuid = super(ContrailQosConfig, self).resource_create(obj_0)
        except:
            raise Exception(_('qos-config %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().qos_config_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('qos-config %s not found.') % self.name)

        if prop_diff.get(self.QOS_CONFIG_TYPE) is not None:
            obj_0.set_qos_config_type(prop_diff.get(self.QOS_CONFIG_TYPE))
        if prop_diff.get(self.VLAN_PRIORITY_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(prop_diff.get(self.VLAN_PRIORITY_ENTRIES, {}).get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.VLAN_PRIORITY_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_vlan_priority_entries(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.MPLS_EXP_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(prop_diff.get(self.MPLS_EXP_ENTRIES, {}).get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.MPLS_EXP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_mpls_exp_entries(obj_1)
        if prop_diff.get(self.DSCP_ENTRIES) is not None:
            obj_1 = vnc_api.QosIdForwardingClassPairs()
            if prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR))):
                    obj_2 = vnc_api.QosIdForwardingClassPair()
                    if prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_KEY))
                    if prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID) is not None:
                        obj_2.set_forwarding_class_id(prop_diff.get(self.DSCP_ENTRIES, {}).get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR, {})[index_1].get(self.DSCP_ENTRIES_QOS_ID_FORWARDING_CLASS_PAIR_FORWARDING_CLASS_ID))
                    obj_1.add_qos_id_forwarding_class_pair(obj_2)
            obj_0.set_dscp_entries(obj_1)
        if prop_diff.get(self.TRUSTED) is not None:
            obj_0.set_trusted(prop_diff.get(self.TRUSTED))

        try:
            self.vnc_lib().qos_config_update(obj_0)
        except:
            raise Exception(_('qos-config %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().qos_config_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('qos_config %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().qos_config_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::QosConfig': ContrailQosConfig,
    }
