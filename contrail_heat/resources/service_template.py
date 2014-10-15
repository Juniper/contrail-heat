from heat.engine import constraints
from heat.engine import properties
from heat.openstack.common import log as logging
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource

logger = logging.getLogger(__name__)


class HeatServiceTemplate(ContrailResource):
    PROPERTIES = (
        NAME, DOMAIN, SERVICE_MODE, SERVICE_TYPE, IMAGE_NAME,
        SERVICE_SCALING, INTERFACE_TYPE, FLAVOR, ORDERED_INTERFACES,
        SERVICE_VIRT_TYPE, AVAILABILITY_ZONE_ENABLE
    ) = (
        'name', 'domain', 'service_mode', 'service_type', 'image_name',
        'service_scaling', 'interface_type', 'flavor', 'ordered_interfaces',
        'service_virtualization_type', 'availability_zone_enable'
    )

    _INTERFACE_KEYS = (
        SERVICE_INTERFACE_TYPE, SHARED_IP, STATIC_ROUTE_ENABLE
    ) = (
        'service_interface_type', 'shared_ip', 'static_route_enable'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Service Template name'),
            update_allowed=False,
        ),
        DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('Name of the Domain where Template needs to be created'),
            update_allowed=False,
            default='default-domain'
        ),
        SERVICE_MODE: properties.Schema(
            properties.Schema.STRING,
            _('Service Mode'),
            constraints=[
                constraints.AllowedValues(['transparent', 'in-network',
                                           'in-network-nat']),
            ],
            update_allowed=False,
            required=True,
        ),
        SERVICE_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('Service Type'),
            constraints=[
                constraints.AllowedValues(['firewall', 'analyzer',
                                           'source-nat', 'loadbalancer']),
            ],
            update_allowed=False,
            required=True,
        ),
        IMAGE_NAME: properties.Schema(
            properties.Schema.STRING,
            _('Name of the service VM image'),
            update_allowed=False,
            required=True,
        ),
        SERVICE_SCALING: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Indicates whether service scaling is enabled'),
            update_allowed=False,
            default=False,
        ),
        INTERFACE_TYPE: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of interfaces to be added to this service'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    SERVICE_INTERFACE_TYPE: properties.Schema(
                        properties.Schema.STRING,
                        _('Service Interface type'),
                        required=True,
                        constraints=[
                            constraints.AllowedValues(['management', 'left',
                                                       'right', 'other']),
                        ],
                    ),
                    SHARED_IP: properties.Schema(
                        properties.Schema.BOOLEAN,
                        _('IP is shared for this interface'),
                        default=False,
                    ),
                    STATIC_ROUTE_ENABLE: properties.Schema(
                        properties.Schema.BOOLEAN,
                        _('Static routes enabled'),
                        default=False,
                    ),
                },
            ),
            required=True,
            update_allowed=False
        ),
        FLAVOR: properties.Schema(
            properties.Schema.STRING,
            _('Indicates service VM flavor'),
            update_allowed=False,
            required=True,
        ),
        ORDERED_INTERFACES: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Indicates service interfaces are ordered'),
            default=False,
            update_allowed=False
        ),
        SERVICE_VIRT_TYPE: properties.Schema(
            properties.Schema.STRING,
            _('Indicates service VM virtualization type'),
            default='virtual-machine',
            constraints=[
                constraints.AllowedValues(['virtual-machine',
                                           'network-namespace']),
            ],
            update_allowed=False
        ),
        AVAILABILITY_ZONE_ENABLE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Indicates availability zone is enabled'),
            default=False,
            update_allowed=False
        )
    }

    attributes_schema = {
        "name": _("The name of the Service Template."),
        "fq_name": _("The FQ name of the Service Template."),
        "service_instaces": _("Service Instances launched with this service "
                              "template."),
        "show": _("All attributes."),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        domain = self.vnc_lib().domain_read(
            fq_name=[self.properties[self.DOMAIN]])
        st_obj = vnc_api.ServiceTemplate(name=self.properties[self.NAME],
                                         parent_obj=domain)
        st_uuid = self.vnc_lib().service_template_create(st_obj)
        svc_properties = vnc_api.ServiceTemplateType()
        svc_properties.set_image_name(self.properties[self.IMAGE_NAME])
        svc_properties.set_flavor(self.properties[self.FLAVOR])
        svc_properties.set_service_scaling(
            self.properties[self.SERVICE_SCALING])
        svc_properties.set_service_mode(self.properties[self.SERVICE_MODE])
        svc_properties.set_service_type(self.properties[self.SERVICE_TYPE])
        svc_properties.set_service_virtualization_type(
            self.properties[self.SERVICE_VIRT_TYPE])
        # set interface list
        for itf in self.properties[self.INTERFACE_TYPE]:
            if_type = vnc_api.ServiceTemplateInterfaceType(
                shared_ip=itf[self.SHARED_IP])
            if_type.set_service_interface_type(
                itf[self.SERVICE_INTERFACE_TYPE])
            if_type.set_static_route_enable(itf[self.STATIC_ROUTE_ENABLE])
            svc_properties.add_interface_type(if_type)
        st_obj.set_service_template_properties(svc_properties)
        self.vnc_lib().service_template_update(st_obj)
        self.resource_id_set(st_uuid)

    def _show_resource(self):
        st_obj = self.vnc_lib().service_template_read(id=self.resource_id)
        dict = {}
        dict['name'] = st_obj.get_display_name()
        dict['fq_name'] = st_obj.get_fq_name_str()
        sis = []
        for si_ref in st_obj.get_service_instance_back_refs() or []:
            si_info = {}
            si_info['name'] = ':'.join(si_ref['to'])
            si_info['uuid'] = si_ref['uuid']
            sis.append(si_info)
        dict['service_instances'] = sis
        return dict

    def handle_delete(self):
        try:
            self.vnc_lib().service_template_delete(id=self.resource_id)
        except Exception:
            pass

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        pass


def resource_mapping():
    return {
        'OS::Contrail::ServiceTemplate': HeatServiceTemplate,
    }
