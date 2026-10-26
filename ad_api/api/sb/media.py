from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Media(Client):
    """
    Use this interface to request and retrieve store information. This can be used for Sponsored Brands campaign creation, to pull the store URL information, and for asset registration for Stores.
    """

    # NOTE: /media/upload and /media/complete are NOT in the v3 contract.
    # Probing /media/upload answers 403 IncompleteSignatureException before the
    # router sees it, which suggests the route expects an AWS SigV4 signature
    # rather than the bearer token this client sends. Not verified either way.
    # /media/complete answers 500 with a NullPointerException on an empty body,
    # so the route exists but its expected fields are unknown.

    @sp_endpoint('/media/upload', method='POST')
    def create_media(self, **kwargs) -> ApiResponse:
        """
        Creates an ephemeral resource (upload location) to upload Media for an Ad Program (SponsoredBrands).

        The upload location is short lived and expires in 15 minutes. Once the upload is complete, /media/complete API should be used to notify that the upload is complete.

        The upload location only supports PUT HTTP Method to upload the media content. If the upload location expires, API user will get 403 Forbidden response.

        Request body
            | **programType** (string): [required] [ SponsoredBrands ].
            | **creativeType** (string): [required] [ Video ].

        Returns:
            | ApiResponse

        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/media/complete', method='PUT')
    def complete_media(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/media/describe', method='GET')
    def describe_media(self, mediaId, **kwargs) -> ApiResponse:
        """
        Describes an uploaded media resource.

        The media id goes in the query string. Answered ``400 InvalidMediaId``
        for an id that does not exist, which means the route is live.

        Keyword Args
            | path **mediaId** (string): The media identifier. [required]

        Returns:
            | ApiResponse

        Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi
        """
        return self._request(kwargs.pop('path'), params={'mediaId': mediaId, **kwargs})
