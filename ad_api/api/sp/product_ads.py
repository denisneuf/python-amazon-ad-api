import urllib.parse

from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class ProductAds(Client):

    @sp_endpoint('/v2/sp/productAds', method='GET')
    def list_product_ads_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/productAds/extended', method='GET')
    def list_product_ads_extended_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'),  params=kwargs)

    @sp_endpoint('/v2/sp/productAds/{}', method='GET')
    def get_product_ad_request(self, adId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adId), params=kwargs)

    @sp_endpoint('/v2/sp/productAds/extended/{}', method='GET')
    def get_product_ad_extended_request(self, adId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adId), params=kwargs)

    @sp_endpoint('/v2/sp/productAds/{}', method='DELETE')
    def delete_product_ad_request(self, adId, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), adId), params=kwargs)

    @sp_endpoint('/v2/sp/productAds', method='PUT')
    def edit_product_ads_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/productAds', method='POST')
    def create_product_ads_request(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
