# {{ cookiecutter.project_name }}

{% if cookiecutter.vcs == 'Github' %}
[![build](https://img.shields.io/travis/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }}.svg)](https://travis-ci.org/{{ cookiecutter.vcs_username }}/{{ cookiecutter.project_slug }})
{% endif -%}
[![docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest)

{{ cookiecutter.project_short_description }}

## Quickstart

This project generated from [python3-boilerplate](https://github.com/insspb/py3-bp) package.
Quick start will be filled soon.

## Examples

This project generated from [python3-boilerplate](https://github.com/insspb/py3-bp) package.
Examples will be filled soon.

## Documentation

This project generated from [python3-boilerplate](https://github.com/insspb/py3-bp) package.
Documentation will be filled soon.

## Contributing

Contributions are very welcome. Please follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).

{% if cookiecutter.license != 'None' -%}
## License
{% endif %}
{% if cookiecutter.license == 'MIT' -%}
This project distributed under **MIT license**.
{%- elif cookiecutter.license == 'BSD-3' -%}
This project distributed under **BSD-3 license**.
{%- elif cookiecutter.license == 'GNU GPL v3.0' -%}
This project distributed under **GNU GPL v3.0 license**.
{%- elif cookiecutter.license == 'Apache Software License 2.0' -%}
This project distributed under **Apache Software License 2.0**.
{%- elif cookiecutter.license == 'unlicensed' -%}
This project distributed as **public domain** software.
{%- else -%}
{% endif %}
