try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import netaddr
import uuid


# temp comment 
class HeatVnSubnet(contrail.ContrailResource):
    PROPERTIES = (
        NAME, NETWORK, IP_PREFIX, DEFAULT_GATEWAY, IPAM,
        ENABLE_DHCP, DNS_NAMESERVERS, ALLOCATION_POOLS,
        HOST_ROUTES,
    ) = (
        'name', 'network', 'ip_prefix', 'default_gateway', 'ipam',
        'enable_dhcp', 'dns_nameservers', 'allocation_pools',
        'host_routes',
    )

    _ALLOCATION_POOL_KEYS = (
        ALLOCATION_POOL_START, ALLOCATION_POOL_END,
    ) = (
        'start', 'end',
    )

    _HOST_ROUTES_KEYS = (
        ROUTE_DESTINATION, ROUTE_NEXTHOP,
    ) = (
        'destination', 'nexthop',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Network Subnet name'),
            update_allowed=True,
        ),
        NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('Network ID this subnet belongs to.'),
            required=True,
            update_allowed=False,
        ),
        IP_PREFIX: properties.Schema(
            properties.Schema.STRING,
            _('IP prefix of subnet.'),
            required=True,
        ),
        DEFAULT_GATEWAY: properties.Schema(
            properties.Schema.STRING,
            _('Default gateway of subnet.'),
            required=True,
            update_allowed=True,
        ),
        IPAM: properties.Schema(
            properties.Schema.STRING,
            _('IPAM this subnet uses.'),
            default=None,
            update_allowed=True,
        ),
        ENABLE_DHCP: properties.Schema(
            properties.Schema.STRING,
            _('Set to true if DHCP is enabled and false if DHCP is disabled.'),
            default="True",
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=True
        ),
        DNS_NAMESERVERS: properties.Schema(
            properties.Schema.LIST,
            _('A specified set of DNS name servers to be used.'),
            default=[],
            update_allowed=True
        ),
        ALLOCATION_POOLS: properties.Schema(
            properties.Schema.LIST,
            _('The start and end addresses for the allocation pools.'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ALLOCATION_POOL_START: properties.Schema(
                        properties.Schema.STRING,
                        required=True,
                        update_allowed=False
                    ),
                    ALLOCATION_POOL_END: properties.Schema(
                        properties.Schema.STRING,
                        required=True,
                        update_allowed=False
                    ),
                },
            ),
            update_allowed=False
        ),
        HOST_ROUTES: properties.Schema(
            properties.Schema.LIST,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    ROUTE_DESTINATION: properties.Schema(
                        properties.Schema.STRING,
                        required=True
                    ),
                    ROUTE_NEXTHOP: properties.Schema(
                        properties.Schema.STRING,
                        required=True
                    ),
                },
            )
        ),
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the Virtual Network.'),
        ),
        "network": attributes.Schema(
            _('Network ID this subnet belongs to.'),
        ),
        "ip_prefix": attributes.Schema(
            _('IP prefix of subnet.'),
        ),
        "default_gateway": attributes.Schema(
            _('Default gateway of subnet.'),
        ),
        "ipam": attributes.Schema(
            _('IPAM this subnet uses.'),
        ),
        "subnet_uuid": attributes.Schema(
            _('UUID of subnet.'),
        ),
        "subnet_name": attributes.Schema(
            _('Name of subnet.'),
        ),
        "enable_dhcp": attributes.Schema(
            _('True if DHCP is enabled for this subnet; False otherwise.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def _get_subnets(self, vn_obj, ipam):
        subnets = []
        for ref in vn_obj.get_network_ipam_refs() or []:
            if ref['to'] == ipam.get_fq_name():
                subnets = ref['attr'].get_ipam_subnets()
                break
        return subnets

    def _get_ipam(self):
        ipam = self.properties[self.IPAM]
        if ipam:
            try:
                ipam_obj = self.vnc_lib().network_ipam_read(id=ipam)
            except vnc_api.NoIdError:
                ipam_obj = self.vnc_lib().network_ipam_read(fq_name_str=ipam)
        else:
            tenant_id = self.stack.context.tenant_id
            project_obj = self.vnc_lib().project_read(
                id=str(uuid.UUID(tenant_id)))
            ipam_fq_name = project_obj.get_fq_name() + ['default-network-ipam']
            try:
                ipam_obj = self.vnc_lib().network_ipam_read(fq_name=ipam_fq_name)
            except vnc_api.NoIdError:
                ipam_obj = vnc_api.NetworkIpam('default-network-ipam',
                                               project_obj)
                ipam_id = self.vnc_lib().network_ipam_create(ipam_obj)
                ipam_obj = self.vnc_lib().network_ipam_read(id=ipam_id)
        return ipam_obj

    def _update_subnet(self, subnet, props):
        if props.get(self.ENABLE_DHCP) == "True":
            subnet.set_enable_dhcp(True)
        else:
            subnet.set_enable_dhcp(False)
        dns_servers = props.get(self.DNS_NAMESERVERS)
        if dns_servers:
            subnet.set_dns_nameservers(dns_servers)
        host_routes = props.get(self.HOST_ROUTES)
        if host_routes:
            subnet.set_host_routes(host_routes)

    def handle_create(self):
        try:
            vn_obj = self.vnc_lib().virtual_network_read(
                id=self.properties[self.NETWORK])
        except vnc_api.NoIdError:
            vn_obj = self.vnc_lib().virtual_network_read(
                fq_name_str=self.properties[self.NETWORK])

        net = netaddr.IPNetwork(self.properties[self.IP_PREFIX])
        if self.properties[self.ENABLE_DHCP] == "True":
            enable_dhcp = True
        else:
            enable_dhcp = False
        ipam = self._get_ipam()
        subnets = self._get_subnets(vn_obj, ipam)
        subnet_uuid = str(uuid.uuid4())
        subnet = vnc_api.IpamSubnetType(
            subnet_name=self.properties[self.NAME],
            subnet=vnc_api.SubnetType(str(net.ip), net.prefixlen),
            default_gateway=self.properties[self.DEFAULT_GATEWAY],
            allocation_pools=self.properties[self.ALLOCATION_POOLS],
            enable_dhcp=enable_dhcp,
            dns_nameservers=self.properties[self.DNS_NAMESERVERS],
            host_routes=self.properties[self.HOST_ROUTES],
            subnet_uuid=subnet_uuid)
        if subnets:
            subnets.append(subnet)
            vn_obj._pending_field_updates.add('network_ipam_refs')
        else:
            vn_obj.add_network_ipam(ipam, vnc_api.VnSubnetsType([subnet]))
        self.vnc_lib().virtual_network_update(vn_obj)
        self.resource_id_set(subnet_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        subnet_uuid = self.resource_id
        try:
            vn_obj = self.vnc_lib().virtual_network_read(
                id=self.properties[self.NETWORK])
        except vnc_api.NoIdError:
            vn_obj = self.vnc_lib().virtual_network_read(
                fq_name_str=self.properties[self.NETWORK])

        ipam = self._get_ipam()
        subnets = self._get_subnets(vn_obj, ipam)
        for subnet in subnets:
            if (subnet.get_subnet_uuid() and
                    subnet.get_subnet_uuid() == str(uuid.UUID(subnet_uuid))):
                self._update_subnet(subnet, prop_diff)
                vn_obj._pending_field_updates.add('network_ipam_refs')
                break
        self.vnc_lib().virtual_network_update(vn_obj)

    def handle_delete(self):
        subnet_uuid = self.resource_id
        if subnet_uuid:
            try:
                vn_obj = self.vnc_lib().virtual_network_read(
                    id=self.properties[self.NETWORK])
            except vnc_api.NoIdError:
                vn_obj = self.vnc_lib().virtual_network_read(
                    fq_name_str=self.properties[self.NETWORK])

            ipam = self._get_ipam()
            subnets = self._get_subnets(vn_obj, ipam)
            for subnet in subnets:
                if (subnet.get_subnet_uuid() and
                        subnet.get_subnet_uuid() == str(uuid.UUID(subnet_uuid))):
                    subnets.remove(subnet)
                    vn_obj._pending_field_updates.add('network_ipam_refs')
                    break
            if not subnets:
                vn_obj.del_network_ipam(ipam)
            self.vnc_lib().virtual_network_update(vn_obj)

    def _show_resource(self):
        dic = {}
        dic['network'] = self.properties[self.NETWORK]
        dic['ip_block'] = self.properties[self.IP_PREFIX]
        dic['gateway'] = self.properties[self.DEFAULT_GATEWAY]
        dic['subnet_uuid'] = self.resource_id
        dic['ipam'] = self.get_ipam().get_uuid()
        dic['name'] = self.properties[self.NAME]


def resource_mapping():
    return {
        'OS::Contrail::VnSubnet': HeatVnSubnet,
    }
