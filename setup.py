#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import io


with io.open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='py3-bp',
    version='0.0.4',
    description=('Ultimate template for new Python 3 projects'),
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Andrey Shpak',
    author_email='ashpak@ashpak.ru',
    url='https://github.com/insspb/py3-bp',
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[
        'cookiecutter'
    ],
    license='MIT',
    license_file='LICENSE',
    zip_safe=True,
    project_urls={
        "Bug Tracker": "https://github.com/insspb/py3-bp/issues",
        "Documentation": "https://py3-bp.readthedocs.io",
        "Source Code": "https://github.com/insspb/py3-bp",
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Framework :: Sphinx',
        'Framework :: tox',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Documentation',
        'Topic :: Education',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities'
    ],
    platforms=[
        'Any'
    ],
    keywords=(
        'cookiecutter',
        'python',
        'python3',
        'boilerplate',
        'boilerplate-template',
        'template',
        'skeleton',
        'scaffolding',
        'scaffoldings',
        'scaffolding-framework',
        'skeleton-template',
        'skeleton-application',
        'utilities'
    ),
)
