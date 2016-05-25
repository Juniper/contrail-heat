import uuid
import os
import sys
import subprocess
import argparse
from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
#from novaclient import exceptions as nova_exceptions
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from vnc_api import vnc_api


LOG = logging.getLogger(__name__)


class VSRX_HA(contrail.ContrailResource):
    PROPERTIES = (
        VM_NAME, CLUSTER_ID,
    ) = (
        'vm_name', 'cluster_id',
    )

    properties_schema = {
        VM_NAME: properties.Schema(
            properties.Schema.STRING,
            _('Name of vSRX HA service instance to be created'),
            required=True,
            update_allowed=True,
        ),
        CLUSTER_ID: properties.Schema(
            properties.Schema.STRING,
            _('Cluster ID to be used for configuring HA'),
            required=True,
            update_allowed=True
        ),
    }

    attributes_schema = {
        VM_NAME: attributes.Schema(
            _('VM_NAME.'),
        ),
        CLUSTER_ID: attributes.Schema(
            _('CLUSTER_ID.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }


    update_allowed_keys = ('Properties',)


    def handle_create(self):
        LOG.info("Adding Allowed address groups for vSRX")
        # need to run /etc/contrail/openstackrc first
        self.shell_source("/etc/contrail/openstackrc")
        self.data_set('vm_name', self.properties[self.VM_NAME], redact=True)
        vm_name = self.properties[self.VM_NAME]
        self.data_set('cluster_id', self.properties[self.CLUSTER_ID], redact=True)
        cluster_id = self.properties[self.CLUSTER_ID]
        cluster_id = int(cluster_id)
        mac_addresses = []
        mac_addresses_node0 = []
        mac_addresses_node1 = []
        # give the VM name in contrail way for the two nodes in scaling mode.
        vm_name_node0 = vm_name + "__1"
        vm_name_node1 = vm_name + "__2"
        mac_addresses_node0 = self.calculate_mac_addr(vm_name_node0, cluster_id)
        mac_addresses_node1 = self.calculate_mac_addr(vm_name_node1, cluster_id)
        mac_addresses.extend(mac_addresses_node0);
        mac_addresses.extend(mac_addresses_node1);
        self.update_port_list(vm_name_node0,mac_addresses,0)
        self.update_port_list(vm_name_node1,mac_addresses,1)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        pass

    def _show_resource(self):
        attrs = {
            'vm_name': self.data()['vm_name'],
            'cluster_id': self.data()['cluster_id'],
        }
        return attrs
 
    def handle_delete(self):
        pass

    #
    # This function calculates the MAC address for the reth interface and returns it to create function
    #
    def calculate_mac_addr (self, vm_name, cluster_id):

        mac_list = []
        # Get management port MAC address first
        neutron_cmd = "neutron port-list | grep %s | grep management | awk '{print $6}' | cut -d':' -f 5,6" % vm_name
        fxp0_mac = os.popen(neutron_cmd).read()
        if not fxp0_mac or len(fxp0_mac)==0:
            LOG.warn("VM does not have a correct management address")
            return;

        # Generate the virtual MAC address for HA left port
        virtual_mac_left = '4c:96:14:' + fxp0_mac.rstrip() + ':01'

        # Generate the virtual MAC address for HA right port
        virtual_mac_right ='4c:96:14:' + fxp0_mac.rstrip() + ':02'

        # get the cluster ID and reth index to generate the reth MAC address
        # The 1st 4 bytes are fixed at 00:10:db:ff
        # the next byte is LSB(4bits) followed by MSB(4bits) of cluster ID.
        # Last byte is the sequence.
        reth_mac_4bit = format((((cluster_id&0x0F)<<4)|cluster_id>>4), 'x')
        reth_mac_left = '00:10:db:ff:' + reth_mac_4bit + ':00'
        reth_mac_right = '00:10:db:ff:' + reth_mac_4bit + ':01'

        mac_list.append(reth_mac_left)
        mac_list.append(reth_mac_right)
        mac_list.append(virtual_mac_left)
        mac_list.append(virtual_mac_right)

        return mac_list;

    def update_port_list (self, vm_name, mac_addresses, node_id): 
        if node_id != 0 and node_id != 1:
            LOG.warn(" incorrect node id")
            return 1;

        # try to get left and right port for that node
        neutron_cmd_left_portid = \
            "neutron port-list | grep %s | grep left | awk '{print $2}'" % vm_name
        neutron_cmd_right_portid= \
            "neutron port-list | grep %s | grep right| awk '{print $2}'" % vm_name

        left_port_id  = os.popen(neutron_cmd_left_portid).read().rstrip()
        right_port_id = os.popen(neutron_cmd_right_portid).read().rstrip()

        neutron_cmd_left_ip = \
            "neutron port-show %s | grep 'subnet_id' | cut -d'\"' -f 8" % left_port_id
        neutron_cmd_right_ip = \
            "neutron port-show %s | grep 'subnet_id' | cut -d'\"' -f 8" % right_port_id

        left_port_ip_list  = os.popen(neutron_cmd_left_ip).read().rstrip()
        right_port_ip_list = os.popen(neutron_cmd_right_ip).read().rstrip()

        if not left_port_ip_list or len(left_port_ip_list)==0:
            LOG.warn("left port has no IP address")
            return 1;
        if not right_port_ip_list or len(right_port_ip_list)==0:
            LOG.warn("right port has no IP address")
            return 1;


        # Update allowed ip-mac paires for left and right ports
        left_port_ip_mac_list = ""
        right_port_ip_mac_list = ""
        for left_port_ip in left_port_ip_list.split('\n'):
            left_port_ip_mac_list = left_port_ip_mac_list + " " + "ip_address=%s,mac_address=%s ip_address=%s,mac_address=%s ip_address=%s,mac_address=%s" % \
                                     (left_port_ip, mac_addresses[4*int(node_id)], left_port_ip, mac_addresses[(node_id*4+2)%8], \
                                      left_port_ip, mac_addresses[(node_id*4+6)%8])
            print left_port_ip_mac_list

        for right_port_ip in right_port_ip_list.split('\n'):
            right_port_ip_mac_list = right_port_ip_mac_list + " " + "ip_address=%s,mac_address=%s ip_address=%s,mac_address=%s ip_address=%s,mac_address=%s" % \
                                     (right_port_ip, mac_addresses[4*int(node_id)+1], right_port_ip, mac_addresses[(node_id*4+3)%8], \
                                      right_port_ip, mac_addresses[(node_id*4+7)%8])
            print right_port_ip_mac_list

        neutron_cmd_left_allowed_ip_mac = \
            "neutron port-update %s --allowed_address_pairs list=true type=dict %s" % \
            (left_port_id, left_port_ip_mac_list)
        neutron_cmd_right_allowed_ip_mac = \
            "neutron port-update %s --allowed_address_pairs list=true type=dict %s" % \
            (right_port_id, right_port_ip_mac_list)

        LOG.warn(neutron_cmd_left_allowed_ip_mac)
        LOG.warn(neutron_cmd_right_allowed_ip_mac)


        left_port_update_mac = os.popen(neutron_cmd_left_allowed_ip_mac).read()
        if left_port_update_mac.find("Updated port") == -1:
            LOG.warn("Failed to update the allowed-address-pairs for left port")
            return 1;

        right_port_update_mac = os.popen(neutron_cmd_right_allowed_ip_mac).read()
        if right_port_update_mac.find("Updated port") == -1:
            LOG.warn("Failed to update the allowed-address-pairs for right port")
            return 1;

        return 0;


    def shell_source(self, script):
        pipe = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
        output = pipe.communicate()[0]
        env = dict((line.split("=", 1) for line in output.splitlines()))
        os.environ.update(env)

def resource_mapping():
    return {
        'OS::Contrail::VSRX_HA': VSRX_HA,
    }
