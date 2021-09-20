Localization
============

.. autoclass:: ad_api.api.Localization

.. autofunction:: ad_api.api.Localization.get_currency

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("currency.json")
    data = file.read()
    file.close()

    Localization().get_currency(
        body=data
    )

### Example currency.json

.. literalinclude:: ../../test/localizations/currency.json

.. autofunction:: ad_api.api.Localization.get_products

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("products.json")
    data = file.read()
    file.close()

    Localization().get_products(
        body=data
    )

### Example products.json

.. literalinclude:: ../../test/localizations/products.json


.. autofunction:: ad_api.api.Localization.get_keywords

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("products.json")
    data = file.read()
    file.close()

    Localization().get_keywords(
        body=data
    )

### Example products.json

.. literalinclude:: ../../test/localizations/keywords.json

.. autofunction:: ad_api.api.Localization.get_targeting_expression

### Example python

.. code-block:: python

    from ad_api.api.localization import Localization

    file = open("targeting_expression.json")
    data = file.read()
    file.close()

    Localization().get_targeting_expression(
        body=data
    )

### Example products.json

.. literalinclude:: ../../test/localizations/targeting_expression.json

