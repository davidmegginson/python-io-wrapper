#!/usr/bin/python

from setuptools import setup
import sys

if sys.version_info < (3,):
    raise RuntimeError("Requires Python 3 or higher")

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-io-wrapper',
    version='0.3.1',
    description='IO wrapper to add missing methods from io.BaseIO',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    author='David Megginson',
    author_email='contact@megginson.io',
    packages=['io_wrapper'],
    test_suite='tests'
)
