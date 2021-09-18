.. amazon documentation master file, created by
   sphinx-quickstart on Sun Sep 12 03:03:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python Amazon Advertising Documentation
==================================================

.. toctree::
   :maxdepth: 0

   ad_api.api.sp

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


useful #2 -- explicit members
=============================

This is something I want to say that is not in the docstring.

   ::autoclass:: AdGroups
   :members: list_ad_groups_request, list_ad_groups_extended_request


.. literalinclude:: example.py
   :language: python

.. seealso::

   Module :py:mod:`zipfile`
      Documentation of the :py:mod:`zipfile` standard module.

   `GNU tar manual, Basic Tar Format <http://link>`_
      Documentation for tar archive files, including GNU tar extensions.

.. toctree::
   :maxdepth: 1

   modules
   support