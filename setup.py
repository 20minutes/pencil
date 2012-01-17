# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='pencil',
    version='0.6.2',
    description='Dumb but useful wrapper around Graphite URL API.',
    author='Timothée Peignier',
    author_email='tpeignier@20minutes.fr',
    url='https://github.com/20minutes/pencil',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
