from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class PortfoliosV3(Client):
    """ """

    @sp_endpoint('/portfolios/list', method='POST')
    def list_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""

        list_portfolios(body: (str, dict)) -> ApiResponse

        """

        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)



    @sp_endpoint('/portfolios', method='POST')
    def create_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""

        create_portfolios(body: (str, dict)) -> ApiResponse


        """
        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/portfolios', method='PUT')
    def edit_portfolios(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""

        edit_portfolios(body: (str, dict)) -> ApiResponse


        """
        schema_version = 'application/vnd.spPortfolio.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)


    @sp_endpoint('/portfolios/budget/usage', method='POST')
    def get_budget_usage_for_portfolios(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""

        get_budget_usage_for_portfolios(body: (str, dict)) -> ApiResponse


        """
        schema_version = 'application/vnd.portfoliobudgetusage.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)