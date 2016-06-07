
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


class ContrailDsaRule(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DSA_RULE_ENTRY, DSA_RULE_ENTRY_PUBLISHER, DSA_RULE_ENTRY_PUBLISHER_EP_TYPE, DSA_RULE_ENTRY_PUBLISHER_EP_ID, DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX, DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN, DSA_RULE_ENTRY_PUBLISHER_EP_VERSION, DSA_RULE_ENTRY_SUBSCRIBER, DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE, DSA_RULE_ENTRY_SUBSCRIBER_EP_ID, DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX, DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN, DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION, DISPLAY_NAME, DISCOVERY_SERVICE_ASSIGNMENT
    ) = (
        'name', 'fq_name', 'dsa_rule_entry', 'dsa_rule_entry_publisher', 'dsa_rule_entry_publisher_ep_type', 'dsa_rule_entry_publisher_ep_id', 'dsa_rule_entry_publisher_ep_prefix', 'dsa_rule_entry_publisher_ep_prefix_ip_prefix', 'dsa_rule_entry_publisher_ep_prefix_ip_prefix_len', 'dsa_rule_entry_publisher_ep_version', 'dsa_rule_entry_subscriber', 'dsa_rule_entry_subscriber_ep_type', 'dsa_rule_entry_subscriber_ep_id', 'dsa_rule_entry_subscriber_ep_prefix', 'dsa_rule_entry_subscriber_ep_prefix_ip_prefix', 'dsa_rule_entry_subscriber_ep_prefix_ip_prefix_len', 'dsa_rule_entry_subscriber_ep_version', 'display_name', 'discovery_service_assignment'
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
        DSA_RULE_ENTRY: properties.Schema(
            properties.Schema.MAP,
            _('DSA_RULE_ENTRY.'),
            update_allowed=True,
            required=False,
            schema={
                DSA_RULE_ENTRY_PUBLISHER: properties.Schema(
                    properties.Schema.MAP,
                    _('DSA_RULE_ENTRY_PUBLISHER.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        DSA_RULE_ENTRY_PUBLISHER_EP_TYPE: properties.Schema(
                            properties.Schema.STRING,
                            _('DSA_RULE_ENTRY_PUBLISHER_EP_TYPE.'),
                            update_allowed=True,
                            required=False,
                        ),
                        DSA_RULE_ENTRY_PUBLISHER_EP_ID: properties.Schema(
                            properties.Schema.STRING,
                            _('DSA_RULE_ENTRY_PUBLISHER_EP_ID.'),
                            update_allowed=True,
                            required=False,
                        ),
                        DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX: properties.Schema(
                            properties.Schema.MAP,
                            _('DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX.'),
                            update_allowed=True,
                            required=False,
                            schema={
                                DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX: properties.Schema(
                                    properties.Schema.STRING,
                                    _('DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        ),
                        DSA_RULE_ENTRY_PUBLISHER_EP_VERSION: properties.Schema(
                            properties.Schema.STRING,
                            _('DSA_RULE_ENTRY_PUBLISHER_EP_VERSION.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                DSA_RULE_ENTRY_SUBSCRIBER: properties.Schema(
                    properties.Schema.LIST,
                    _('DSA_RULE_ENTRY_SUBSCRIBER.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE: properties.Schema(
                                properties.Schema.STRING,
                                _('DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE.'),
                                update_allowed=True,
                                required=False,
                            ),
                            DSA_RULE_ENTRY_SUBSCRIBER_EP_ID: properties.Schema(
                                properties.Schema.STRING,
                                _('DSA_RULE_ENTRY_SUBSCRIBER_EP_ID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX: properties.Schema(
                                properties.Schema.MAP,
                                _('DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION: properties.Schema(
                                properties.Schema.STRING,
                                _('DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION.'),
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
        DISCOVERY_SERVICE_ASSIGNMENT: properties.Schema(
            properties.Schema.STRING,
            _('DISCOVERY_SERVICE_ASSIGNMENT.'),
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
        DSA_RULE_ENTRY: attributes.Schema(
            _('DSA_RULE_ENTRY.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        DISCOVERY_SERVICE_ASSIGNMENT: attributes.Schema(
            _('DISCOVERY_SERVICE_ASSIGNMENT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.DISCOVERY_SERVICE_ASSIGNMENT):
            try:
                parent_obj = self.vnc_lib().discovery_service_assignment_read(id=self.properties.get(self.DISCOVERY_SERVICE_ASSIGNMENT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().discovery_service_assignment_read(fq_name_str=self.properties.get(self.DISCOVERY_SERVICE_ASSIGNMENT))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.DsaRule(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DSA_RULE_ENTRY) is not None:
            obj_1 = vnc_api.DiscoveryServiceAssignmentType()
            if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER) is not None:
                obj_2 = vnc_api.DiscoveryPubSubEndPointType()
                if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_TYPE) is not None:
                    obj_2.set_ep_type(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_TYPE))
                if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_ID) is not None:
                    obj_2.set_ep_id(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_ID))
                if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX) is not None:
                    obj_3 = vnc_api.SubnetType()
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX) is not None:
                        obj_3.set_ip_prefix(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX))
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN) is not None:
                        obj_3.set_ip_prefix_len(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN))
                    obj_2.set_ep_prefix(obj_3)
                if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_VERSION) is not None:
                    obj_2.set_ep_version(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_VERSION))
                obj_1.set_publisher(obj_2)
            if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER) is not None:
                for index_1 in range(len(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER))):
                    obj_2 = vnc_api.DiscoveryPubSubEndPointType()
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE) is not None:
                        obj_2.set_ep_type(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE))
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_ID) is not None:
                        obj_2.set_ep_id(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_ID))
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX))
                        if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_ep_prefix(obj_3)
                    if self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION) is not None:
                        obj_2.set_ep_version(self.properties.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION))
                    obj_1.add_subscriber(obj_2)
            obj_0.set_dsa_rule_entry(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        try:
            obj_uuid = super(ContrailDsaRule, self).resource_create(obj_0)
        except:
            raise Exception(_('dsa-rule %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().dsa_rule_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('dsa-rule %s not found.') % self.name)

        if prop_diff.get(self.DSA_RULE_ENTRY) is not None:
            obj_1 = vnc_api.DiscoveryServiceAssignmentType()
            if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER) is not None:
                obj_2 = vnc_api.DiscoveryPubSubEndPointType()
                if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_TYPE) is not None:
                    obj_2.set_ep_type(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_TYPE))
                if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_ID) is not None:
                    obj_2.set_ep_id(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_ID))
                if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX) is not None:
                    obj_3 = vnc_api.SubnetType()
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX) is not None:
                        obj_3.set_ip_prefix(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX))
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN) is not None:
                        obj_3.set_ip_prefix_len(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_PREFIX_IP_PREFIX_LEN))
                    obj_2.set_ep_prefix(obj_3)
                if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_VERSION) is not None:
                    obj_2.set_ep_version(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_PUBLISHER, {}).get(self.DSA_RULE_ENTRY_PUBLISHER_EP_VERSION))
                obj_1.set_publisher(obj_2)
            if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER) is not None:
                for index_1 in range(len(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER))):
                    obj_2 = vnc_api.DiscoveryPubSubEndPointType()
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE) is not None:
                        obj_2.set_ep_type(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_TYPE))
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_ID) is not None:
                        obj_2.set_ep_id(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_ID))
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX))
                        if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_PREFIX_IP_PREFIX_LEN))
                        obj_2.set_ep_prefix(obj_3)
                    if prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION) is not None:
                        obj_2.set_ep_version(prop_diff.get(self.DSA_RULE_ENTRY, {}).get(self.DSA_RULE_ENTRY_SUBSCRIBER, {})[index_1].get(self.DSA_RULE_ENTRY_SUBSCRIBER_EP_VERSION))
                    obj_1.add_subscriber(obj_2)
            obj_0.set_dsa_rule_entry(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        try:
            self.vnc_lib().dsa_rule_update(obj_0)
        except:
            raise Exception(_('dsa-rule %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().dsa_rule_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('dsa_rule %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().dsa_rule_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::DsaRule': ContrailDsaRule,
    }
