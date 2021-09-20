Audiences
============

.. autoclass:: ad_api.api.Audiences

.. autofunction:: ad_api.api.Audiences.list_audiences_taxonomy

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

.. autofunction:: ad_api.api.Audiences.list_audiences

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
