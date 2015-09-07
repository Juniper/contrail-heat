try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.common import exception
from heat.engine import properties

from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource

try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging

logger = logging.getLogger(__name__)


class AttachPolicy(ContrailResource):

    PROPERTIES = (
        NETWORK, POLICY, SEQUENCE
    ) = (
        'network', 'policy', 'sequence'
    )

    _SEQUENCE_KEYS = (
        MAJOR, MINOR
    ) = (
        'major', 'minor'
    )

    properties_schema = {
        NETWORK: properties.Schema(
            properties.Schema.STRING,
            description=_('The network id or fq_name_string'),
            required=True),
        POLICY: properties.Schema(
            properties.Schema.STRING,
            description=_('The policy id or fq_name_string'),
            required=True),
        SEQUENCE: properties.Schema(
            properties.Schema.MAP,
            _('Order of the policy'),
            schema={
                MAJOR: properties.Schema(
                    properties.Schema.INTEGER,
                    _('Major number to define the order of this policy'),
                    default=0,
                ),
                MINOR: properties.Schema(
                    properties.Schema.INTEGER,
                    _('Minor number to define the order of this policy'),
                    default=0,
                )
            }
        ),
    }

    def handle_create(self):
        try:
            vn_obj = self.vnc_lib().virtual_network_read(
                id=self.properties.get(self.NETWORK))
        except vnc_api.NoIdError:
            vn_obj = self.vnc_lib().virtual_network_read(
                fq_name_str=self.properties.get(self.NETWORK))

        try:
            policy_obj = self.vnc_lib().network_policy_read(
                id=self.properties.get(self.POLICY))
        except vnc_api.NoIdError:
            policy_obj = self.vnc_lib().network_policy_read(
                fq_name_str=self.properties.get(self.POLICY))

        if self.properties[self.SEQUENCE] is None:
            major = 0
            minor = 0
        else:
            major = self.properties[self.SEQUENCE][self.MAJOR]
            minor = self.properties[self.SEQUENCE][self.MINOR]

        policy_order = vnc_api.VirtualNetworkPolicyType(vnc_api.SequenceType(major, minor))

        self.vnc_lib().ref_update('virtual-network', vn_obj.uuid,
                                 'network-policy', policy_obj.uuid, None, 'ADD', policy_order)

        self.resource_id_set('%s|%s' % (vn_obj.uuid, policy_obj.uuid))

    def handle_delete(self):
        if not self.resource_id:
            return
        (network_id, policy_id) = self.resource_id.split('|')
        try:
            self.vnc_lib().ref_update('virtual-network', network_id,
                                    'network-policy', policy_id, None, 'DELETE')
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_("Virtual Network %s already deleted.") % network_id)

def resource_mapping():
    return {
        'OS::Contrail::AttachPolicy': AttachPolicy,
    }
