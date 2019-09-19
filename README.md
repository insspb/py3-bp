# Python 3 boilerplate template

[![docs](https://readthedocs.org/projects/py3-bp/badge/?version=latest)](https://readthedocs.org/projects/py3-bp/?badge=latest)
[![build](https://img.shields.io/travis/insspb/py3-bp.svg)](https://travis-ci.org/insspb/py3-bp)

As a [freelancer](https://www.upwork.com/fl/andreyshpak) I often require
to do small projects on python. As any developer I do not like to do same
boilerplate work each time, but I like to work in expected environment.
So I decided to make this small project and include everything I often
need in one place.

This project for small non-web projects.

Project is under development. Unreleased features available at master branch.
Most fresh changes data available in [CHANGELOG](CHANGELOG.md)

## Current project features

* Readme file generation for new projects. Available formats: `Markdown`
or `reStructuredText`
* Authors file generation for new projects. Available formats: `Markdown`
or `reStructuredText`
* Changelog file generation for new projects. Available formats: `Markdown`
or `reStructuredText`
* License file generation for new projects. Generated as `LICENSE` in root
folder and as `reStructuredText` in `docs` folder.
 Available licenses:
  * MIT
  * BSD-3
  * GNU GPL v3.0
  * Apache Software License 2.0
  * unlicensed (Public domain)
* Sphinx doc folder and project generation. Configured for separated `source`
and `build` folders.
* `setup.py` and `setup.cfg` generation.
* `requirements.txt` and `requirements.dev` generation based on template
choices.

## Usage

Single time usage example, requires installation of
[Cookiecutter](https://github.com/cookiecutter/cookiecutter):

```bash
cookiecutter https://github.com/insspb/py3-bp
```

## Roadmap

* Include pytest sample tests if pytest enabled
* Include tox sample configuration files
* Include nox sample configuration files
* Include Alembic sample configuration files
* Include Travis CI sample configuration files
* Include Gitlab CI sample configuration files
* Include AppVeyor CI sample configuration files

Currently this project is in 'I have an idea' stage.

## Project python version

This project is developed and tested on python version 3.6 and python 3.7, but
should work under any python 3.2+.
