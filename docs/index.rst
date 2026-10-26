Python Amazon Advertising API documentation
===========================================

This project helps you using python 3.8 to use the *Python Amazon Advertising API*.


.. toctree::
   :maxdepth: 1
   
   installation
   credentials
   v1
   v0
   api
   api/attribution
   api/brand_metrics
   api/advertising_test_account
   disclaimer


.. note::
   The Sponsored Brands 4.0 contract is covered end to end, including budget
   rules, optimization rules, targeting categories, migration and the collection
   creatives. The 3.0 campaigns and ad groups remain only as reference: Amazon
   answers ``403 Endpoint has been deprecated`` and points to 4.0.

.. note::
   Most per-product routes take a versioned media type and the service routes on
   it. Sending ``application/json`` where a versioned type is expected answers
   ``404 Could not find resource``, which reads like a missing route but is only
   the wrong media type.

.. literalinclude:: example.py
