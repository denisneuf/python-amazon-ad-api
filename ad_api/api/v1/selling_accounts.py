from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class SellingAccounts(Client):
    r"""
    SellingAccounts(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - selling accounts

    One route, read only:

        POST /adsApi/v1/query/sellingAccounts

    No adProductFilter here: a selling account is the account behind the ads,
    not an ad product. Every member of the request is optional, so an empty
    body is a valid request.
    """

    @sp_endpoint('/adsApi/v1/query/sellingAccounts', method='POST')
    def query_selling_accounts(self, **kwargs) -> ApiResponse:
        r"""
        query_selling_accounts(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Selling Accounts (operationId: QuerySellingAccount)

        Request Body [All optional]
            | **sellingAccountLinkTokenFilter** (dict)
            | **sellingProgramFilter** (dict)
            | **maxResults** (int) : 10..100, default 100
            | **nextToken** (string)

        Returns
            | **sellingAccounts** (list<SellingAccount>) : 0..100
                | **sellingAccountLinkToken** (string) : [required] the token that locates the account
                | **portals** (list<Portal>) : [required] 1..6
                | **sellingProgram** (SellingProgram) : [required]
                | **displayName** (string)
                | **countryCodes** (list<CountryCode>) : 0..30
                | **business** (SellingAccountBusiness)
            | **nextToken** (string)

        maxResults starts at 10, so a smaller value is a rejected body rather
        than a shorter page.
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
