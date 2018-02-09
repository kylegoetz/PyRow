#!/usr/bin/env python

from setuptools import setup

setup(name='PyRow',
    version='0.1',
    description='Module for interfacing with Concept2 PM3/PM4 monitors',
    packages=['pyrow'],
    install_requires=['pyusb', 'future']
)
