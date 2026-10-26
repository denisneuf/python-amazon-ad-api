Change History
==============
`https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json`_

.. _https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/Changehistory_prod_3p.json

Provides information about changes made to campaigns, ad groups, ads and the
rest of the entity tree.

.. autoclass:: ad_api.api.History
    :members:

    .. note::

        The contract is version 3.0 and carries no beta marker: no ``x-beta``,
        no ``x-amz-*``, no deprecation notice. The page is listed as stable
        because of that.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
         - Answer
       * - ``POST /history``
         - ``get_history``
         - ``vnd.historyresponse.v1.0``
         - ``200``
       * - ``POST /history`` with ``version="1.1"``
         - ``get_history``
         - ``vnd.historyresponse.v1.1``
         - ``200``

    The second row is the same route. ``THEME`` is the only event type that
    needs version 1.1; at 1.0 the service answers ``400`` and names it.

    ### Event types

    .. list-table::
        :header-rows: 1

       * - Type
         - Version needed
       * - ``AD``
         - 1.0
       * - ``AD_GROUP``
         - 1.0
       * - ``CAMPAIGN``
         - 1.0
       * - ``KEYWORD``
         - 1.0
       * - ``NEGATIVE_KEYWORD``
         - 1.0
       * - ``PRODUCT_TARGETING``
         - 1.0
       * - ``THEME``
         - 1.1

    ### Request body

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``fromDate``
         - integer
         - Required. Epoch in **milliseconds**. At most 90 days back, counted
           from the moment of the request.
       * - ``toDate``
         - integer
         - Required. Epoch in milliseconds.
       * - ``eventTypes``
         - object
         - Required. One or more of the types above, each carrying an object,
           usually ``{}`` or ``{"filters": [...]}``.
       * - ``count``
         - integer
         - Page size. Default 100, minimum 50, maximum 200.
       * - ``nextToken``
         - string
         - Token from a previous answer. Mutually exclusive with
           ``pageOffset``.
       * - ``pageOffset``
         - integer
         - Alternative to ``nextToken``, up to 10000.
       * - ``sort``
         - object
         - ``{"direction": "ASC"|"DESC", "key": "DATE"}``.

    The names are camelCase. A body written with ``from_date`` answers ``400``
    and names ``fromDate`` as a required field.

    ### Answer

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``events``
         - array
         - The changes found, empty when there were none.
       * - ``pageSize``
         - integer
         - The page size the service applied, taken from ``count``.
       * - ``pageOffset``
         - integer
         - Where this page starts.
       * - ``maxPageNumber``
         - integer
         - The last page number reachable.
       * - ``totalRecords``
         - integer
         - How many changes the account has in the window.

    An empty ``events`` with ``totalRecords`` at ``0`` means the account saw no
    change in that window. The call worked; there was nothing to report.

    ### Two things that cost time

    **The window moves.** Ninety days is counted from the service clock at the
    moment of the request. A window computed once at the top of a script and
    reused drifts past the edge and answers
    ``400 fromDate is more than 90 days ago``. In testing, 717 milliseconds of
    drift was enough. Compute it per call and leave a day of slack.

    **The route throttles.** Seven calls within twelve seconds answered
    ``429 Too Many Requests``. Space them out.

    ### Example python

    .. code-block:: python

        from datetime import datetime, timedelta, timezone
        from ad_api.api import History

        def get_history():
            now = datetime.now(timezone.utc)
            frm = now - timedelta(days=7)   # 90 max, leave slack

            body = {
                "fromDate": int(frm.timestamp() * 1000),
                "toDate": int(now.timestamp() * 1000),
                "eventTypes": {"CAMPAIGN": {"filters": ["STATUS"]}},
                "count": 50,
                "sort": {"direction": "DESC", "key": "DATE"},
            }

            res = History(account='my_account', debug=False).get_history(body=body)
            p = res.payload
            print(f"{p['totalRecords']} cambios")
            for event in p["events"]:
                print(event)

        if __name__ == '__main__':
            get_history()

    ### Example with THEME

    ``THEME`` needs version 1.1. The method takes it as a string, because the
    versions are ``1.0`` and ``1.1``.

    .. code-block:: python

        from datetime import datetime, timedelta, timezone
        from ad_api.api import History

        now = datetime.now(timezone.utc)
        frm = now - timedelta(days=7)

        body = {
            "fromDate": int(frm.timestamp() * 1000),
            "toDate": int(now.timestamp() * 1000),
            "eventTypes": {"THEME": {"filters": ["STATUS"]}},
        }

        res = History(account='my_account', debug=False).get_history(
            body=body, version="1.1")

    ### Example query.json

    Download :download:`json <../../test/history/query.json>` the file to use:

    .. literalinclude:: ../../test/history/query.json
