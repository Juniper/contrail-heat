from heat.engine import properties
from vnc_api import vnc_api
from contrail_heat.resources import contrail
import netaddr
import uuid


class HeatVnSubnet(contrail.ContrailResource):
    PROPERTIES = (
        NAME, NETWORK_ID, IP_PREFIX, DEFAULT_GATEWAY, IPAM
    ) = (
        'name', 'network_id', 'ip_prefix', 'default_gateway', 'ipam',
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Virtual Network Subnet name'),
            update_allowed=True,
        ),
        NETWORK_ID: properties.Schema(
            properties.Schema.STRING,
            _('Network ID this subnet belongs to.'),
            required=True,
            update_allowed=False,
        ),
        IP_PREFIX: properties.Schema(
            properties.Schema.STRING,
            _('IP prefix of subnet.'),
            required=True,
            update_allowed=True,
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
    }

    attributes_schema = {
        "name": _("The name of the Virtual Network."),
        "network_id": _("Network ID this subnet belongs to."),
        "ip_prefix": _("IP prefix of subnet."),
        "default_gateway": _("Default gateway of subnet."),
        "ipam": _("IPAM this subnet uses."),
        "subnet_uuid": _("UUID of subnet."),
        "subnet_name": _("Name of subnet"),
        "show": _("All attributes."),
    }

    def _get_subnets(self, vn_obj, ipam):
        subnets = []
        for ref in vn_obj.get_network_ipam_refs() or []:
            if ref['to'] == ipam.get_fq_name():
                subnets = ref['attr'].get_ipam_subnets()
                break
        return subnets

    def _get_ipam(self):
        ipam_id = self.properties[self.IPAM]
        if ipam_id:
            ipam = self.vnc_lib().network_ipam_read(id=ipam_id)
        else:
            tenant_id = self.stack.context.tenant_id
            project_obj = self.vnc_lib().project_read(
                id=str(uuid.UUID(tenant_id)))
            ipam_fq_name = project_obj.get_fq_name() + ['default-network-ipam']
            try:
                ipam = self.vnc_lib().network_ipam_read(fq_name=ipam_fq_name)
            except vnc_api.NoIdError:
                ipam_obj = vnc_api.NetworkIpam('default-network-ipam',
                                               project_obj)
                ipam_id = self.vnc_lib().network_ipam_create(ipam_obj)
                ipam = self.vnc_lib().network_ipam_read(id=ipam_id)
        return ipam

    def handle_create(self):
        vn_obj = self.vnc_lib().virtual_network_read(
            id=self.properties[self.NETWORK_ID])
        net = netaddr.IPNetwork(self.properties[self.IP_PREFIX])
        ipam = self._get_ipam()
        subnets = self._get_subnets(vn_obj, ipam)
        subnet_uuid = uuid.uuid4()
        subnet = vnc_api.IpamSubnetType(
            subnet_name=self.properties[self.NAME],
            subnet=vnc_api.SubnetType(str(net.ip), net.prefixlen),
            default_gateway=self.properties[self.DEFAULT_GATEWAY],
            subnet_uuid=subnet_uuid)
        if subnets:
            subnets.append(subnet)
            vn_obj._pending_field_updates.add('network_ipam_refs')
        else:
            vn_obj.add_network_ipam(ipam, vnc_api.VnSubnetsType([subnet]))
        self.vnc_lib().virtual_network_update(vn_obj)
        self.resource_id_set(subnet_uuid)

    def _show_resource(self):
        dic = {}
        dic['network_id'] = self.properties[self.NETWORK_ID]
        dic['ip_block'] = self.properties[self.IP_PREFIX]
        dic['gateway'] = self.properties[self.DEFAULT_GATEWAY]
        dic['subnet_uuid'] = self.resource_id
        dic['ipam'] = self.get_ipam().get_uuid()
        dic['name'] = self.properties[self.NAME]

    def handle_delete(self):
        subnet_uuid = self.resource_id
        if subnet_uuid:
            vn_obj = self.vnc_lib().virtual_network_read(
                id=self.properties[self.NETWORK_ID])
            ipam = self._get_ipam()
            subnets = self._get_subnets(vn_obj, ipam)
            for subnet in subnets:
                if (subnet.get_subnet_uuid() and
                        subnet.get_subnet_uuid()['int'] == int(
                            uuid.UUID(subnet_uuid))):
                    subnets.remove(subnet)
                    vn_obj._pending_field_updates.add('network_ipam_refs')
                    break
            if not subnets:
                vn_obj.del_network_ipam(ipam)
            self.vnc_lib().virtual_network_update(vn_obj)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
        pass


def resource_mapping():
    return {
        'OS::Contrail::VnSubnet': HeatVnSubnet,
    }
