from vnc_api.vnc_api import *
from heat.engine.resources.neutron import neutron

class ContrailResource(neutron.NeutronResource):
    def __init__(self, name, json_snippet, stack):
        try:
            if stack.clients._vnc_lib:
                pass
        except:
            # TODO take parameter
            stack.clients._vnc_lib = VncApi("admin", "contrail123", "admin", "127.0.0.1", "8082", '/')
        super(ContrailResource, self).__init__(name, json_snippet, stack)

    def vnc_lib(self):
	return self.stack.clients._vnc_lib
    # end vnc_lib
