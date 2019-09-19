#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import io

{% if cookiecutter.readme_format == 'Markdown' -%}
with io.open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()
{%- endif -%}
{% if cookiecutter.readme_format == 'reStructuredText' -%}
with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()
{%- endif %}

setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    description=('{{cookiecutter.project_short_description}}'),
    {%- if cookiecutter.readme_format == 'Markdown' %}
    long_description=readme,
    long_description_content_type='text/markdown',
    {%- endif %}
    {%- if cookiecutter.readme_format == 'reStructuredText' %}
    long_description=readme,
    long_description_content_type='text/x-rst',
    {%- endif %}
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    {%- if cookiecutter.vcs == 'Gitlab' %}
    url='https://gitlab.com/{{cookiecutter.vcs_username}}/{{cookiecutter.project_slug}}',
    {%- elif cookiecutter.vcs == 'Github' %}
    url='https://github.com/{{cookiecutter.vcs_username}}/{{cookiecutter.project_slug}}',
    {%- elif cookiecutter.vcs == 'Bitbucket' %}
    url='https://bitbucket.org/{{cookiecutter.vcs_username}}/{{cookiecutter.project_slug}}',
    {%- endif %}
    include_package_data=True,

    python_requires='>={{cookiecutter.minimum_python_version}}, <={{cookiecutter.maximum_python_version}}',
    install_requires=[
    ],
    {%- if cookiecutter.license == 'Apache Software License 2.0' %}
    license='Apache Software License 2.0',
    {%- elif cookiecutter.license == 'BSD-3' %}
    license='BSD 3-Clause License',
    {%- elif cookiecutter.license == 'GNU GPL v3.0' %}
    license='GNU GPL v3.0',
    {%- elif cookiecutter.license == 'MIT' %}
    license='MIT',
    {%- elif cookiecutter.license == 'unlicensed' %}
    license='Unlicensed',
    {%- endif %}
    license_file='LICENSE',
    zip_safe=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        {%- if cookiecutter.license == 'Apache Software License 2.0' %}
        'License :: OSI Approved :: Apache Software License',
        {%- elif cookiecutter.license == 'BSD-3' %}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.license == 'GNU GPL v3.0' %}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        {%- elif cookiecutter.license == 'MIT' %}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == 'unlicensed' %}
        'License :: Public Domain',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python',
        {% if cookiecutter.minimum_python_version |float <= 2.7 < cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        {% endif -%}
        'Programming Language :: Python :: 3',
        {% if cookiecutter.minimum_python_version |float <= 3.2 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.2',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.3 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.3',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.4 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.4',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.5 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.5',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.6 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.6',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.6 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.7',
        {% endif -%}
        {% if cookiecutter.minimum_python_version |float <= 3.8 <= cookiecutter.maximum_python_version |float -%}
        'Programming Language :: Python :: 3.8',
        {% endif -%}
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    platforms=[
        'Any'
    ],
    keywords=(
        'python',
        'python3',
    ),
)
