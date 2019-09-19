# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com),
and this project adheres to [Semantic versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

Unreleased features are usually available in HEAD master branch.

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
and `build` folders. Cannot be switched off at this moment.
* `setup.py` and `setup.cfg` generation. Files will work, but some adjustment
required if you want to use them on pypi. Not all planned features included.
* `requirements.txt` and `requirements.dev` generation based on template
choices.
