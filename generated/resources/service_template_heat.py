
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
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
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailServiceTemplate(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, SERVICE_TEMPLATE_PROPERTIES, SERVICE_TEMPLATE_PROPERTIES_VERSION, SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE, SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE, SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME, SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING, SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE, SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP, SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE, SERVICE_TEMPLATE_PROPERTIES_FLAVOR, SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES, SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE, SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE, SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE, SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA, SERVICE_APPLIANCE_SET_REFS, DOMAIN
    ) = (
        'name', 'fq_name', 'display_name', 'service_template_properties', 'service_template_properties_version', 'service_template_properties_service_mode', 'service_template_properties_service_type', 'service_template_properties_image_name', 'service_template_properties_service_scaling', 'service_template_properties_interface_type', 'service_template_properties_interface_type_service_interface_type', 'service_template_properties_interface_type_shared_ip', 'service_template_properties_interface_type_static_route_enable', 'service_template_properties_flavor', 'service_template_properties_ordered_interfaces', 'service_template_properties_service_virtualization_type', 'service_template_properties_availability_zone_enable', 'service_template_properties_vrouter_instance_type', 'service_template_properties_instance_data', 'service_appliance_set_refs', 'domain'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        SERVICE_TEMPLATE_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('SERVICE_TEMPLATE_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                SERVICE_TEMPLATE_PROPERTIES_VERSION: properties.Schema(
                    properties.Schema.INTEGER,
                    _('SERVICE_TEMPLATE_PROPERTIES_VERSION.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'transparent', u'in-network', u'in-network-nat']),
                    ],
                ),
                SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'firewall', u'analyzer', u'source-nat', u'loadbalancer']),
                    ],
                ),
                SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE: properties.Schema(
                    properties.Schema.LIST,
                    _('SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE: properties.Schema(
                                properties.Schema.STRING,
                                _('SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP: properties.Schema(
                                properties.Schema.BOOLEAN,
                                _('SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE: properties.Schema(
                                properties.Schema.BOOLEAN,
                                _('SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
                SERVICE_TEMPLATE_PROPERTIES_FLAVOR: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_FLAVOR.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'virtual-machine', u'network-namespace', u'vrouter-instance', u'physical-device']),
                    ],
                ),
                SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE.'),
                    update_allowed=True,
                    required=False,
                ),
                SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'libvirt-qemu', u'docker']),
                    ],
                ),
                SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA: properties.Schema(
                    properties.Schema.STRING,
                    _('SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        SERVICE_APPLIANCE_SET_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SERVICE_APPLIANCE_SET_REFS.'),
            update_allowed=True,
            required=False,
        ),
        DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('DOMAIN.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        SERVICE_TEMPLATE_PROPERTIES: attributes.Schema(
            _('SERVICE_TEMPLATE_PROPERTIES.'),
        ),
        SERVICE_APPLIANCE_SET_REFS: attributes.Schema(
            _('SERVICE_APPLIANCE_SET_REFS.'),
        ),
        DOMAIN: attributes.Schema(
            _('DOMAIN.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.DOMAIN):
            try:
                parent_obj = self.vnc_lib().domain_read(id=self.properties.get(self.DOMAIN))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().domain_read(fq_name_str=self.properties.get(self.DOMAIN))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.ServiceTemplate(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceTemplateType()
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VERSION) is not None:
                obj_1.set_version(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VERSION))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE) is not None:
                obj_1.set_service_mode(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE) is not None:
                obj_1.set_service_type(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME) is not None:
                obj_1.set_image_name(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING) is not None:
                obj_1.set_service_scaling(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE) is not None:
                for index_1 in range(len(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE))):
                    obj_2 = vnc_api.ServiceTemplateInterfaceType()
                    if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE) is not None:
                        obj_2.set_service_interface_type(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE))
                    if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP) is not None:
                        obj_2.set_shared_ip(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP))
                    if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE) is not None:
                        obj_2.set_static_route_enable(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE))
                    obj_1.add_interface_type(obj_2)
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_FLAVOR) is not None:
                obj_1.set_flavor(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_FLAVOR))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES) is not None:
                obj_1.set_ordered_interfaces(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE) is not None:
                obj_1.set_service_virtualization_type(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE) is not None:
                obj_1.set_availability_zone_enable(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE) is not None:
                obj_1.set_vrouter_instance_type(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE))
            if self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA) is not None:
                obj_1.set_instance_data(self.properties.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA))
            obj_0.set_service_template_properties(obj_1)

        # reference to service_appliance_set_refs
        if self.properties.get(self.SERVICE_APPLIANCE_SET_REFS):
            for index_0 in range(len(self.properties.get(self.SERVICE_APPLIANCE_SET_REFS))):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=self.properties.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                obj_0.add_service_appliance_set(ref_obj)

        try:
            obj_uuid = super(ContrailServiceTemplate, self).resource_create(obj_0)
        except:
            raise Exception(_('service-template %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().service_template_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('service-template %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES) is not None:
            obj_1 = vnc_api.ServiceTemplateType()
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VERSION) is not None:
                obj_1.set_version(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VERSION))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE) is not None:
                obj_1.set_service_mode(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_MODE))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE) is not None:
                obj_1.set_service_type(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_TYPE))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME) is not None:
                obj_1.set_image_name(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_IMAGE_NAME))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING) is not None:
                obj_1.set_service_scaling(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_SCALING))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE) is not None:
                for index_1 in range(len(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE))):
                    obj_2 = vnc_api.ServiceTemplateInterfaceType()
                    if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE) is not None:
                        obj_2.set_service_interface_type(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SERVICE_INTERFACE_TYPE))
                    if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP) is not None:
                        obj_2.set_shared_ip(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_SHARED_IP))
                    if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE) is not None:
                        obj_2.set_static_route_enable(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE, {})[index_1].get(self.SERVICE_TEMPLATE_PROPERTIES_INTERFACE_TYPE_STATIC_ROUTE_ENABLE))
                    obj_1.add_interface_type(obj_2)
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_FLAVOR) is not None:
                obj_1.set_flavor(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_FLAVOR))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES) is not None:
                obj_1.set_ordered_interfaces(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_ORDERED_INTERFACES))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE) is not None:
                obj_1.set_service_virtualization_type(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_SERVICE_VIRTUALIZATION_TYPE))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE) is not None:
                obj_1.set_availability_zone_enable(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_AVAILABILITY_ZONE_ENABLE))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE) is not None:
                obj_1.set_vrouter_instance_type(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_VROUTER_INSTANCE_TYPE))
            if prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA) is not None:
                obj_1.set_instance_data(prop_diff.get(self.SERVICE_TEMPLATE_PROPERTIES, {}).get(self.SERVICE_TEMPLATE_PROPERTIES_INSTANCE_DATA))
            obj_0.set_service_template_properties(obj_1)

        # reference to service_appliance_set_refs
        ref_obj_list = []
        ref_data_list = []
        if self.SERVICE_APPLIANCE_SET_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        id=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().service_appliance_set_read(
                        fq_name_str=prop_diff.get(self.SERVICE_APPLIANCE_SET_REFS)[index_0]
                    )
                ref_obj_list.append(ref_obj.fq_name)

            obj_0.set_service_appliance_set_list(ref_obj_list)
            # End: reference to service_appliance_set_refs

        try:
            self.vnc_lib().service_template_update(obj_0)
        except:
            raise Exception(_('service-template %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().service_template_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('service_template %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().service_template_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::ServiceTemplate': ContrailServiceTemplate,
    }
