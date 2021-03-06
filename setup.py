#!/usr/bin/env python
from setuptools import setup

# get version
with open('oparlvalidator/version.py') as version_file:
    exec(version_file.read())

setup(
    name='oparlvalidator',
    version=__version__,
    author='OParl Consortium',
    include_package_data=True,
    extras_require=dict(
        test=[],
    ),
    install_requires=[
        'setuptools',
        'requests==2.2.1',
        'jsonschema==2.3.0',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'oparlval = oparlvalidator.cli:main'
        ]
    }
)
