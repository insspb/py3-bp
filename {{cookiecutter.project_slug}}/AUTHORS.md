# Authors
{%- if cookiecutter.vcs == 'Gitlab' %}
{% set link = 'https://gitlab.com/' %}
{% elif cookiecutter.vcs == 'Github' %}
{% set link = 'http://github.com/' %}
{% elif cookiecutter.vcs == 'Bitbucket' %}
{% set link = 'https://bitbucket.org/' %}
{% endif -%}

This project is inspired and made by:

## Development Leads

* {{ cookiecutter.author }} ([@{{cookiecutter.vcs_username}}]({{ link }}{{ cookiecutter.vcs_username }}))

## Core Committers

* You name can be here

## Contributors

* You name can be here
