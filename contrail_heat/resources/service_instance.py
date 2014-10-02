from heat.engine import constraints
from heat.engine import properties
from heat.openstack.common import log as logging
from vnc_api.vnc_api import *
from contrail_heat.resources.contrail import ContrailResource
import uuid

logger = logging.getLogger(__name__)

class HeatServiceInstance(ContrailResource):
    PROPERTIES = (
        NAME, SERVICE_TEMPLATE, AUTO_POLICY, AVAILABILITY_ZONE,
        INTERFACE_LIST, SCALE_OUT, HA_MODE
    ) = (
        'name', 'service_template', 'auto_policy', 'availability_zone',
	'interface_list', 'scale_out', 'ha_mode'
    )

    _INTERFACE_LIST_KEYS = (
        VIRTUAL_NETWORK, IP_ADDRESS, STATIC_ROUTES
    ) = (
        'virtual_network', 'ip_address', 'static_routes'
    )

    _STATIC_ROUTE_KEYS = (
        PREFIX, NEXT_HOP, NEXT_HOP_TYPE
    ) = (
        'prefix', 'next_hop', 'next_hop_type'
    )

    _SCALE_OUT_KEYS = (
        MAX_INSTANCES, AUTO_SCALE
    ) = (
        'max_instances', 'auto_scale'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Service Instance name.'),
            required=True,
            update_allowed=False
        ),
        SERVICE_TEMPLATE: properties.Schema(
            properties.Schema.STRING,
            _('Service Template name.'),
            required=True,
            update_allowed=False
        ),
        AUTO_POLICY: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Auto policy'),
            default=False,
            update_allowed=False
        ),
        AVAILABILITY_ZONE: properties.Schema(
            properties.Schema.STRING,
            _('Availability Zone.'),
            update_allowed=False
        ),
        INTERFACE_LIST: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of interfaces to be added to this service instance'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    VIRTUAL_NETWORK: properties.Schema(
                        properties.Schema.STRING,
                        _('Virtual Network for interface'),
                    ),
                    IP_ADDRESS: properties.Schema(
                        properties.Schema.STRING,
                        _('IP for this interface')
                    ),
                    STATIC_ROUTES: properties.Schema(
                    	properties.Schema.LIST,
            		_('An ordered list of static routes to be added to this interface'),
			schema=properties.Schema(
				properties.Schema.MAP,
				schema={
					PREFIX: properties.Schema(
						properties.Schema.STRING,
						_('Route prefix'),
					),
					NEXT_HOP: properties.Schema(
						properties.Schema.STRING,
						_('Nexthop'),
					),
					NEXT_HOP_TYPE: properties.Schema(
						properties.Schema.STRING,
						_('Nexthop Type'),
					)
				}
			)
                    ),
                }
            ),
            update_allowed=False
        ),
        SCALE_OUT: properties.Schema(
            properties.Schema.MAP,
            _('Scale out property'),
            update_allowed=False,
            schema={
                    MAX_INSTANCES: properties.Schema(
                        properties.Schema.INTEGER,
                        _('Number of instances of service instance'),
            		default=1,
                    ),
                    AUTO_SCALE: properties.Schema(
                        properties.Schema.BOOLEAN,
                        _('Whether to auto scale the service instance'),
            		default=False,
                    )
            }
        ),

	HA_MODE: properties.Schema(
	    properties.Schema.STRING,
	    _('High availability mode'),
	    constraints=[
	        constraints.AllowedValues(['active-active', 'active-standby']),
	    ],
	),
    }

    attributes_schema = {
        "name": _("The name of the Service Instance."),
        "fq_name": _("The FQ name of the Service Instance."),
        "status": _("Status of the Service Instance."),
        "service_template": _("Service Template of the Service Instance."),
        "virtual_machines": _("Service VMs for the Service Instance."),
        "active_service_vms": _("Number of service VMs active for this Service Instance."),
        "tenant_id": _("Tenant id of the Service Instance."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        try:
            st_obj = self.vnc_lib().service_template_read(id=self.properties[self.SERVICE_TEMPLATE])
        except NoIdError:
            st_obj = self.vnc_lib().service_template_read(name=self.properties[self.SERVICE_TEMPLATE])

        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        si_obj = ServiceInstance(name=self.properties[self.NAME], parent_obj=project_obj)
        si_uuid = self.vnc_lib().service_instance_create(si_obj)

        si_prop = ServiceInstanceType()

        for intf in self.properties[self.INTERFACE_LIST]:
            if intf[self.VIRTUAL_NETWORK] == "auto":
                vn = ""
            else:
                vn = intf[self.VIRTUAL_NETWORK]
            if_type = ServiceInstanceInterfaceType(virtual_network=vn)
            si_prop.add_interface_list(if_type)

        if self.properties[self.SCALE_OUT] is None:
            max_instances = 1
            auto_scale = False
        else:
            max_instances = self.properties[self.SCALE_OUT][self.MAX_INSTANCES]
            auto_scale = self.properties[self.SCALE_OUT][self.AUTO_SCALE]
        scale_out = ServiceScaleOutType(max_instances=max_instances,
            auto_scale=auto_scale)
        si_prop.set_scale_out(scale_out)

        si_prop.set_ha_mode(self.properties[self.HA_MODE])
        si_obj.set_service_instance_properties(si_prop)

        st_obj = self.vnc_lib().service_template_read(id=st_obj.uuid)
        si_obj.set_service_template(st_obj)

        self.vnc_lib().service_instance_update(si_obj)
        self.resource_id_set(si_uuid)

    def _show_resource(self):
        si_obj = self.vnc_lib().service_instance_read(id=self.resource_id)
        dict = {}
        dict['name'] = si_obj.get_display_name()
        dict['fq_name'] =si_obj.get_fq_name_str()
        dict['tenant_id'] = si_obj.parent_uuid
        status = 'INACTIVE'
        dict['virtual_machines'] = []
        svms = []
        status = 'INACTIVE'
        inactive_count = 0
        active_count = 0
        for vms in si_obj.get_virtual_machine_back_refs():
            svm = {}
            vm = self.nova().servers.get(vms['to'][0])
            svm['vm_id'] = vm.id
            svm['name'] = vm.name
            svm['status'] = vm.status
            svms.append(svm)
            if vm.status == 'ACTIVE':
                active_count += 1
            else:
                inactive_count += 1
        dict['virtual_machines'] = svms
        if inactive_count and active_count:
            status = "PARTIALLY ACTIVE"
        elif active_count == len(si_obj.get_virtual_machine_back_refs()):
            status = "ACTIVE"
        dict['status'] = status
        dict['active_service_vms'] = active_count
        dict['service_template'] = ':'.join(si_obj.get_service_template_refs()[0]['to'])
	return dict

    def handle_delete(self):
        try:
            self.vnc_lib().service_instance_delete(id=self.resource_id)
        except:
            pass 

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        # TODO
	pass

def resource_mapping():
    return {
        'OS::Contrail::ServiceInstance': HeatServiceInstance,
    }
