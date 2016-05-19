contrail-heat
=============
Opencontrail heat plugin, resources and templates

In Release 2.x, we supported a few contrail heat resources which were
hand coded.

The R2.x Heat Plugin Resources
------------------------------
Here is a list of all the hand-written plugin resources supported by
contrail-heat in Release 2.x

  attach_policy.py
  network_ipam.py
  network_policy.py
  physical_router.py
  port_tuple.py
  service_health_check.py
  service_instance.py
  virtual_machine_interface.py
  virtual_network.py
  vn_subnet.py
  physical_interface.py
  route_table.py
  service_template.py

With Release 3.0, contrail-heat resources/templates are being auto-generated
from the Schema. 

The generated resources/templates are part of the python-contrail package
and located in /usr/lib/python2.7/dist-packages/vnc_api/gen/heat/
directory in the target installation. This directory has three sub-directories

1. resources/ 
   This sub-directory contains all the resources for the contrail-heat plugin.
   It runs in the context of the heat-engine service.
2. templates/
   This sub-directory contains template for each resource. They are sample
   templates with every possible parameter in the schema. They should be used
   as a reference when you build up more complex templates for your network
   design.
3. env/
   This sub-directories contains environment for input to each template.

The Heat Plugin Resources
-------------------------
Here is a list of all the generated plugin resources supported by
contrail-heat in Release 3.0

  access_control_list_heat.py
  analytics_node_heat.py
  api_access_list_heat.py
  bgp_as_a_service_heat.py
  bgp_router_heat.py
  config_node_heat.py
  config_root_heat.py
  customer_attachment_heat.py
  database_node_heat.py
  discovery_service_assignment_heat.py
  domain_heat.py
  dsa_rule_heat.py
  floating_ip_heat.py
  floating_ip_pool_heat.py
  global_system_config_heat.py
  global_vrouter_config_heat.py
  instance_ip_heat.py
  interface_route_table_heat.py
  loadbalancer_healthmonitor_heat.py
  loadbalancer_heat.py
  loadbalancer_listener_heat.py
  loadbalancer_member_heat.py
  loadbalancer_pool_heat.py
  logical_interface_heat.py
  logical_router_heat.py
  namespace_heat.py
  network_ipam_heat.py
  network_policy_heat.py
  physical_interface_heat.py
  physical_router_heat.py
  port_tuple_heat.py
  project_heat.py
  provider_attachment_heat.py
  qos_forwarding_class_heat.py
  qos_queue_heat.py
  route_aggregate_heat.py
  route_table_heat.py
  route_target_heat.py
  routing_instance_heat.py
  routing_policy_heat.py
  security_group_heat.py
  service_appliance_heat.py
  service_appliance_set_heat.py
  service_health_check_heat.py
  service_instance_heat.py
  service_template_heat.py
  subnet_heat.py
  virtual_DNS_heat.py
  virtual_DNS_record_heat.py
  virtual_ip_heat.py
  virtual_machine_heat.py
  virtual_machine_interface_heat.py
  virtual_network_heat.py
  virtual_router_heat.py
