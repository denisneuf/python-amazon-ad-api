from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class RankedKeywordsRecommendations(Client):
    """
    Sponsored Products Targeting API.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#/

    Specification: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

    """

    @sp_endpoint('/sp/targets/keywords/recommendations', method='POST')
    def list_ranked_keywords_recommendations(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.spkeywordsrecommendation.v4+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs, headers=headers)
