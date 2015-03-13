from heat.common import exception
from heat.engine.resources.neutron import neutron
from heat.engine import properties

from neutronclient.common.exceptions import NeutronClientException
from neutronclient.neutron import v2_0 as neutronV20
from heat.openstack.common import log as logging

logger = logging.getLogger(__name__)


class AttachPolicy(neutron.NeutronResource):

    PROPERTIES = (
        NETWORK, POLICY,
    ) = (
        'network', 'policy',
    )

    properties_schema = {
        NETWORK: properties.Schema(
            properties.Schema.STRING,
            description=_('The network id or fq_name_string'),
            required=True),
        POLICY: properties.Schema(
            properties.Schema.STRING,
            description=_('policy name FQ name notation'),
            required=True),
    }

    def handle_create(self):
        if not ":" in self.properties.get(self.NETWORK):
            network = self.properties.get(self.NETWORK)
        else:
            network = self.properties.get(self.NETWORK).split(":")[2]
        network_id = neutronV20.find_resourceid_by_name_or_id(
            self.neutron(), 'network', network)

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
    return {
        'OS::Contrail::AttachPolicy': AttachPolicy,
    }
