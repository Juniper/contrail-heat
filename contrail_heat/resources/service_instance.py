try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import constraints
from novaclient import exceptions as nova_exceptions
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from heat.engine import scheduler
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource
import uuid

LOG = logging.getLogger(__name__)


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
            _('An ordered list of interfaces to be added to this '
              'service instance'),
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
                        _('An ordered list of static routes to be added '
                          'to this interface'),
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
            update_allowed=True,
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
        "active_service_vms": _("Number of service VMs active for this "
                                "Service Instance."),
        "tenant_id": _("Tenant id of the Service Instance."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        try:
            st_obj = self.vnc_lib().service_template_read(
                id=self.properties[self.SERVICE_TEMPLATE])
        except vnc_api.NoIdError:
            st_obj = self.vnc_lib().service_template_read(
                fq_name_str=self.properties[self.SERVICE_TEMPLATE])

        tenant_id = self.stack.context.tenant_id
        project_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))
        si_obj = vnc_api.ServiceInstance(
            name=self.properties[self.NAME], parent_obj=project_obj)

        svc_tmpl_if_list = st_obj.get_service_template_properties().interface_type
        svc_inst_if_list = self.properties[self.INTERFACE_LIST]
        if len(svc_tmpl_if_list) != len(svc_inst_if_list):
            raise vnc_api.BadRequest

        if_index = 0
        si_prop = vnc_api.ServiceInstanceType()
        for intf in self.properties[self.INTERFACE_LIST]:
            virt_net = intf[self.VIRTUAL_NETWORK]
            if virt_net == "auto":
                vn_name = ""
            elif not ":" in virt_net:
                fq_name = self.vnc_lib().id_to_fq_name(virt_net)
                vn_name = ":".join(fq_name)
            else:
                vn_name = virt_net

            # now check for static routes on this interface
            routes_list = {}
            if svc_tmpl_if_list[if_index].get_static_route_enable(
                ) and self.STATIC_ROUTES in intf:
                routes_list['route'] = intf[self.STATIC_ROUTES]

            if_type = vnc_api.ServiceInstanceInterfaceType(
                virtual_network=vn_name,static_routes=routes_list or None)
            si_prop.add_interface_list(if_type)
            if_index = if_index + 1

        if self.properties[self.SCALE_OUT] is None:
            max_instances = 1
            auto_scale = False
        else:
            max_instances = self.properties[self.SCALE_OUT][self.MAX_INSTANCES]
            auto_scale = self.properties[self.SCALE_OUT][self.AUTO_SCALE]
        scale_out = vnc_api.ServiceScaleOutType(max_instances=max_instances,
                                                auto_scale=auto_scale)
        si_prop.set_scale_out(scale_out)

        si_prop.set_availability_zone(self.properties[self.AVAILABILITY_ZONE])

        si_prop.set_ha_mode(self.properties[self.HA_MODE])
        si_obj.set_service_instance_properties(si_prop)

        st_obj = self.vnc_lib().service_template_read(id=st_obj.uuid)
        si_obj.set_service_template(st_obj)

        si_uuid = self.vnc_lib().service_instance_create(si_obj)
        self.resource_id_set(si_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            si_obj = self.vnc_lib().service_instance_read(id=self.resource_id)
        except vnc_api.NoIdError:
            LOG.warn(_("Service Instance %s not found.") % self.name)
            raise
        except:
            LOG.warn(_("Unknown error."))
            raise

        si_prop = si_obj.get_service_instance_properties()

        scaleprop = prop_diff.get(self.SCALE_OUT)
        if scaleprop:
            max_instances = scaleprop.get(self.MAX_INSTANCES)
            auto_scale = scaleprop.get(self.AUTO_SCALE)
        scale_out = vnc_api.ServiceScaleOutType(max_instances=max_instances,
                                                auto_scale=auto_scale)
        si_prop.set_scale_out(scale_out)

        si_obj.set_service_instance_properties(si_prop)
        self.vnc_lib().service_instance_update(si_obj)

    def get_vm(self, vm):
        '''
        Refresh vm's attributes and log warnings for non-critical API errors.
        '''
        try:
            vm.get()
        except nova_exceptions.OverLimit as exc:
            msg = _("Server %(name)s (%(id)s) received an OverLimit "
                    "response during vm.get(): %(exception)s")
            logger.warning(msg % {'name': vm.name,
                                  'id': vm.id,
                                  'exception': str(exc)})
        except nova_exceptions.ClientException as exc:
            if ((getattr(exc, 'http_status', getattr(exc, 'code', None)) in
                 (500, 503))):
                msg = _('Server "%(name)s" (%(id)s) received the following '
                        'exception during vm.get(): %(exception)s')
                logger.warning(msg % {'name': vm.name,
                                      'id': vm.id,
                                      'exception': str(exc)})
            else:
                raise

    def delete_vm(self, vm):
        '''
        Return a routine that deletes the vm and waits for it to
        disappear from Nova.
        '''

        while True:
            yield

            try:
                self.get_vm(vm)
            except nova_exceptions.NotFound:
                break

    def handle_delete(self):
        try:
            # get the servers list
            si_obj = self.vnc_lib().service_instance_read(id=self.resource_id)
            vm_uuid_list = list(si_obj.get_virtual_machine_back_refs() or [])

            self.vnc_lib().service_instance_delete(id=self.resource_id)

            for vm_uuid in vm_uuid_list or []:
                try:
                    vm = self.nova().servers.get(vm_uuid['to'][0])
                except nova_exceptions.NotFound:
                    pass
                else:
                    delete = scheduler.TaskRunner(self.delete_vm, vm)
                    delete(wait_time=1.0)

        except vnc_api.NoIdError:
            LOG.warn(_("Service Instance %s not found.") % self.name)
        except:
            LOG.warn(_("Unknown error."))
            raise

    def _show_resource(self):
        si_obj = self.vnc_lib().service_instance_read(id=self.resource_id)
        dict = {}
        dict['name'] = si_obj.get_display_name()
        dict['fq_name'] = si_obj.get_fq_name_str()
        dict['tenant_id'] = si_obj.parent_uuid
        svms = []
        status = 'INACTIVE'
        inactive_count = 0
        active_count = 0
        for vms in si_obj.get_virtual_machine_back_refs() or []:
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
        elif active_count == 0:
            status = "INACTIVE"
        elif active_count == len(si_obj.get_virtual_machine_back_refs() or []):
            status = "ACTIVE"
        dict['status'] = status
        dict['active_service_vms'] = active_count
        dict['service_template'] = ':'.join(
            si_obj.get_service_template_refs()[0]['to'])
        return dict


def resource_mapping():
    return {
        'OS::Contrail::ServiceInstance': HeatServiceInstance,
    }
