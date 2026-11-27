from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Recommendations(Client):
    r"""
    Recommendations(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - recommendations

    Three routes, two of them generic and one per product:

        POST /adsApi/v1/query/recommendations      QueryRecommendation
        GET  /adsApi/v1/recommendations            ListRecommendation
        POST /adsApi/v1/create/recommendations/sb  SBCreateRecommendation

    Only the create carries a product suffix in its path. The query and the
    list are generic and take the product in ``adProductFilter``, so a
    Sponsored Products or Sponsored Display create would sit beside the SB one
    under its own suffix without touching these two.

    The query requires ``accessRequestedAccounts``, the same account selector
    the v1 reports family uses, so the account travels in the body and not only
    in the headers.
    """

    @sp_endpoint('/adsApi/v1/query/recommendations', method='POST')
    def query_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        query_recommendations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Recommendations (operationId: QueryRecommendation)

        Request Body [Required]
            | **accessRequestedAccounts** (list<QueryRecommendationRequestAccessRequestedAccountItem>) : [required] 1..2000, each item is either {advertiserAccountId} or {managerAccountId}
            | **adProductFilter** (dict) [optional]
            | **recommendationTypeFilter** (dict) [optional]
            | **recommendationTypeDetailsFilter** (dict) [optional]
            | **marketplacesFilter** (dict) [optional]
            | **languageFilter** (dict) [optional]
            | **maxResults** (int) : 1..300, default 100
            | **nextToken** (string)

        Returns
            | **recommendations** (list<Recommendation>) : 0..300
            | **totalResults** (int)
            | **nextToken** (string)

        Headers
            | **Amazon-Ads-ClientId** (string) [required] sent by the base Client
              on every call.

        The accounts travel in the body through ``accessRequestedAccounts``,
        each item naming an ``advertiserAccountId`` or a ``managerAccountId``.
        The contract also declares Amazon-Ads-AccountId as optional here.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}

        # Optional account header, taken from kwargs and removed before the
        # call is built: left in kwargs it would travel in the query string.
        account_id = kwargs.pop('account_id', None)
        if account_id:
            headers["Amazon-Ads-AccountId"] = account_id

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/recommendations', method='GET')
    def list_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        list_recommendations(**params) -> ApiResponse

        Amazon Ads API v1 - List Recommendations (operationId: ListRecommendation)

        A GET with query parameters, not a body.

        Headers
            | **Amazon-Ads-AccountId** (string) [optional] advertiser account
            | **Amazon-Ads-Manager-AccountId** (string) [optional] manager account
        Parameters
            | **nextToken**, **maxResults** (1..300), **adProduct**, **marketplace**, **language**, **recommendationType**

        The account travels in the headers, and since 2026-11-11 the contract
        marks both of them optional: the list can be read for an advertiser
        account or for a manager account. Pass ``account_id=`` or
        ``manager_id=``; each becomes its own header and neither reaches the
        query string.

        Returns
            | **recommendations** (list<Recommendation>) : 0..300
            | **totalResults** (int)
            | **nextToken** (string)
        """
        path = kwargs.pop('path')
        params = dict(kwargs)

        # Optional account headers, taken from kwargs and removed before the
        # call is built: left in kwargs they would travel in the query string.
        account_id = params.pop('account_id', None)
        manager_id = params.pop('manager_id', None)
        headers = {}
        if account_id:
            headers["Amazon-Ads-AccountId"] = account_id
        if manager_id:
            headers["Amazon-Ads-Manager-AccountId"] = manager_id

        return self._request(path, params=params, headers=headers or None)

    @sp_endpoint('/adsApi/v1/create/recommendations/sb', method='POST')
    def create_recommendations_sb(self, **kwargs) -> ApiResponse:
        r"""
        create_recommendations_sb(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Sponsored Brands Recommendation (operationId: SBCreateRecommendation)

        Request Body
            | **recommendations** (list<SBRecommendationCreate>) : 1..1

        Answer
            207 MultiStatus with success[] and error[] indexed.

        This route creates a recommendation in the account, so it is not a
        read. It is the only route in the family with a product suffix.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}

        # Optional advertiser account header, taken from kwargs and removed
        # before the call is built: left in kwargs it would travel in the query.
        account_id = kwargs.pop('account_id', None)
        if account_id:
            headers["Amazon-Ads-AccountId"] = account_id

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
