#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

from setuptools import setup, find_packages
import glob, os

def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

setup(
    name='contrail_heat',
    version='0.1dev',
    packages=find_packages(),
    package_data={'': ['*.env', '*.yaml', '*.xml']},
    zip_safe=False,
    long_description="Contrail heat resources and templates",

    install_requires=requirements('requirements.txt'),
)
