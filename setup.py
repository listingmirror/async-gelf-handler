#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='graypy',
    version='0.1.1',
    description="An async wrapper around the GELF (Graylog Extended Log Format).",
    long_description=open('README.rst').read(),
    keywords='logging gelf graylog2 graylog async',
    author='Developer',
    author_email='developer@listingmirror.com',
    url='https://github.com/listingmirror/async-gelf-handler',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['graypy>=0.2.13.2'],
    classifiers=['License :: OSI Approved :: BSD License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3'],
)