from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Portfolios(Client):
    r"""
    Portfolios(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified Portfolios endpoints

    A portfolio groups campaigns under one name, one budget and one set of
    marketplace rules. It is the v1 replacement for the v2 ``/v2/portfolios``
    routes, retired in March 2025, and for the v3 ``/portfolios`` family.

    Three routes, all POST. There is no GET on a path and no DELETE:

        /adsApi/v1/create/portfolios   CreatePortfolio
        /adsApi/v1/query/portfolios    QueryPortfolio
        /adsApi/v1/update/portfolios   UpdatePortfolio

    A portfolio is never deleted: it is retired by updating ``state`` to
    ARCHIVED, which is a terminal state and cannot be reverted.

    Budget sharing is the new part
    ------------------------------
    ``budgetControls.campaignBudgetSharing.shareUnspentCampaignBudget``
    (ENABLED or DISABLED) lets the campaigns of the portfolio spend budget
    that the other campaigns did not use, instead of each campaign being
    capped on its own.

    Global and per marketplace
    --------------------------
    A portfolio is GLOBAL, covering every marketplace named in
    ``marketplaces``, or SINGLE_MARKETPLACE. When it is global,
    ``marketplaceConfigurations`` overrides ``budgetControls``,
    ``startDateTime``, ``endDateTime`` and ``state`` for one marketplace, up
    to 30 overrides. Anything not overridden carries the global value.

    Writes answer 207, not 200: a batch can create some portfolios and
    reject others, so ``success`` and ``error`` in the payload have to be read
    together, indexed the same way.
    """

    @sp_endpoint('/adsApi/v1/create/portfolios', method='POST')
    def create_portfolios(self, **kwargs) -> ApiResponse:
        r"""
        create_portfolios(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Portfolios (operationId: CreatePortfolio)

        Request Body [Required]
            | **portfolios** (list<PortfolioCreate>) : [required] 1..100

        PortfolioCreate fields
            | **name** (string) : the name of the portfolio
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED, PROPOSED ]
            | **marketplaceScope** (string) : Enum [ GLOBAL, SINGLE_MARKETPLACE ]
            | **marketplaces** (list<Marketplace>) : 0..30 country codes
            | **budget** (dict)
                | **budgetType** (string) : [required] MONETARY
                | **budgetValue** (dict) : [required] the monetary value
                | **recurrenceTimePeriod** (string) : [required]
                  Enum [ DAILY, LIFETIME ]
            | **budgetControls** (dict)
                | **campaignBudgetSharing** (dict) : [required]
                    | **shareUnspentCampaignBudget** (string) : [required]
                      Enum [ DISABLED, ENABLED ]
            | **marketplaceConfigurations** (list<dict>) : 0..30
                | **marketplace** (string) : [required] the country code
                | **overrides** (dict) : [required]
                    | **budgetControls**, **startDateTime**,
                      **endDateTime**, **state**
            | **startDateTime** (string) : ISO 8601, with a LIFETIME budget
            | **endDateTime** (string) : ISO 8601, with a LIFETIME budget

        Returns
            207 MultiStatus with success[] and error[] indexed together.
            Each success carries the created Portfolio and its position.

        This writes into the account. A 207 is not all or nothing: read both
        lists before assuming every portfolio was created.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        body = kwargs.pop('body', None)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers,
                             **({'data': Utils.convert_body(body, False)} if body is not None else {}))

    @sp_endpoint('/adsApi/v1/query/portfolios', method='POST')
    def query_portfolios(self, **kwargs) -> ApiResponse:
        r"""
        query_portfolios(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Portfolios (operationId: QueryPortfolio)

        A POST that reads: the filters travel in the body, not in the path.

        Request Body
            | **portfolioIdFilter** (dict) [optional]
                | **include** (list<string>) : 1..1000 portfolio identifiers
            | **nameFilter** (dict) [optional]
                | **include** (list<string>) : 1..100 names
                | **queryTermMatchType** (string) : [required]
                  Enum [ BROAD_MATCH, EXACT_MATCH ]
            | **stateFilter** (dict) [optional]
                | **include** (list<State>) : ARCHIVED, DRAFT, ENABLED,
                  PAUSED, PROPOSED
            | **marketplaceScopeFilter** (dict) [optional]
                | **include** (list<MarketplaceScope>) : exactly 1,
                  GLOBAL or SINGLE_MARKETPLACE
            | **maxResults** (int) : 1..100, default 100
            | **nextToken** (string) : the token from the previous page

        Returns
            | **portfolios** (list<Portfolio>), **nextToken** (string)

        Portfolio fields
            | **portfolioId**, **globalPortfolioId**, **name**, **state**,
              **status**
            | **budget**, **budgetControls**
            | **startDateTime**, **endDateTime**
            | **marketplaces** (list<string>), **marketplaceScope**
            | **marketplaceConfigurations** (list<dict>) : the per marketplace
              overrides, 0..30
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        body = kwargs.pop('body', None)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers,
                             **({'data': Utils.convert_body(body, False)} if body is not None else {}))

    @sp_endpoint('/adsApi/v1/update/portfolios', method='POST')
    def update_portfolios(self, **kwargs) -> ApiResponse:
        r"""
        update_portfolios(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Portfolios (operationId: UpdatePortfolio)

        Request Body [Required]
            | **portfolios** (list<PortfolioUpdate>) : [required] 1..100

        PortfolioUpdate fields
            | **portfolioId** (string) : [required] the portfolio to rewrite
            | **name** (string)
            | **state** (string) : Enum [ DRAFT, ENABLED, PAUSED, PROPOSED,
              ARCHIVED ]
            | **budget** (dict)
                | **budgetType**, **budgetValue** (UpdateBudgetValue),
                  **recurrenceTimePeriod**
            | **budgetControls** (dict)
                | **campaignBudgetSharing** (dict)
                    | **shareUnspentCampaignBudget** (string) : ENABLED, DISABLED
            | **marketplaces** (list<Marketplace>) : 0..30
            | **marketplaceConfigurations** (list<dict>) : 0..30
            | **startDateTime** (string) : nullable
            | **endDateTime** (string) : nullable

        Returns
            207 MultiStatus with success[] and error[] indexed together.

        ARCHIVED is terminal: a portfolio set to ARCHIVED cannot be
        reactivated. With no delete route, archiving is how a portfolio is
        retired.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        body = kwargs.pop('body', None)
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers,
                             **({'data': Utils.convert_body(body, False)} if body is not None else {}))
