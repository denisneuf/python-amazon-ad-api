from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Ads(Client):

    @sp_endpoint('/sb/v4/ads/list', method='GET')
    def list_ads(self, **kwargs):
        """
        Lists all Sponsored Brands ads.


        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint(path="", method="GET")
    def get_ad_by_id(self, ad_id, **kwargs):
        """
        Get a specific ad by its adId identifier.

        Keyword Args
            | path **adGroupId**:*number* | Required. The identifier of an existing ad group.


        Returns
            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), ad_id), params=kwargs)

    @sp_endpoint('/sb/v4/ads/video', method='POST')
    def create_video_ads(self, **kwargs) -> ApiResponse:

        """
        Creates Sponsored Brand video ads.

        Request Body

        Returns
            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/ads/productCollection', method='POST')
    def create_product_collection_ads(self, **kwargs) -> ApiResponse:
        """
        Creates Sponsored Brands product collection ads.

        Request Body

        Returns
            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/ads/brandVideo', method='POST')
    def create_brand_video_ads(self, **kwargs) -> ApiResponse:
        """
        Creates Sponsored Brands brand video ads.

        Returns
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/ads/storeSpotlight', method='POST')
    def create_store_spotlight_ads(self, **kwargs) -> ApiResponse:
        """
        Creates Sponsored Brands store spotlight ads.

        Returns
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/ads', method='PUT')
    def update_ads(self, **kwargs) -> ApiResponse:
        """
        Updates the Sponsored Brands ads.

        Request Body

        Returns
            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sb/v4/ads/delete', method='DELETE')
    def delete_ads(self, **kwargs) -> ApiResponse:
        pass
