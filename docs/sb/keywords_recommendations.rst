Keyword Recommendations
=======================

Gets keyword recommendations for a Sponsored Brands campaign.

.. note::
    The request and response media type is
    ``application/vnd.sbkeywordrecommendation.v3+json``. The module does not set
    it explicitly and the endpoint answers without it, but the contract declares
    it for both directions.

.. autoclass:: ad_api.api.sb.KeywordsRecommendations
    :members:

    ### Request body

    The body must carry one of two shapes, never both:

    **By ASIN** — ``asins`` is required.

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Description
       * - ``asins``
         - array
         - Required. ASINs to base the recommendations on.
       * - ``goal``
         - string
         - ``PAGE_VISIT``, ``BRAND_IMPRESSION_SHARE``, ``ACQUIRE_NEW_CUSTOMERS`` or ``AD_VIEWS``.
       * - ``creativeType``
         - string
         - ``PRODUCT_COLLECTION``, ``AUTHOR_COLLECTION``, ``STORE_SPOTLIGHT``, ``VIDEO`` or ``BRAND_VIDEO``.
       * - ``maxNumSuggestions``
         - integer
         - Up to 1000. Defaults to 100.
       * - ``creativeAsins``
         - array
         - ASINs used by the creative.
       * - ``locale``
         - string
         - Optional locale for the suggested keywords.

    **By landing page URL** — ``url`` is required.

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Description
       * - ``url``
         - string
         - Required. Stores page URL, or a custom landing page URL.
       * - ``goal``
         - string
         - Same values as above.
       * - ``creativeType``
         - string
         - Same values as above.
       * - ``maxNumSuggestions``
         - integer
         - Up to 1000. Defaults to 100.
       * - ``creativeAsins``
         - array
         - ASINs used by the creative.
       * - ``locale``
         - string
         - Optional locale for the suggested keywords.

    A body with neither ``asins`` nor ``url`` answers ``400`` with
    *"Must include one of: ASINs, Landing Page Url, or Landing Page Url list in
    request"*.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import KeywordsRecommendations

        recs = KeywordsRecommendations(account='account_name', debug=False)

        body = {
            "asins": ["B00TEST01"],
            "goal": "PAGE_VISIT",
            "creativeType": "PRODUCT_COLLECTION",
            "maxNumSuggestions": 100,
        }

        response = recs.list_keywords_recommendations(body=body)
        print(response.payload)

    ### Example by landing page

    .. code-block:: python

        body = {
            "url": "https://www.amazon.es/stores/page/XXXXXXXX",
            "goal": "BRAND_IMPRESSION_SHARE",
        }

        response = recs.list_keywords_recommendations(body=body)

    ### Responses

    .. list-table::
        :header-rows: 1

       * - Status
         - Meaning
       * - ``200``
         - Recommendations returned.
       * - ``400``
         - Bad request, usually a missing ``asins`` or ``url``.
       * - ``429``
         - Rate limited; retry later.
       * - ``500``
         - Internal error on Amazon's side.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Keyword-Recommendations
