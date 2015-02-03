#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

from setuptools import setup, find_packages
import glob, os

def get_files(source, target):
    files = filter(lambda x: '__init__.py' not in x, glob.glob(source+'/*'))
    return (target, files)

def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

setup(
    name='contrail_heat',
    version='0.1.dev0',
    packages=find_packages(),
    package_data={'': ['*.env', '*.yaml', '*.xml']},
    zip_safe=False,
    long_description="Contrail heat resources and templates",

    install_requires=requirements('requirements.txt'),
    data_files=[get_files('contrail_heat/resources', '/usr/lib/heat/resources'),
                get_files('contrail_heat/template', '/usr/lib/heat/template'),
                get_files('contrail_heat/env', '/usr/lib/heat/env')]
)
