Installation
============


Prerequisites
-------------

* Python 3.5 or later (http://www.python.org/)
* See the ``setup.py`` file for python package dependencies.


Using pip
---------

The easiest way to install this extension and it's dependencies is directly
from the Python Package Index:

.. code-block:: bash

    pip3 install sphinxcontrib-inherit


Using Sources
-------------

Alternatively, you can clone the *sphinxcontrib-inherit* repository, and
install the extension from there:

.. code-block:: bash

    git clone https://bitbucket.org/libateq/sphinxcontrib-inherit
    cd sphinxcontrib-inherit
    python3 setup.py install


Other Information
-----------------

You may need administrator/root privileges to perform the installation, as the
install commands will by default attempt to install the extension to the
system wide Python site-packages directory on your system.

For advanced options, please refer to the easy_install and/or the distutils
documentation:

* https://docs.python.org/3/installing/index.html
* http://peak.telecommunity.com/DevCenter/EasyInstall
