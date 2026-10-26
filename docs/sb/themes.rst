Themes
======

Sponsored Brands theme targets.

.. note::
    ``list_themes`` answers ``200`` on a live account, and the media types below
    were exercised against the service. The two write methods are documented from
    the contract and the module docstrings; they are not probed, because they
    change campaign data.

.. autoclass:: ad_api.api.sb.Themes

    .. autofunction:: ad_api.api.sb.Themes.list_themes(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Themes.create_themes(self, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.Themes.update_themes(self, **kwargs) -> ApiResponse:

    ### Endpoint map

    ==========================================  ==============================  =====================================
    Path                                        Method                          Response media type
    ==========================================  ==============================  =====================================
    ``POST /sb/themes/list``                    ``list_themes``                 ``vnd.sbthemeslistresponse.v3``
    ``POST /sb/themes``                         ``create_themes``               ``vnd.sbthemescreateresponse.v3``
    ``PUT  /sb/themes``                         ``update_themes``               ``vnd.sbthemesupdateresponse.v3``
    ==========================================  ==============================  =====================================

    ### list_themes request body

    ====================  ========  ==============================================================
    Field                 Type      Description
    ====================  ========  ==============================================================
    ``nextToken``         string    Pagination token.
    ``maxResults``        number    Maximum results; defaults to the API maximum.
    ``campaignIdFilter``  object    Campaign ids, max 100.
    ``adGroupIdFilter``   object    Ad group ids, max 100.
    ``themeIdFilter``     object    Theme ids, max 100.
    ``stateFilter``       object    ``enabled``, ``paused``, ``archived``. Default enabled and paused.
    ``themeTypeFilter``   object    ``KEYWORDS_RELATED_TO_YOUR_BRAND`` or
                                    ``KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES``.
    ====================  ========  ==============================================================

    ### create_themes request body

    .. code-block:: json

        {
            "themes": [
                {
                    "adGroupId": "string",
                    "campaignId": "string",
                    "themeType": "KEYWORDS_RELATED_TO_YOUR_BRAND|KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES",
                    "bid": 0.75
                }
            ]
        }

    Maximum of 100 themes per call. Only one target per ``themeType`` per ad group.

    ### update_themes request body

    .. code-block:: json

        {
            "themes": [
                {
                    "themeId": "string",
                    "adGroupId": "string",
                    "campaignId": "string",
                    "state": "enabled|paused|archived",
                    "bid": 0.80
                }
            ]
        }

    Maximum of 100 themes per call.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Themes

        themes = Themes(account='account_name', debug=False)

        # list
        print(themes.list_themes(body={}).payload)

        # create
        themes.create_themes(themes=[{
            "adGroupId": "YOUR_ADGROUP_ID",
            "campaignId": "YOUR_CAMPAIGN_ID",
            "themeType": "KEYWORDS_RELATED_TO_YOUR_BRAND",
            "bid": 0.75,
        }])

        # update
        themes.update_themes(themes=[{
            "themeId": "YOUR_THEME_ID",
            "adGroupId": "YOUR_ADGROUP_ID",
            "campaignId": "YOUR_CAMPAIGN_ID",
            "state": "paused",
        }])

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi
