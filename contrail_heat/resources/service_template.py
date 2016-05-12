try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from vnc_api import vnc_api
from contrail_heat.resources.contrail import ContrailResource

logger = logging.getLogger(__name__)


class HeatServiceTemplate(ContrailResource):
    PROPERTIES = (
        NAME, DOMAIN, SERVICE_MODE, SERVICE_TYPE, IMAGE_NAME,
        SERVICE_SCALING, SERVICE_INTERFACE_TYPE_LIST, SHARED_IP_LIST,
        STATIC_ROUTES_LIST, FLAVOR, ORDERED_INTERFACES,
        SERVICE_VIRT_TYPE, AVAILABILITY_ZONE_ENABLE, SERVICE_VERSION
    ) = (
        'name', 'domain', 'service_mode', 'service_type', 'image_name',
        'service_scaling', 'service_interface_type_list', 'shared_ip_list',
        'static_routes_list', 'flavor', 'ordered_interfaces',
        'service_virtualization_type', 'availability_zone_enable',
        'service_version'
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
            properties.Schema.STRING,
            _('Indicates whether service scaling is enabled'),
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=False,
            default='False',
        ),
        SERVICE_INTERFACE_TYPE_LIST: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of interfaces to be added to this service'),
            required=True,
            constraints=[
                constraints.AllowedValues(['management', 'left',
                                           'right', 'other']),
            ],
            update_allowed=False
        ),
        SHARED_IP_LIST: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of shared ip enabled for each interface'),
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=False
        ),
        STATIC_ROUTES_LIST: properties.Schema(
            properties.Schema.LIST,
            _('An ordered list of static routes enabled for each interface'),
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=False
        ),
        FLAVOR: properties.Schema(
            properties.Schema.STRING,
            _('Indicates service VM flavor'),
            update_allowed=False,
        ),
        ORDERED_INTERFACES: properties.Schema(
            properties.Schema.STRING,
            _('Indicates service interfaces are ordered'),
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            default='False',
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
            properties.Schema.STRING,
            _('Indicates availability zone is enabled'),
            constraints=[
                constraints.AllowedValues(['True', 'False']),
            ],
            update_allowed=False
        ),
        SERVICE_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('Indicates version for the template'),
            constraints=[
                constraints.AllowedValues([1, 2]),
            ],
            default='1',
            update_allowed=False
        ),
    }

    attributes_schema = {
        "name": attributes.Schema(
            _('The name of the Service Template.'),
        ),
        "fq_name": attributes.Schema(
            _('The FQ name of the Service Template.'),
        ),
        "service_instances": attributes.Schema(
            _('Service Instances launched with this service template.'),
        ),
        "show": attributes.Schema(
            _('All attributes.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        domain = self.vnc_lib().domain_read(
            fq_name=[self.properties[self.DOMAIN]])
        st_obj = vnc_api.ServiceTemplate(name=self.properties[self.NAME],
                                         parent_obj=domain)
        svc_properties = vnc_api.ServiceTemplateType()
        svc_properties.set_image_name(self.properties[self.IMAGE_NAME])
        svc_properties.set_flavor(self.properties[self.FLAVOR])
        if self.properties[self.SERVICE_SCALING] == 'True':
            svc_properties.set_service_scaling(True)
        else:
            svc_properties.set_service_scaling(False)
        if self.properties[self.AVAILABILITY_ZONE_ENABLE] == 'True':
            svc_properties.set_availability_zone_enable(True)
        else:
            svc_properties.set_availability_zone_enable(False)
        svc_properties.set_service_mode(self.properties[self.SERVICE_MODE])
        svc_properties.set_service_type(self.properties[self.SERVICE_TYPE])
        svc_properties.set_availability_zone_enable(self.properties[self.AVAILABILITY_ZONE_ENABLE])
        svc_properties.set_service_virtualization_type(
            self.properties[self.SERVICE_VIRT_TYPE])
        svc_properties.set_ordered_interfaces(
            self.properties[self.ORDERED_INTERFACES])
        svc_properties.set_version(int(self.properties[self.SERVICE_VERSION]))
        # set interface list
        itf_list = self.properties[self.SERVICE_INTERFACE_TYPE_LIST]
        for itf in itf_list:
            index = itf_list.index(itf)
            try:
                shared_ip = self.properties[self.SHARED_IP_LIST][index]
                if shared_ip == 'True':
                    shared_ip_val = True
                else:
                    shared_ip_val = False
            except (IndexError, TypeError):
                shared_ip_val = False
            try:
                static_route = self.properties[self.STATIC_ROUTES_LIST][index]
                if static_route == 'True':
                    static_route_val = True
                else:
                    static_route_val = False
            except (IndexError, TypeError):
                static_route_val = False
            if_type = vnc_api.ServiceTemplateInterfaceType(shared_ip=shared_ip_val)
            if_type.set_service_interface_type(itf)
            if_type.set_static_route_enable(static_route_val)
            svc_properties.add_interface_type(if_type)
        st_obj.set_service_template_properties(svc_properties)
        st_uuid = self.vnc_lib().service_template_create(st_obj)
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
