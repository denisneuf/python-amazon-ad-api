from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Portfolios(Client):
    """
    Portfolios consist of campaigns that are grouped together and linked to a distinct Advertiser Account. The term 'advertiser' refers to a brand, entity, account ID, or claim ID. An integrator can create multiple portfolios within an Advertiser Account.
    """

    @sp_endpoint('/v2/portfolios', method='GET')
    def list_portfolios(self, **kwargs) -> ApiResponse:
        r"""

        list_portfolios(self, **kwargs) -> ApiResponse

        """
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/portfolios/extended', method='GET')
    def list_portfolios_extended(self, **kwargs) -> ApiResponse:
        r"""

        list_portfolios_extended(self, **kwargs) -> ApiResponse

        """
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/portfolios/{}', method='GET')
    def get_portfolio(self, portfolioId, **kwargs) -> ApiResponse:
        r"""

        get_portfolio(self, portfolioId, **kwargs) -> ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), portfolioId), params=kwargs)

    @sp_endpoint('/v2/portfolios/extended/{}', method='GET')
    def get_portfolio_extended(self, portfolioId, **kwargs) -> ApiResponse:
        r"""

        get_portfolio_extended(self, portfolioId, **kwargs) -> ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), portfolioId), params=kwargs)

    @sp_endpoint('/v2/portfolios', method='POST')
    def create_portfolios(self, **kwargs) -> ApiResponse:
        r"""

        create_portfolios(self, **kwargs) -> ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/portfolios', method='PUT')
    def edit_portfolios(self, **kwargs) -> ApiResponse:
        r"""

        edit_portfolios(self, **kwargs) -> ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
