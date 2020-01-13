Documentation Inheritance for Sphinx
====================================

The *sphinxcontrib-inherit* package is an extension to Sphinx_.  It allows you
to extend existing sphinx documentation without needing to add any directives
or hooks to the original document.  It is ideal for use in projects that make
extensive use of pluggable modules, and require different documentation to be
generated depending on which modules are enabled.

This extension was inspired by the sphinxcontrib-inheritance_ package, but
takes a different approach on how the inheritance is implemented.

.. _Sphinx: http://www.sphinx-doc.org/
.. _sphinxcontrib-inheritance: https://bitbucket.org/nantic/sphinxcontrib-inheritance

.. start-of-readme-only-text

Installation
============

.. code:: python

    pip3 install sphinxcontrib-inherit
