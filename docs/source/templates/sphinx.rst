Sphinx documentation engine template
====================================

*Implemented in 0.0.4*

During project generation you will be asked about installation of basic Sphinx
documentation template. Question:

- Use Sphinx documentation?

Default answer is ``yes`` and by default ``docs`` folder and related entries to
``requirements.dev`` will be created.

Selection of this option will add dependency for following list of packages:

- ``sphinx`` - basic Sphinx engine
- ``sphinx-rtd-theme`` - my theme of preference to use with docs engine
- ``doc8`` - RST files style checker
- ``recommonmark`` - plugin, that allow usage of ``Markdown`` files in Sphinx
  documentation

Included configuration accept ``docs/source`` folder of new project as
documentation source, and will place generated docs to ``docs/build`` folder.

Based on other questions on installation stage following files will be included
in default documentation:

- README
- CHANGELOG
- AUTHORS
- LICENSE

You can generate docs and check them before initial push with following
commands sequence:

.. code-block:: bash

    pip install -r requirements.dev
    cd docs
    make html

Then open ``build/html/index.html`` file with your favorite browser.
