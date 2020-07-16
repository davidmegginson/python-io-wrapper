#!/usr/bin/python

from setuptools import setup
import sys

if sys.version_info < (3,):
    raise RuntimeError("Requires Python 3 or higher")

setup(
    name='python-io-wrapper',
    version='0.2',
    description='IO wrapper to add missing methods from io.BaseIO',
    author='David Megginson',
    author_email='contact@megginson.io',
    packages=['io_wrapper'],
    test_suite='tests'
)
