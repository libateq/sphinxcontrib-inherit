#!/usr/bin/env python3
# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from re import compile, match
from os.path import dirname, join
from setuptools import setup, find_packages


def read(fname):
    with open(join(dirname(__file__), fname), 'r', encoding='utf-8') as file:
        return file.read()


def version(fname):
    regex = compile("^version[^0-9]*([0-9A-Za-z_.-]*)")
    filename = join(dirname(__file__), fname, '__init__.py')
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            version = match(regex, line)
            if version:
                return version.group(1)


setup(
    name='sphinxcontrib-inherit',
    version=version('sphinxcontrib/inherit'),
    description=(
        "A Sphinx extension that allows documentation to be created in a "
        "modular way."),
    long_description=read('README.rst'),
    author='David Harper',
    author_email='python-packages@libateq.org',
    url='https://bitbucket.org/libateq/sphinxcontrib-inherit',
    project_urls={
        "Bug Tracker": (
            'https://bitbucket.org/libateq/sphinxcontrib-inherit/issues'),
        "Documentation": 'https://sphinxcontrib-inherit.readthedocs.org/',
        "Source Code": 'https://bitbucket.org/libateq/sphinxcontrib-inherit',
    },
    keywords='sphinx inherit modular documentation',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    license='GPL-3',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['sphinxcontrib'],
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[
        'Sphinx>=2.0.0',
        'docpath>=0.1.1',
    ],
    zip_safe=False,
)
