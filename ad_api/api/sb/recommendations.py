from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Recommendations(Client):
    """
    Ask for headline suggestions to use in a Sponsored Brands creative.

    The resource has a single operation, POST with a HeadlineSuggestionRequest,
    and it exists only in the 4.0 contract: the 3.0 contract does not carry the
    route. The call suggests headlines; it neither creates nor changes a
    creative, so it is safe to run while a campaign is live.
    """

    @sp_endpoint('/sb/recommendations/creative/headline', method='POST')
    def list_recommendations(self, **kwargs) -> ApiResponse:
        """
        Returns suggested headlines for the products or store pages given.

        The request names what the headlines are for, either by ASIN or by store
        page, and caps how many suggestions come back. An answer of 422 means
        the parameters were understood but rejected, which is what an empty or
        contradictory request produces.

        Request body (HeadlineSuggestionRequest)
            | **asins** (array): the products the headlines are for.
            | **storePages** (array): the store pages the headlines are for.
            | **maxNumSuggestions** (number): how many suggestions to return.
            | **adFormat** (string): the format the headlines are written for.

        Returns:
            | ApiResponse

        Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)
