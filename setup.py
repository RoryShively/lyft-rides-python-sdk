#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='lyft_rides_hero',
    version='0.1.0',
    packages=find_packages(),
    description='Unofficial Lyft Rides API Python SDK',
    long_description=readme,
    url='https://github.com/RoryShively/lyft-rides-python-sdk',
    license='MIT',
    author='Gautam Mishra',
    author_email='gautam.mishra@hotmail.com',
    install_requires=['requests', 'pyyaml'],
    extras_require={
        ':python_version == "2.7"': ['future'],
    },
    keywords=['lyft', 'api', 'sdk', 'rides', 'library'],
)
