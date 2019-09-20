#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath), ignore_errors=False, onerror=None)


if __name__ == '__main__':

    if '{{ cookiecutter.authors_format }}' == 'Markdown':
        remove_file('AUTHORS.rst')
        remove_file('docs/source/AUTHORS.rst')
    elif '{{ cookiecutter.authors_format }}' == 'reStructuredText':
        remove_file('AUTHORS.md')
        remove_file('docs/source/AUTHORS.md')
    else:
        remove_file('AUTHORS.rst')
        remove_file('docs/source/AUTHORS.rst')
        remove_file('AUTHORS.md')
        remove_file('docs/source/AUTHORS.md')

    if '{{ cookiecutter.readme_format }}' == 'Markdown':
        remove_file('README.rst')
        remove_file('docs/source/README.rst')
    elif '{{ cookiecutter.readme_format }}' == 'reStructuredText':
        remove_file('README.md')
        remove_file('docs/source/README.md')

    if '{{ cookiecutter.changelog_format }}' == 'Markdown':
        remove_file('CHANGELOG.rst')
        remove_file('docs/source/CHANGELOG.rst')
    elif '{{ cookiecutter.changelog_format }}' == 'reStructuredText':
        remove_file('CHANGELOG.md')
        remove_file('docs/source/CHANGELOG.md')
    else:
        remove_file('CHANGELOG.rst')
        remove_file('docs/source/CHANGELOG.rst')
        remove_file('CHANGELOG.md')
        remove_file('docs/source/CHANGELOG.md')

    if '{{ cookiecutter.license }}' == 'None':
        remove_file('LICENSE')
        remove_file('docs/source/license.rst')

    if '{{ cookiecutter.use_sphinx_documentation }}' == 'no':
        remove_directory('docs')

    if '{{ cookiecutter.install_issues_templates }}' == 'no':
        remove_directory('.github')
        remove_directory('.gitlab')
    elif '{{ cookiecutter.install_issues_templates }}' == 'Gitlab':
        remove_directory('.github')
    elif '{{ cookiecutter.install_issues_templates }}' == 'Github':
        remove_directory('.gitlab')
