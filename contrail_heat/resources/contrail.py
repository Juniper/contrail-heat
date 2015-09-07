import ConfigParser

from cfgm_common import exceptions as cfgm_exp
from heat.engine import resource
from heat.engine.properties import Properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailResource(resource.Resource):
    _DEFAULT_USER = 'admin'
    _DEFAULT_PASSWD = 'contrail123'
    _DEFAULT_TENANT = 'admin'
    _DEFAULT_API_SERVER = '127.0.0.1'
    _DEFAULT_API_PORT = '8082'
    _DEFAULT_BASE_URL = '/'
    _DEFAULT_AUTH_HOST = '127.0.0.1'

    def __init__(self, name, json_snippet, stack):
        super(ContrailResource, self).__init__(name, json_snippet, stack)
        cfg_parser = ConfigParser.ConfigParser()
        cfg_parser.read("/etc/heat/heat.conf")
        self._user = self._read_cfg(cfg_parser,
                                    'clients_contrail',
                                    'user',
                                    self._DEFAULT_USER)
        self._passwd = self._read_cfg(cfg_parser,
                                      'clients_contrail',
                                      'password',
                                      self._DEFAULT_PASSWD)
        self._tenant = self._read_cfg(cfg_parser,
                                      'clients_contrail',
                                      'tenant',
                                      self._DEFAULT_TENANT)
        self._api_server_ip = self._read_cfg(cfg_parser,
                                             'clients_contrail',
                                             'api_server',
                                             self._DEFAULT_API_SERVER)
        self._api_server_port = self._read_cfg(cfg_parser,
                                               'clients_contrail',
                                               'api_port',
                                               self._DEFAULT_API_PORT)
        self._api_base_url = self._read_cfg(cfg_parser,
                                            'clients_contrail',
                                            'api_base_url',
                                            self._DEFAULT_BASE_URL)
        self._auth_host_ip = self._read_cfg(cfg_parser,
                                            'clients_contrail',
                                            'auth_host_ip',
                                            self._DEFAULT_AUTH_HOST)
        self._vnc_lib = None

    @staticmethod
    def _read_cfg(cfg_parser, section, option, default):
        try:
            val = cfg_parser.get(section, option)
        except (AttributeError,
                ConfigParser.NoOptionError,
                ConfigParser.NoSectionError):
            val = default

        return val

    def _show_resource(self):
        return {}

    def prepare_update_properties(self, json_snippet):
        '''
        Removes any properties which are not update_allowed, then processes
        as for prepare_properties.
        '''
        p = Properties(self.properties_schema,
                       json_snippet.get('Properties', {}),
                       self._resolve_runtime_data,
                       self.name,
                       self.context)
        props = dict((k, v) for k, v in p.items()
                     if p.props.get(k).schema.update_allowed)
        return props

    def _resolve_attribute(self, name):
        try:
            attributes = self._show_resource()
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_("Attribute %s not found in %s.") % (name, self.name))
            return None
        if name == 'show':
            return attributes
        return attributes.get(name)

    @staticmethod
    def _ignore_not_found(ex):
        if not isinstance(ex, cfgm_exp.NoIdError):
            raise ex

    def vnc_lib(self):
        if self._vnc_lib is None:
            self._vnc_lib = vnc_api.VncApi(self._user,
                                           self._passwd,
                                           self._tenant,
                                           self._api_server_ip,
                                           self._api_server_port,
                                           self._api_base_url,
                                           auth_host=self._auth_host_ip)
        return self._vnc_lib
