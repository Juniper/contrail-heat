import ConfigParser

from vnc_api.vnc_api import *
from heat.engine.resources.neutron import neutron

def _read_cfg(cfg_parser, section, option, default):
        try:
            val = cfg_parser.get(section, option)
        except (AttributeError,
                ConfigParser.NoOptionError,
                ConfigParser.NoSectionError):
            val = default

        return val
#end _read_cfg

class ContrailResource(neutron.NeutronResource):
    _DEFAULT_USER = "admin"
    _DEFAULT_PASSWD = 'contrail123'
    _DEFAULT_TENANT = "admin"
    _DEFAULT_API_SERVER = "127.0.0.1"
    _DEFAULT_BASE_URL = "/"

    def __init__(self, name, json_snippet, stack):
        try:
            if stack.clients._vnc_lib:
                pass
        except:
            cfg_parser = ConfigParser.ConfigParser()
            cfg_parser.read("/etc/heat/heat.conf")
            self._user = _read_cfg(cfg_parser, 'clients_contrail', 'user', self._DEFAULT_USER)
            self._passwd = _read_cfg(cfg_parser, 'clients_contrail', 'password', self._DEFAULT_PASSWD)
            self._tenant = _read_cfg(cfg_parser, 'clients_contrail', 'tenant', self._DEFAULT_TENANT)
            self._api_server_ip = _read_cfg(cfg_parser, 'clients_contrail', 'api_server', self._DEFAULT_API_SERVER)
            self._api_base_url = _read_cfg(cfg_parser, 'clients_contrail', 'api_base_url', self._DEFAULT_BASE_URL)

            stack.clients._vnc_lib = VncApi(self._user ,self._passwd ,self._tenant, self._api_server_ip, "8082", self._api_base_url)

        super(ContrailResource, self).__init__(name, json_snippet, stack)

    def vnc_lib(self):
	return self.stack.clients._vnc_lib
    # end vnc_lib
