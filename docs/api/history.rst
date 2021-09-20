History
=================

.. autoclass:: ad_api.api.History
    :members:

### Example python

.. code-block:: python

    file = open("query.json")
    data = file.read()
    file.close()

    res = History().get_history(
        body=data
    )

### Example query.json

.. literalinclude:: ../../test/history/query.json