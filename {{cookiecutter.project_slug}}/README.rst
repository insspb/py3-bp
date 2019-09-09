{{ cookiecutter.project_name }}
===============================

{% if cookiecutter.vcs == 'Github' %}
.. image:: https://img.shields.io/travis/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}
{% endif -%}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest


{{ cookiecutter.project_short_description }}

Quickstart
----------

This project generated from `python3-boilerplate<https://github.com/insspb/py3-bp>`_ package.
Quick start will be filled soon.

Examples
--------

This project generated from `python3-boilerplate<https://github.com/insspb/py3-bp>`_ package.
Examples will be filled soon.

Documentation
-------------

This project generated from `python3-boilerplate<https://github.com/insspb/py3-bp>`_ package.
Documentation will be filled soon.

Contributing
------------

Contributions are very welcome. Please follow the `PyPA Code of Conduct<https://www.pypa.io/en/latest/code-of-conduct/>`_.

{% if cookiecutter.license != 'None' -%}
License
-------
{% endif %}
{% if cookiecutter.license == 'MIT' -%}
This project distributed under `MIT license<LICENSE>`_.
{%- elif cookiecutter.license == 'BSD-3' -%}
This project distributed under `BSD-3 license<LICENSE>`_.
{%- elif cookiecutter.license == 'GNU GPL v3.0' -%}
This project distributed under `GNU GPL v3.0 license<LICENSE>`_.
{%- elif cookiecutter.license == 'Apache Software License 2.0' -%}
This project distributed under `Apache Software License 2.0<LICENSE>`_.
{%- elif cookiecutter.license == 'unlicensed' -%}
This project distributed as `public domain<LICENSE>`_ software.
{%- else -%}
{% endif %}
