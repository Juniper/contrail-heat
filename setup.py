#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

from setuptools import setup, find_packages

def requirements(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

setup(
    name='heat_contrail',
    version='0.1dev',
    packages=find_packages(),
    package_data={'': ['*.html', '*.css', '*.xml']},
    zip_safe=False,
    long_description="Contrail heat resources and templates",

    install_requires=requirements('requirements.txt'),
)
