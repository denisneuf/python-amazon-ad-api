from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Eligibility(Client):

    @sp_endpoint('/eligibility/product/list', method='POST')
    def get_eligibility(self, **kwargs) -> ApiResponse:
        r"""

        get_eligibility(self, **kwargs) -> ApiResponse

        Gets advertising eligibility status for a list of products.

        body: | REQUIRED

            '**adType**': *string*, {'description': 'Set to 'sp' to check product eligibility for Sponsored Products advertisements. Set to 'sb' to check product eligibility for Sponsored Brands advertisements. default: sp. [ sp, sb ]'}

            '**productDetailsList**': *dict*, {'asin*': 'An Amazon product identifier.', 'sku': 'A seller product identifier'}

            '**locale**': *string*, {'description': 'Set to the locale string in the table below to specify the language in which the response is returned.'}

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
