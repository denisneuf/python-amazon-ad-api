Recommendations
===============

Creative headline recommendations for Sponsored Brands.

.. note::
    ``POST /sb/recommendations/creative/headline`` answers ``422`` with
    *"Failed due to invalid parameters"* on an empty body, which means the route
    is live. The 4.0 contract lists it as ``getHeadlineRecommendations``.

.. autoclass:: ad_api.api.sb.Recommendations
    :members:

    ### Endpoint

    ==========================================  ==========================
    Path                                        Method
    ==========================================  ==========================
    ``POST /sb/recommendations/creative/headline``  ``list_recommendations``
    ==========================================  ==========================

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Recommendations

        recs = Recommendations(account='account_name', debug=False)

        response = recs.list_recommendations(body={
            "asins": ["B00TEST01"],
        })
        print(response.payload)

    .. note::
        The body shape is not documented in the contract beyond
        ``getHeadlineRecommendations``; an empty body answers ``422``, so at least
        one member is required.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
