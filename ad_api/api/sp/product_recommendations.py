from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class ProductRecommendations(Client):
    @sp_endpoint('/sp/targets/products/recommendations', method='POST')
    def list_products_recommendations(self, **kwargs) -> ApiResponse:
        contentType = 'application/vnd.spproductrecommendation.v3+json'
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
