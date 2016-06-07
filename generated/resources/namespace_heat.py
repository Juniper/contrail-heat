
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


class ContrailNamespace(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, NAMESPACE_CIDR, NAMESPACE_CIDR_IP_PREFIX, NAMESPACE_CIDR_IP_PREFIX_LEN, DISPLAY_NAME, DOMAIN
    ) = (
        'name', 'fq_name', 'namespace_cidr', 'namespace_cidr_ip_prefix', 'namespace_cidr_ip_prefix_len', 'display_name', 'domain'
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
        NAMESPACE_CIDR: properties.Schema(
            properties.Schema.MAP,
            _('NAMESPACE_CIDR.'),
            update_allowed=True,
            required=False,
            schema={
                NAMESPACE_CIDR_IP_PREFIX: properties.Schema(
                    properties.Schema.STRING,
                    _('NAMESPACE_CIDR_IP_PREFIX.'),
                    update_allowed=True,
                    required=False,
                ),
                NAMESPACE_CIDR_IP_PREFIX_LEN: properties.Schema(
                    properties.Schema.INTEGER,
                    _('NAMESPACE_CIDR_IP_PREFIX_LEN.'),
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
        NAMESPACE_CIDR: attributes.Schema(
            _('NAMESPACE_CIDR.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
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

        obj_0 = vnc_api.Namespace(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.NAMESPACE_CIDR) is not None:
            obj_1 = vnc_api.SubnetType()
            if self.properties.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX) is not None:
                obj_1.set_ip_prefix(self.properties.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX))
            if self.properties.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX_LEN) is not None:
                obj_1.set_ip_prefix_len(self.properties.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX_LEN))
            obj_0.set_namespace_cidr(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))

        try:
            obj_uuid = super(ContrailNamespace, self).resource_create(obj_0)
        except:
            raise Exception(_('namespace %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().namespace_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('namespace %s not found.') % self.name)

        if prop_diff.get(self.NAMESPACE_CIDR) is not None:
            obj_1 = vnc_api.SubnetType()
            if prop_diff.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX) is not None:
                obj_1.set_ip_prefix(prop_diff.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX))
            if prop_diff.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX_LEN) is not None:
                obj_1.set_ip_prefix_len(prop_diff.get(self.NAMESPACE_CIDR, {}).get(self.NAMESPACE_CIDR_IP_PREFIX_LEN))
            obj_0.set_namespace_cidr(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))

        try:
            self.vnc_lib().namespace_update(obj_0)
        except:
            raise Exception(_('namespace %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().namespace_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('namespace %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().namespace_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Namespace': ContrailNamespace,
    }
