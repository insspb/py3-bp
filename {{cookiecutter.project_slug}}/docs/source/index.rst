.. python3-boilerplate documentation master file, created by
   sphinx-quickstart on Sat Aug 31 08:08:04 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{cookiecutter.project_name}}'s documentation!
============================================================================================

.. toctree::
   :maxdepth: 1
{% if cookiecutter.readme_format == 'Markdown' %}
   Overview <README.md>
{%- endif %}
{%- if cookiecutter.readme_format == 'reStructuredText' %}
   Overview <README.rst>
{%- endif %}
{%- if cookiecutter.authors_format == 'Markdown' %}
   Authors <AUTHORS.md>
{%- endif %}
{%- if cookiecutter.authors_format == 'reStructuredText' %}
   Authors <AUTHORS.rst>
{%- endif %}
{%- if cookiecutter.changelog_format == 'Markdown' %}
   Changelog <CHANGELOG.md>
{%- endif %}
{%- if cookiecutter.changelog_format == 'reStructuredText' %}
   Changelog <CHANGELOG.rst>
{%- endif %}
{%- if cookiecutter.license != 'None' %}
   license
{% endif %}