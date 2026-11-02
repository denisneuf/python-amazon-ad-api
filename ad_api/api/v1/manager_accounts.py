from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class ManagerAccounts(Client):
    r"""
    ManagerAccounts(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified ManagerAccounts endpoints

    Three routes, no delete in the contract:

        POST /adsApi/v1/create/managerAccounts
        POST /adsApi/v1/query/managerAccounts
        POST /adsApi/v1/update/managerAccounts

    This family is not about ad products, so no adProductFilter appears
    anywhere. The query declares no required member at all: an empty body is a
    valid request and returns every manager account the caller can see.

    Both write routes take up to 10 accounts per call and answer a multi-status
    with success[] and error[] indexed the same way.

    Alongside this class the package keeps the legacy manager account reader as
    ad_api.api.ManagerAccounts; the two live in different packages and do not
    shadow each other.
    """

    @sp_endpoint('/adsApi/v1/query/managerAccounts', method='POST')
    def query_manager_accounts(self, **kwargs) -> ApiResponse:
        r"""
        query_manager_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Manager Accounts (operationId: QueryManagerAccount)

        Request Body [All optional]
            | **managerAccountIdFilter** (dict)
                | **include** (list<string>) : 1..100 identifiers
            | **maxResults** (int) : 10..100, default 100
            | **nextToken** (string) : token to navigate to the next page

        Returns
            | **managerAccounts** (list<ManagerAccount>) : 0..100
                | **displayName** (string)
                | **managerAccountId** (string)
                | **currencyCode** (CurrencyCode)
                | **timeZoneIana** (TimeZoneIana)
                | **industryVertical** (IndustryVertical)
                | **accountUsageType** (AccountUsageType)
                | **businessDetails** (BusinessDetail)
            | **nextToken** (string)

        maxResults starts at 10: a value below that is a rejected body, not a
        smaller page.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/create/managerAccounts', method='POST')
    def create_manager_accounts(self, **kwargs) -> ApiResponse:
        r"""
        create_manager_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create Manager Accounts (operationId: CreateManagerAccount)

        Request Body [Required]
            | **managerAccounts** (list<ManagerAccountCreate>) : [required] 1..10
                | **displayName** (string) : required on create
                | **currencyCode** (CurrencyCode)
                | **timeZoneIana** (TimeZoneIana)
                | **industryVertical** (IndustryVertical)
                | **accountUsageType** (AccountUsageType)
                | **businessDetails** (CreateBusinessDetail)

        Answer
            207 MultiStatus: success[] carries the created accounts with their
            index, error[] the index and reason of the refused ones.

        This route creates an account in the manager hierarchy. It is not a
        read and not something to fire to see what happens.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adsApi/v1/update/managerAccounts', method='POST')
    def update_manager_accounts(self, **kwargs) -> ApiResponse:
        r"""
        update_manager_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update Manager Accounts (operationId: UpdateManagerAccount)

        Request Body [Required]
            | **managerAccounts** (list<ManagerAccountUpdate>) : [required] 1..10
                | **managerAccountId** (string) : the account to change
                | **displayName** (string)
                | **currencyCode** (CurrencyCode)
                | **timeZoneIana** (TimeZoneIana)
                | **industryVertical** (IndustryVertical)
                | **businessDetails** (UpdateBusinessDetail)

        Answer
            207 MultiStatus, indexed the same way as create.

        businessDetails uses the Update variant of each nested object, so a
        body copied from create is not interchangeable here.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
