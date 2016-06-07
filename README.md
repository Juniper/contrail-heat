contrail-heat
=============
Opencontrail heat plugin, resources and templates

In Release 2.x, we supported a few contrail heat resources which were
hand coded.

The R2.x Heat Plugin Resources
------------------------------
Here is the link of all the hand-written plugin resources supported by
contrail-heat in Release 2.x

https://github.com/Juniper/contrail-heat/tree/master/contrail_heat/resources

With Release 3.0, contrail-heat resources/templates are being auto-generated
from the Schema. 

The generated resources/templates are part of the python-contrail package
and located in /usr/lib/python2.7/dist-packages/vnc_api/gen/heat/
directory in the target installation. This directory has three sub-directories

1. resources/ 
   This sub-directory contains all the resources for the contrail-heat plugin.
   It runs in the context of the heat-engine service.
2. templates/
   This sub-directory contains template for each resource. They are sample
   templates with every possible parameter in the schema. They should be used
   as a reference when you build up more complex templates for your network
   design.
3. env/
   This sub-directories contains environment for input to each template.

The Heat Plugin Resources
-------------------------
Here is the link of all the generated plugin resources supported by
contrail-heat in Release 3.x

https://github.com/Juniper/contrail-heat/tree/master/generated/resources

