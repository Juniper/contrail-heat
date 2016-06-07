
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


class ContrailFloatingIpPool(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, FLOATING_IP_POOL_PREFIXES, FLOATING_IP_POOL_PREFIXES_SUBNET, FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX, FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN, VIRTUAL_NETWORK
    ) = (
        'name', 'fq_name', 'display_name', 'floating_ip_pool_prefixes', 'floating_ip_pool_prefixes_subnet', 'floating_ip_pool_prefixes_subnet_ip_prefix', 'floating_ip_pool_prefixes_subnet_ip_prefix_len', 'virtual_network'
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
        FLOATING_IP_POOL_PREFIXES: properties.Schema(
            properties.Schema.MAP,
            _('FLOATING_IP_POOL_PREFIXES.'),
            update_allowed=True,
            required=False,
            schema={
                FLOATING_IP_POOL_PREFIXES_SUBNET: properties.Schema(
                    properties.Schema.LIST,
                    _('FLOATING_IP_POOL_PREFIXES_SUBNET.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX: properties.Schema(
                                properties.Schema.STRING,
                                _('FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX.'),
                                update_allowed=True,
                                required=False,
                            ),
                            FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                properties.Schema.INTEGER,
                                _('FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_NETWORK.'),
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
        FLOATING_IP_POOL_PREFIXES: attributes.Schema(
            _('FLOATING_IP_POOL_PREFIXES.'),
        ),
        VIRTUAL_NETWORK: attributes.Schema(
            _('VIRTUAL_NETWORK.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_NETWORK):
            try:
                parent_obj = self.vnc_lib().virtual_network_read(id=self.properties.get(self.VIRTUAL_NETWORK))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_network_read(fq_name_str=self.properties.get(self.VIRTUAL_NETWORK))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.FloatingIpPool(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.FLOATING_IP_POOL_PREFIXES) is not None:
            obj_1 = vnc_api.FloatingIpPoolType()
            if self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET) is not None:
                for index_1 in range(len(self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX))
                    if self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(self.properties.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_floating_ip_pool_prefixes(obj_1)

        try:
            obj_uuid = super(ContrailFloatingIpPool, self).resource_create(obj_0)
        except:
            raise Exception(_('floating-ip-pool %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().floating_ip_pool_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('floating-ip-pool %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.FLOATING_IP_POOL_PREFIXES) is not None:
            obj_1 = vnc_api.FloatingIpPoolType()
            if prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET) is not None:
                for index_1 in range(len(prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET))):
                    obj_2 = vnc_api.SubnetType()
                    if prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX) is not None:
                        obj_2.set_ip_prefix(prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX))
                    if prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN) is not None:
                        obj_2.set_ip_prefix_len(prop_diff.get(self.FLOATING_IP_POOL_PREFIXES, {}).get(self.FLOATING_IP_POOL_PREFIXES_SUBNET, {})[index_1].get(self.FLOATING_IP_POOL_PREFIXES_SUBNET_IP_PREFIX_LEN))
                    obj_1.add_subnet(obj_2)
            obj_0.set_floating_ip_pool_prefixes(obj_1)

        try:
            self.vnc_lib().floating_ip_pool_update(obj_0)
        except:
            raise Exception(_('floating-ip-pool %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().floating_ip_pool_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('floating_ip_pool %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().floating_ip_pool_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::FloatingIpPool': ContrailFloatingIpPool,
    }
