
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


class ContrailVirtualDnsRecord(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, VIRTUAL_DNS_RECORD_DATA, VIRTUAL_DNS_RECORD_DATA_RECORD_NAME, VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE, VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS, VIRTUAL_DNS_RECORD_DATA_RECORD_DATA, VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS, VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE, DISPLAY_NAME, VIRTUAL_DNS
    ) = (
        'name', 'fq_name', 'virtual_dns_record_data', 'virtual_dns_record_data_record_name', 'virtual_dns_record_data_record_type', 'virtual_dns_record_data_record_class', 'virtual_dns_record_data_record_data', 'virtual_dns_record_data_record_ttl_seconds', 'virtual_dns_record_data_record_mx_preference', 'display_name', 'virtual_dns'
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
        VIRTUAL_DNS_RECORD_DATA: properties.Schema(
            properties.Schema.MAP,
            _('VIRTUAL_DNS_RECORD_DATA.'),
            update_allowed=True,
            required=False,
            schema={
                VIRTUAL_DNS_RECORD_DATA_RECORD_NAME: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_NAME.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'A', u'AAAA', u'CNAME', u'PTR', u'NS', u'MX']),
                    ],
                ),
                VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'IN']),
                    ],
                ),
                VIRTUAL_DNS_RECORD_DATA_RECORD_DATA: properties.Schema(
                    properties.Schema.STRING,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_DATA.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS.'),
                    update_allowed=True,
                    required=False,
                ),
                VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE: properties.Schema(
                    properties.Schema.INTEGER,
                    _('VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_DNS: properties.Schema(
            properties.Schema.STRING,
            _('VIRTUAL_DNS.'),
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
        VIRTUAL_DNS_RECORD_DATA: attributes.Schema(
            _('VIRTUAL_DNS_RECORD_DATA.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        VIRTUAL_DNS: attributes.Schema(
            _('VIRTUAL_DNS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.VIRTUAL_DNS):
            try:
                parent_obj = self.vnc_lib().virtual_dns_read(id=self.properties.get(self.VIRTUAL_DNS))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().virtual_dns_read(fq_name_str=self.properties.get(self.VIRTUAL_DNS))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.VirtualDnsRecord(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA) is not None:
            obj_1 = vnc_api.VirtualDnsRecordType()
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_NAME) is not None:
                obj_1.set_record_name(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_NAME))
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE) is not None:
                obj_1.set_record_type(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE))
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS) is not None:
                obj_1.set_record_class(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS))
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_DATA) is not None:
                obj_1.set_record_data(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_DATA))
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS) is not None:
                obj_1.set_record_ttl_seconds(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS))
            if self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE) is not None:
                obj_1.set_record_mx_preference(self.properties.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE))
            obj_0.set_virtual_DNS_record_data(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        try:
            obj_uuid = super(ContrailVirtualDnsRecord, self).resource_create(obj_0)
        except:
            raise Exception(_('virtual-DNS-record %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().virtual_DNS_record_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('virtual-DNS-record %s not found.') % self.name)

        if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA) is not None:
            obj_1 = vnc_api.VirtualDnsRecordType()
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_NAME) is not None:
                obj_1.set_record_name(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_NAME))
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE) is not None:
                obj_1.set_record_type(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TYPE))
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS) is not None:
                obj_1.set_record_class(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_CLASS))
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_DATA) is not None:
                obj_1.set_record_data(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_DATA))
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS) is not None:
                obj_1.set_record_ttl_seconds(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_TTL_SECONDS))
            if prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE) is not None:
                obj_1.set_record_mx_preference(prop_diff.get(self.VIRTUAL_DNS_RECORD_DATA, {}).get(self.VIRTUAL_DNS_RECORD_DATA_RECORD_MX_PREFERENCE))
            obj_0.set_virtual_DNS_record_data(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        try:
            self.vnc_lib().virtual_DNS_record_update(obj_0)
        except:
            raise Exception(_('virtual-DNS-record %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().virtual_DNS_record_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('virtual_DNS_record %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().virtual_DNS_record_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::VirtualDnsRecord': ContrailVirtualDnsRecord,
    }
