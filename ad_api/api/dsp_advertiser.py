from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class DspAdvertiser(Client):
    @sp_endpoint('/dsp/advertisers', method='GET')
    def list_advertisers(self, **kwargs) -> ApiResponse:
        r"""
        list_advertisers(**kwargs) -> ApiResponse

        Retrieve the DSP advertisers the profile can see.

            query **startIndex**:*int* | Optional. Index of the first result.
            query **count**:*int* | Optional. Number of results to return.
            query **advertiserIdFilter**:*string* | Optional. Filter by advertiser id.

        The profile has to be a DSP one: accountInfo.type must be agency and
        subType must not be AMAZON_ATTRIBUTION.

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/dsp/advertisers/{}', method='GET')
    def get_advertiser(self, advertiserId: str, **kwargs) -> ApiResponse:
        r"""
        get_advertiser(advertiserId: str, **kwargs) -> ApiResponse

        Retrieve one DSP advertiser by id.

        path **advertiserId**:*string* | Required. The advertiser id.

        The profile has to be a DSP one: accountInfo.type must be agency and
        subType must not be AMAZON_ATTRIBUTION.

        Returns:

            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), advertiserId), params=kwargs)
