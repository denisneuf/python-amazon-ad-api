Forecast
========

Gets performance forecasts for new Sponsored Brands campaigns.

.. warning::
    The Amazon backend for this route answers ``500 InternalFailure`` with an
    empty body once a request passes validation. Verified from every angle:
    keyword ad groups, target ad groups, themes with landing pages and mixed ad
    groups all fail the same way. The validation rules themselves do answer
    correctly, with ``400`` and a business message. This client is built to the
    contract and will work unchanged once Amazon fixes the service.

.. autoclass:: ad_api.api.sb.Forecast
    :members:

    ### Request body

    ``list_forecast`` takes the list of campaigns and wraps it in ``{"campaigns": [...]}``.

    The contract states that only **one** new campaign is supported for now.

    Campaign object:

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Description
       * - ``budget``
         - number
         - Required. Budget amount.
       * - ``budgetType``
         - string
         - Required. ``DAILY`` or ``LIFETIME``.
       * - ``forecastType``
         - string
         - Required. ``WEEKLY`` or ``MONTHLY``.
       * - ``adGroups``
         - array
         - Required. Ad groups to forecast.
       * - ``startDate``
         - string
         - ``YYYY-MM-DD``.
       * - ``endDate``
         - string
         - ``YYYY-MM-DD``, later than ``startDate``.
       * - ``goal``
         - string
         - ``PAGE_VISIT``, ``BRAND_IMPRESSION_SHARE``, ``ACQUIRE_NEW_CUSTOMERS`` or ``AD_VIEWS``. Defaults to ``PAGE_VISIT``.

    Ad group object:

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Description
       * - ``keywords``
         - array
         - ``keywordText``, ``matchType``, ``bid``.
       * - ``targets``
         - array
         - ``expressions``, ``bid``.
       * - ``themes``
         - array
         - ``themeType``, ``bid``. Requires ``landingPages``.
       * - ``landingPages``
         - array
         - ``landingPageUrl``.
       * - ``negativeKeywords``
         - array
         - ``keywordText``, ``matchType``.
       * - ``negativeTargets``
         - array
         - ``expressions``.
       * - ``creativeAsins``
         - array
         - ASINs used by the creative.

    ### Rules found by probing, not in the contract

    * ``themes`` without ``landingPages`` is rejected with
      *"LandingPageUrl list is null or empty but theme list is not empty"*.
    * An ad group carrying only ``landingPages`` is rejected with
      *"Ad group is null or missing required fields"*: it needs something to bid on.

    ### Responses

    .. list-table::
        :header-rows: 1

       * - Status
         - Meaning
       * - ``207``
         - Success. Multi-status is the documented success code, not ``200``.
       * - ``400``
         - Bad request; the message names the member that failed.
       * - ``401``
         - Unauthorized.
       * - ``403``
         - Access denied.
       * - ``422``
         - Unprocessable entity.
       * - ``429``
         - Throttled.
       * - ``500``
         - Internal failure. Empty body at the time of writing.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Forecast

        forecast = Forecast(account='account_name', debug=False)

        response = forecast.list_forecast(campaigns=[{
            "budget": 100,
            "budgetType": "DAILY",
            "forecastType": "WEEKLY",
            "startDate": "2026-11-01",
            "endDate": "2026-11-30",
            "goal": "PAGE_VISIT",
            "adGroups": [{
                "themes": [{"themeType": "KEYWORDS_RELATED_TO_YOUR_BRAND", "bid": 0.5}],
                "landingPages": [{"landingPageUrl": "https://www.amazon.es/stores/page/XXXX"}],
            }],
        }])

        print(response.payload)

    .. note::
        This replaces ``/sb/campaigns/shopperSegments/forecast``, which answers
        ``404 Could not find resource``.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi#tag/Forecasting
