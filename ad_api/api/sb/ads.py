from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Ads(Client):

    @sp_endpoint('/sb/v4/ads/list', method='POST')
    def list_ads(self, **kwargs):
        """
        Lists all Sponsored Brands ads.
        """
        pass

    @sp_endpoint('/sb/v4/ads/video', method='POST')
    def create_video_ads(self, **kwargs) -> ApiResponse:

        """
        Creates Sponsored Brand video ads.

        Request Body

        Returns
            ApiResponse

        """
        pass

    @sp_endpoint('/sb/v4/ads/productCollection', method='POST')
    def create_product_collection_ads(self, **kwargs) -> ApiResponse:
        """

        """
        pass

    @sp_endpoint('/sb/v4/ads/brandVideo', method='POST')
    def create_brand_video_ads(self) -> ApiResponse:
        """
        Creates Sponsored Brands brand video ads.
        """
        pass

    @sp_endpoint('/sb/v4/ads/storeSpotlight', method='POST')
    def create_store_spotlight_ads(self, **kwargs) -> ApiResponse:
        """
        Creates Sponsored Brands store spotlight ads.
        """
        pass

    @sp_endpoint('/sb/v4/ads', method='PUT')
    def update_ads(self, **kwargs):
        """

        """
        pass

    @sp_endpoint('/sb/v4/ads/delete', method='DELETE')
    def delete_ads(self, **kwargs) -> ApiResponse:
        pass
