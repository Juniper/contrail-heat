from heat.common import exception
from heat.engine import clients
from heat.engine.resources.neutron import neutron
from heat.engine import properties

if clients.neutronclient is not None:
    from neutronclient.common.exceptions import NeutronClientException

from heat.openstack.common import log as logging

logger = logging.getLogger(__name__)


class AttachPolicy(neutron.NeutronResource):

    PROPERTIES = (
        NETWORK_ID, POLICY,
    ) = (
        'network_id', 'policy',
    )

    properties_schema = {
        NETWORK_ID: properties.Schema(
            properties.Schema.STRING,
            description=_('The network id'),
            required=True),
        POLICY: properties.Schema(
            properties.Schema.STRING,
            description=_('policy name FQ name notation'),
            required=True),
    }

    def handle_create(self):
        network_id = self.properties.get(self.NETWORK_ID)
        policies = self.neutron().show_network(network_id).get('network').get('contrail:policys')
        if not policies:
            policies = []
        policies.append(self.properties.get(self.POLICY).split(':'))
        self.neutron().update_network(network_id, {'network':
                                     {'contrail:policys': policies}})
        self.resource_id_set(
            '%s|%s' % (network_id, self.properties.get(self.POLICY)))

    def handle_delete(self):
        if not self.resource_id:
            return
        (network_id, policy) = self.resource_id.split('|')
        try:
            policies = self.neutron().show_network(
                network_id).get('network').get('contrail:policys', [])
            try:
                policies.remove(policy.split(':'))
            except ValueError:
                return
            self.neutron().update_network(network_id, {'network':
                                         {'contrail:policys': policies}})
        except NeutronClientException as ex:
            if ex.status_code != 404:
                raise ex


def resource_mapping():
    if clients.neutronclient is None:
        return {}

    return {
        'OS::Contrail::AttachPolicy': AttachPolicy,
    }
