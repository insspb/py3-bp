Soft links in templates
=======================

As a developer I do not like to make duplicates of same data in project.
To exclude duplicates Sphinx documentation in template use soft links to
documents located at project core directory.

By default this list of files has soft links:

- README.rst
- README.md
- CHANGELOG.rst
- CHANGELOG.md
- AUTHORS.rst
- AUTHORS.md
- HISTORY.rst
- HISTORY.md


Some soft links will be deleted after project creation.

If you choose rst format for one of document - Markdown files and links
will be removed. And vice versa. This setting works per document type.

If `None` chosen for either `README` or `CHANGELOG` corresponding files
will be removed.

By default only `README.md` will be created.

.. note:: Soft links in windows works with Windows 10 and up.
