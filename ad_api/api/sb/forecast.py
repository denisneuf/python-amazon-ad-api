from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Forecast(Client):
    """Sponsored Brands campaign performance forecasts.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi#tag/Forecasting

    .. warning::
        The Amazon backend for this route answers ``500 InternalFailure`` with an
        empty body once the request passes validation. Verified from every angle:
        keywords, targets, themes with landing pages, and mixed ad groups all fail
        the same way, while the validation rules themselves do answer correctly
        (``400`` with a business message). The client is built to the contract, so
        it will work unchanged once Amazon fixes the service.

    Validation rules observed against the live service, not in the contract:

    * ``themes`` require ``landingPages``:
      *"LandingPageUrl list is null or empty but theme list is not empty"*.
    * An ad group with only ``landingPages`` is rejected:
      *"Ad group is null or missing required fields"*; it needs something to bid on.
    """

    _ACCEPT = 'application/vnd.sbforecasting.v4+json'

    @classmethod
    def _accept(cls):
        return {"Accept": cls._ACCEPT, "Content-Type": cls._ACCEPT}

    @sp_endpoint('/sb/forecasts', method='POST')
    def list_forecast(self, campaigns, version: int = 4, **kwargs) -> ApiResponse:
        r"""
        Gets performance forecasts for new campaigns.

        ``campaigns`` is the list under the required ``campaigns`` key, ready to
        send: the method wraps it in ``{"campaigns": [...]}``.

        Positional Args
            | **campaigns** (list): One or more campaign objects. The contract
              states only one new campaign is supported for now.

        Keyword Args
            | **version** (int): Media type version, ``4`` by default.

        Campaign object
            | **budget** (number): [required] Budget amount.
            | **budgetType** (string): [required] ``DAILY`` or ``LIFETIME``.
            | **forecastType** (string): [required] ``WEEKLY`` or ``MONTHLY``.
            | **adGroups** (list): [required] Ad groups to forecast.
            | **startDate** (string): ``YYYY-MM-DD``.
            | **endDate** (string): ``YYYY-MM-DD``, later than ``startDate``.
            | **goal** (string): ``PAGE_VISIT``, ``BRAND_IMPRESSION_SHARE``,
              ``ACQUIRE_NEW_CUSTOMERS`` or ``AD_VIEWS``. Defaults to ``PAGE_VISIT``
              when the campaign was created without a goal.

        Ad group object
            | **keywords** (list): ``keywordText``, ``matchType`` and ``bid``.
            | **targets** (list): ``expressions`` and ``bid``.
            | **themes** (list): ``themeType`` and ``bid``. Requires landingPages.
            | **landingPages** (list): ``landingPageUrl``.
            | **negativeKeywords** (list): ``keywordText`` and ``matchType``.
            | **negativeTargets** (list): ``expressions``.
            | **creativeAsins** (list): ASINs used by the creative.

        Returns:
            | ApiResponse, with status ``207`` on success.

        Example::

            forecast = Forecast(account='account_name')
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
        """
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body({'campaigns': campaigns}, False),
            params=kwargs,
            headers=self._accept(),
        )
