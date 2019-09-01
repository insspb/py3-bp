#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.authors_format }}' == 'Markdown':
        remove_file('AUTHORS.rst')
        remove_file('docs/AUTHORS.rst')
    elif '{{ cookiecutter.authors_format }}' == 'Rest':
        remove_file('AUTHORS.md')
        remove_file('docs/AUTHORS.md')
    else:
        remove_file('AUTHORS.rst')
        remove_file('docs/AUTHORS.rst')
        remove_file('AUTHORS.md')
        remove_file('docs/AUTHORS.md')

    if '{{ cookiecutter.readme_format }}' == 'Markdown':
        remove_file('README.rst')
        remove_file('docs/README.rst')
    elif '{{ cookiecutter.readme_format }}' == 'Rest':
        remove_file('README.md')
        remove_file('docs/README.md')
    else:
        remove_file('README.rst')
        remove_file('docs/README.rst')
        remove_file('README.md')
        remove_file('docs/README.md')

    if '{{ cookiecutter.history_format }}' == 'Markdown':
        remove_file('HISTORY.rst')
        remove_file('docs/HISTORY.rst')
    elif '{{ cookiecutter.history_format }}' == 'Rest':
        remove_file('HISTORY.md')
        remove_file('docs/HISTORY.md')
    else:
        remove_file('HISTORY.rst')
        remove_file('docs/HISTORY.rst')
        remove_file('HISTORY.md')
        remove_file('docs/HISTORY.md')

    if '{{ cookiecutter.changelog_format }}' == 'Markdown':
        remove_file('CHANGELOG.rst')
        remove_file('docs/CHANGELOG.rst')
    elif '{{ cookiecutter.changelog_format }}' == 'Rest':
        remove_file('CHANGELOG.md')
        remove_file('docs/CHANGELOG.md')
    else:
        remove_file('CHANGELOG.rst')
        remove_file('docs/CHANGELOG.rst')
        remove_file('CHANGELOG.md')
        remove_file('docs/CHANGELOG.md')

    if '{{ cookiecutter.license }}' == 'None':
        remove_file('LICENSE')
        remove_file('docs/license.rst')
