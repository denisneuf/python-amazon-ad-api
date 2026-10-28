from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class AdvertiserAccounts(Client):
    r"""
    AdvertiserAccounts(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified AdvertiserAccounts endpoints

    Three routes and no delete, like the rest of the account family:

    - ``create_advertiser_accounts`` -- 1 to 100 accounts per call.
    - ``query_advertiser_accounts`` -- filter by identifier or by global flag.
    - ``update_advertiser_accounts`` -- here the mutable fields really are
      mutable: currency, time zone, display name, industry, manager link.

    Unlike Ads, Targets or AdExtensions this is not an ad-product resource, so
    there is no ``adProductFilter```; querying is by ``advertiserAccountIdFilter``
    or ``isGlobalAccountFilter``.

    ``managerAccountId`` decides what the account can run: without it the account
    is created for Sponsored Ads only, and DSP needs it set.
    """

    @sp_endpoint('/adsApi/v1/query/advertiserAccounts', method='POST')
    def query_advertiser_accounts(self, **kwargs) -> ApiResponse:
        r"""
        query_advertiser_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query AdvertiserAccounts (operationId: QueryAdvertiserAccount)

        Request Body
            | **advertiserAccountIdFilter** (dict) [optional]
                | **include** (list<string>) : advertiser account identifiers
            | **isGlobalAccountFilter** (dict) [optional]
                | **include** (list<boolean>) : true for global accounts
            | **maxResults** (int) [optional] Maximum number of records in the response
            | **nextToken** (string) [optional] Token to navigate to the next page

        Returns
            ApiResponse. ``payload`` holds ``advertiserAccounts`` and ``nextToken``.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/create/advertiserAccounts', method='POST')
    def create_advertiser_accounts(self, **kwargs) -> ApiResponse:
        r"""
        create_advertiser_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create AdvertiserAccounts (operationId: CreateAdvertiserAccount)

        Request Body [Required]
            | **advertiserAccounts** (list, 1..100) [required]

              Each element:
                | **businessDetails** (list, exactly 1) [required]
                  Carries either ``addressToken`` for an existing selling account
                  address, or ``address`` when that account has none. Also accepts
                  ``businessRegistrationNumber`` and ``website`.
                | **currencyCode** (string) [optional] Enum of 34 ISO codes,
                  including ``EUR``, ``USD``, ``GBP`
                | **displayName** (string) [optional] name shown for the account
                | **industryVertical** (string) [optional] Enum of 19 sectors
                | **isGlobalAccount** (boolean) [optional]
                | **isTestAccount** (boolean) [optional]
                | **managerAccountId** (string) [optional] Required for
                  ADSP-enabled accounts; without it the account is created for
                  Sponsored Ads only.
                | **sellingAccountLinkRequests** (list, 0..1) [optional]
                | **timeZoneIana** (string) [optional] Enum of 42 IANA zones

        The full enum lists live in the contract; they are not repeated here.

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/update/advertiserAccounts', method='POST')
    def update_advertiser_accounts(self, **kwargs) -> ApiResponse:
        r"""
        update_advertiser_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update AdvertiserAccounts (operationId: UpdateAdvertiserAccount)

        Request Body [Required]
            | **advertiserAccounts** (list) [required]

              Each element:
                | **advertiserAccountId** (string) [required] account to update
                | **businessDetails** (list) [optional]
                | **currencyCode** (string) [optional]
                | **displayName** (string) [optional]
                | **industryVertical** (string) [optional]
                | **isGlobalAccount** (boolean) [optional]
                | **isTestAccount** (boolean) [optional]
                | **managerAccountId** (string) [optional]
                | **sellingAccountLinkRequests** (list) [optional]
                | **timeZoneIana** (string) [optional]

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
