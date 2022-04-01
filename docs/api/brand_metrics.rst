Brand Metrics API open beta
===========================

.. autoclass:: ad_api.api.BrandMetrics

.. autofunction:: ad_api.api.BrandMetrics.post_report

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("query_taxonomy.json")
    data = file.read()
    file.close()

    Localization().get_currency(
        body=data
    )

### Example query_taxonomy.json

.. literalinclude:: ../../test/audiences/query_taxonomy.json

.. autofunction:: ad_api.api.BrandMetrics.get_report

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("query_general.json")
    data = file.read()
    file.close()

    Localization().get_products(
        body=data
    )

### Example query_general.json

.. literalinclude:: ../../test/audiences/query_general.json
