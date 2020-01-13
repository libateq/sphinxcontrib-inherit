Usage
=====

The purpose of the *sphinxcontrib-inherit* extension is to allow content from
modular documentation to be included in the generated documentation based
on what modules in a related system are activated.  Sphinx can be configured to
process the content from a selected subset of module directories.  Any
inherited content in these module directories is then extracted from the
documents it is defined in, and inserted into another document at a specified
position relative to a target node.

The inheritance process is applied to the documents in the same order as the
modules are listed in the ``inherit_modules`` configuration option.  If
correctly setup this enables modules to update documentation that has been
changed by, or defined by, other modules.


Configuration
-------------

To use the *sphinxcontrib-inherit* extension it needs to be enabled in your
project's ``conf.py`` file.  This is done by adding it to the list of enabled
extensions.

.. code-block:: python3

    extensions = ['sphinxcontrib.inherit']

Options
^^^^^^^

The *sphinxcontrib-inherit* extension adds several new configuration options
that can be used in the ``conf.py`` file.  These options are used to change
how the extension behaves, and thus ultimately change what documentation is
generated.

**inherit_modules_dir**
    The directory that contains each module's documentation, relative to the
    source directory.  The documentation for each module should be placed in
    its own directory.
    The default value is ``''``, which means the module directories should be
    located directly inside the source directory.

    Example:

    .. code-block:: python3

        inherit_modules_dir = 'modules'

**inherit_modules**
    A list of the modules that should be processed and included in the
    generated documentation.  This can also be a function that returns a
    list of modules and has the signature ``inherit_modules(app, config)``.
    The names used here for the modules should match the names of the
    directories in which the module's documentation can be found.
    The default value is ``None``, which includes none of the modules in the
    generated documentation.

    Examples:

    .. code-block:: python3

        inherit_modules = ['module1', 'module2', 'module3']

    .. code-block:: python3

        def inherit_modules_function(app, config):
            return ['module1', 'module2', 'module3']

        inherit_modules = inherit_modules_function


Directives
----------

This extension adds a new directive that is used to mark the parts of
documentation that should be inherited, and where and how these inherited parts
should be re-inserted.

**.. inherit::** *position* *target*
    The ``inherit`` directive is used immediately before any section or element
    that should be inherited.  It takes two required arguments that specify
    where and how the inheritance should be applied, and some options that
    enable this process to be adjusted.

    *position*
        This argument specifies where the inherited nodes should be re-inserted
        relative to the target node.

        * *before*: The inherited nodes are re-inserted into the document
          immediately before the target node.
        * *after*: The inherited nodes are re-inserted into the document
          immediately after the target node.
        * *inside*: The inherited nodes are placed inside the target node.
        * *hide*: The target node is hidden.  Unlike the other inherit
          directives any section or element that follows this directive is not
          normally captured and extracted.

    *target*
        This argument is a docpath_ that specifies which node the inherited
        nodes should be positioned relative to.  It can also optionally
        specify the document that the target node must appear in.

        It should be in the form: ``docpath``, or to only match nodes in a
        specific document: ``path/to/document,docpath``.

        .. _docpath: https://docpath.readthedocs.org/

    *:filter: docpath*
        This option is a docpath_ and it alters which nodes get inserted into
        the target document. Sections or elements are extracted as normal from
        the document that they are defined in.  However only nodes (and all
        their children) that match the ``docpath`` get inserted into the
        target document.  This is useful for doing things like inheriting just
        the items from a list instead of the list itself. The ``docpath``
        should be a path relative to the inherit node.

        .. _docpath: https://docpath.readthedocs.org/

    *:index: num*
        When using the ``inside`` *position*, this option allows you to specify
        at what index the inherited nodes should be inserted.  The children of
        the target node are numbered starting at 0.  The inherited nodes are
        inserted immediately before the node at the indexed location.  Negative
        numbers are relative to the end of the list of children.  If this
        option is not provided, or is set to ``end``, then the inherited nodes
        are appended to the end of the list.

    *:quantity: num*
        This option allows you to specify the number of sections or elements
        to extract with the inherit directive.  All the sections or elements
        must be part of the same section and must be at the same level of the
        document as the first.  The default depends on the *position* and is
        normally ``1``, except for the ``hide`` *position* which has a default
        of ``0``.  A value of ``all`` will extract all the elements that are
        at the same level and in the same section as the first.
