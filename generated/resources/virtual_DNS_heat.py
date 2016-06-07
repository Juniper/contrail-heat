
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


class ContrailVirtualDns(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, VIRTUAL_DNS_DATA, VIRTUAL_DNS_DATA_DOMAIN_NAME, VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT, VIRTUAL_DNS_DATA_RECORD_ORDER, VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS, VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS, VIRTUAL_DNS_DATA_FLOATING_IP_RECORD, VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE, VIRTUAL_DNS_DATA_REVERSE_RESOLUTION, DOMAIN
    ) = (
        'name', 'fq_name', 'display_name', 'virtual_dns_data', 'virtual_dns_data_domain_name', 'virtual_dns_data_dynamic_records_from_client', 'virtual_dns_data_record_order', 'virtual_dns_data_default_ttl_seconds', 'virtual_dns_data_next_virtual_dns', 'virtual_dns_data_floating_ip_record', 'virtual_dns_data_external_visible', 'virtual_dns_data_reverse_resolution', 'domain'
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
        VIRTUAL_DNS_DATA: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_DNS_DATA.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_DNS_DATA_DOMAIN_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_DATA_DOMAIN_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_DATA_RECORD_ORDER: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_DATA_RECORD_ORDER.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'fixed', u'random', u'round-robin']),
                    ],
                ),
                VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_DATA_FLOATING_IP_RECORD: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_DATA_FLOATING_IP_RECORD.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'dashed-ip', u'dashed-ip-tenant-name', u'vm-name', u'vm-name-tenant-name']),
                    ],
                ),
                VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_DATA_REVERSE_RESOLUTION: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('VIRTUAL_DNS_DATA_REVERSE_RESOLUTION.'),
                    update_allowed=True,
                    required=False,
                ),
            }
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
        VIRTUAL_DNS_DATA: attributes.Schema(
            _('VIRTUAL_DNS_DATA.'),
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

        obj_0 = vnc_api.VirtualDns(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.VIRTUAL_DNS_DATA) is not None:
            obj_1 = vnc_api.VirtualDnsType()
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DOMAIN_NAME) is not None:
                obj_1.set_domain_name(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DOMAIN_NAME))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT) is not None:
                obj_1.set_dynamic_records_from_client(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_RECORD_ORDER) is not None:
                obj_1.set_record_order(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_RECORD_ORDER))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS) is not None:
                obj_1.set_default_ttl_seconds(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS) is not None:
                obj_1.set_next_virtual_DNS(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_FLOATING_IP_RECORD) is not None:
                obj_1.set_floating_ip_record(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_FLOATING_IP_RECORD))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE) is not None:
                obj_1.set_external_visible(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE))
            if self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_REVERSE_RESOLUTION) is not None:
                obj_1.set_reverse_resolution(self.properties.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_REVERSE_RESOLUTION))
            obj_0.set_virtual_DNS_data(obj_1)

        try:
            obj_uuid = super(ContrailVirtualDns, self).resource_create(obj_0)
        except:
            raise Exception(_('virtual-DNS %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_DNS_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('virtual-DNS %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.VIRTUAL_DNS_DATA) is not None:
            obj_1 = vnc_api.VirtualDnsType()
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DOMAIN_NAME) is not None:
                obj_1.set_domain_name(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DOMAIN_NAME))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT) is not None:
                obj_1.set_dynamic_records_from_client(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DYNAMIC_RECORDS_FROM_CLIENT))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_RECORD_ORDER) is not None:
                obj_1.set_record_order(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_RECORD_ORDER))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS) is not None:
                obj_1.set_default_ttl_seconds(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_DEFAULT_TTL_SECONDS))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS) is not None:
                obj_1.set_next_virtual_DNS(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_NEXT_VIRTUAL_DNS))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_FLOATING_IP_RECORD) is not None:
                obj_1.set_floating_ip_record(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_FLOATING_IP_RECORD))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE) is not None:
                obj_1.set_external_visible(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_EXTERNAL_VISIBLE))
            if prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_REVERSE_RESOLUTION) is not None:
                obj_1.set_reverse_resolution(prop_diff.get(self.VIRTUAL_DNS_DATA, {}).get(self.VIRTUAL_DNS_DATA_REVERSE_RESOLUTION))
            obj_0.set_virtual_DNS_data(obj_1)

        try:
            self.vnc_lib().virtual_DNS_update(obj_0)
        except:
            raise Exception(_('virtual-DNS %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_DNS_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_DNS %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().virtual_DNS_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualDns': ContrailVirtualDns,
    }
