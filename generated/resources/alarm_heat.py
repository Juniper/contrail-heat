
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


class ContrailAlarm(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ALARM_SEVERITY, ALARM_RULES, ALARM_RULES_RULE, ALARM_RULES_RULE_OPERATION, ALARM_RULES_RULE_OPERAND1, ALARM_RULES_RULE_OPERAND2, ALARM_RULES_RULE_VARS, UVE_KEYS, GLOBAL_SYSTEM_CONFIG, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'alarm_severity', 'alarm_rules', 'alarm_rules_rule', 'alarm_rules_rule_operation', 'alarm_rules_rule_operand1', 'alarm_rules_rule_operand2', 'alarm_rules_rule_vars', 'uve_keys', 'global_system_config', 'project'
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
        ALARM_SEVERITY: properties.Schema(
            properties.Schema.INTEGER,
            _('ALARM_SEVERITY.'),
            update_allowed=True,
            required=False,
        ),
        ALARM_RULES: properties.Schema(
            properties.Schema.MAP,
            _('ALARM_RULES.'),
            update_allowed=True,
            required=False,
            schema={
                ALARM_RULES_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('ALARM_RULES_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ALARM_RULES_RULE_OPERATION: properties.Schema(
                                properties.Schema.STRING,
                                _('ALARM_RULES_RULE_OPERATION.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.AllowedValues([u'==', u'!=', u'<=', u'>=', u'in', u'not in']),
                                ],
                            ),
                            ALARM_RULES_RULE_OPERAND1: properties.Schema(
                                properties.Schema.STRING,
                                _('ALARM_RULES_RULE_OPERAND1.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ALARM_RULES_RULE_OPERAND2: properties.Schema(
                                properties.Schema.STRING,
                                _('ALARM_RULES_RULE_OPERAND2.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ALARM_RULES_RULE_VARS: properties.Schema(
                                properties.Schema.LIST,
                                _('ALARM_RULES_RULE_VARS.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        UVE_KEYS: properties.Schema(
            properties.Schema.STRING,
            _('UVE_KEYS.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
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
        ALARM_SEVERITY: attributes.Schema(
            _('ALARM_SEVERITY.'),
        ),
        ALARM_RULES: attributes.Schema(
            _('ALARM_RULES.'),
        ),
        UVE_KEYS: attributes.Schema(
            _('UVE_KEYS.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_system_config_read(id=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT):
            try:
                parent_obj = self.vnc_lib().project_read(id=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except:
                parent_obj = None

        if parent_obj is None:
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.Alarm(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ALARM_SEVERITY) is not None:
            obj_0.set_alarm_severity(self.properties.get(self.ALARM_SEVERITY))
        if self.properties.get(self.ALARM_RULES) is not None:
            obj_1 = vnc_api.AlarmRule()
            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE))):
                    obj_2 = vnc_api.AlarmElement()
                    if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERATION) is not None:
                        obj_2.set_operation(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERATION))
                    if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND1) is not None:
                        obj_2.set_operand1(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND1))
                    if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND2) is not None:
                        obj_2.set_operand2(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND2))
                    if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS) is not None:
                        for index_2 in range(len(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS))):
                            obj_2.add_vars(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS)[index_2])
                    obj_1.add_rule(obj_2)
            obj_0.set_alarm_rules(obj_1)
        if self.properties.get(self.UVE_KEYS) is not None:
            obj_0.set_uve_keys(self.properties.get(self.UVE_KEYS))

        try:
            obj_uuid = super(ContrailAlarm, self).resource_create(obj_0)
        except:
            raise Exception(_('alarm %s could not be updated.') % self.name)

        self.resource_id_set(obj_uuid)

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().alarm_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('alarm %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ALARM_SEVERITY) is not None:
            obj_0.set_alarm_severity(prop_diff.get(self.ALARM_SEVERITY))
        if prop_diff.get(self.ALARM_RULES) is not None:
            obj_1 = vnc_api.AlarmRule()
            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE))):
                    obj_2 = vnc_api.AlarmElement()
                    if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERATION) is not None:
                        obj_2.set_operation(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERATION))
                    if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND1) is not None:
                        obj_2.set_operand1(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND1))
                    if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND2) is not None:
                        obj_2.set_operand2(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_OPERAND2))
                    if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS) is not None:
                        for index_2 in range(len(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS))):
                            obj_2.add_vars(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_RULE, {})[index_1].get(self.ALARM_RULES_RULE_VARS)[index_2])
                    obj_1.add_rule(obj_2)
            obj_0.set_alarm_rules(obj_1)
        if prop_diff.get(self.UVE_KEYS) is not None:
            obj_0.set_uve_keys(prop_diff.get(self.UVE_KEYS))

        try:
            self.vnc_lib().alarm_update(obj_0)
        except:
            raise Exception(_('alarm %s could not be updated.') % self.name)

    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().alarm_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('alarm %s already deleted.') % self.name)

    def _show_resource(self):
        obj = self.vnc_lib().alarm_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Alarm': ContrailAlarm,
    }
