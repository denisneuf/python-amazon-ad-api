Tactical recommendations
========================

Recommendations the service publishes for an account, and the routes to apply or
edit one.

.. autoclass:: ad_api.api.Recommendations
    :members:

    .. note::

        Amazon lists these under ``Recommendations & insights`` in its API index,
        alongside ``Overlapping audiences``, without a beta marker. Seven other
        pages there do carry ``(beta)``; this one does not, so the label is gone
        from this page and from the readme.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Kind
         - Answer
       * - ``POST /recommendations/list``
         - ``list_recommendations``
         - read
         - ``200``
       * - ``POST /recommendations/apply``
         - ``apply_recommendations``
         - write
         - ``200``
       * - ``PUT /recommendations/{recommendationId}``
         - ``update_recommendation``
         - write
         - ``200``

    All three answer at version 1, which is the default. Unlike the Insights
    routes, where version 1 was retired and answered ``415``, these work without
    passing a version.

    ### The STATUS filter

    The filter field ``STATUS`` does not take campaign states. It takes the
    stages a recommendation passes through, and the service lists them when you
    get it wrong:

    .. code-block:: text

        Filter for recommendation status must only contain values
        [PUBLISHED, APPLY_IN_PROGRESS, APPLY_SUCCESS, APPLY_FAILED, REJECTED]

    ``ENABLED`` and ``ACTIVE`` are refused. That enum is not in the contract and
    only comes from the rejection message.

    ### About filters

    ``filters`` behaves oddly, and the contract does not explain it:

    .. list-table::
        :header-rows: 1

       * - Body
         - Result
       * - ``{"maxResults": 10}``
         - ``200``, the account's recommendations
       * - ``{"filters": []}``
         - ``400 Member must have length greater than or equal to 1``
       * - ``{"filters": [{...}]}``
         - ``200``, the filtered set

    Required when present, optional in practice. Each filter takes ``field``,
    ``values``, ``include`` and ``operator``:

    .. list-table::
        :header-rows: 1

       * - Member
         - Type
         - Meaning
       * - ``field``
         - string
         - ``RECOMMENDATION_ID``, ``AD_PRODUCT``, ``RECOMMENDATION_TYPE``,
           ``STATUS``, ``GROUPING_TYPE`` or ``CAMPAIGN_ID``.
       * - ``values``
         - array
         - Between 1 and 500 strings.
       * - ``include``
         - boolean
         - Include the match or exclude it. Defaults to true.
       * - ``operator``
         - string
         - ``EXACT`` is the only value.

    ### A body is required

    Every method takes one. Calling without it fails before the request is sent:

    .. code-block:: text

        KeyError: 'body'

    That comes from the package, not the service, so it costs nothing but says
    nothing helpful either.

    ### The writes were not exercised

    ``apply_recommendations`` edits real bidding and budgets on the account, and
    ``update_recommendation`` edits the recommendation before it is applied.
    Neither was called: the account held no recommendation to apply.

    Read one first with ``list_recommendations``. The fields
    ``update_recommendation`` expects change with ``recommendationType``, and the
    contract describes a bidding rule and a budget rule but not every type.

    ### Example: read the recommendations

    .. code-block:: python

        from ad_api.api import Recommendations

        client = Recommendations(account='my_account', debug=False)

        res = client.list_recommendations(body={"maxResults": 50})
        payload = res.payload

        print(payload["totalResults"])
        for rec in payload["recommendations"]:
            print(rec.get("recommendationId"), rec.get("recommendationType"))

    An empty list with ``totalResults`` at 0 means the account has none. That is
    a fact about the account, not a failed call, and a small account with a few
    campaigns often has none.

    ### Example: filter by status

    .. code-block:: python

        from ad_api.api import Recommendations

        client = Recommendations(account='my_account', debug=False)

        res = client.list_recommendations(body={
            "maxResults": 50,
            "filters": [{
                "field": "STATUS",
                "values": ["PUBLISHED"],
                "include": True,
                "operator": "EXACT",
            }],
        })

    ### Example: apply one

    This changes the account. Read the list first.

    .. code-block:: python

        from ad_api.api import Recommendations

        client = Recommendations(account='my_account', debug=False)

        res = client.apply_recommendations(
            body={"recommendationIds": ["your-recommendation-id"]})
        print(res.payload)
