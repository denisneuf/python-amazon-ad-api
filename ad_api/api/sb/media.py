from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Media(Client):
    """
    Poll the status of media already uploaded for Sponsored Brands.

    The v3 contract carries a single operation on this resource, GET
    /media/describe, which answers the state of a media id. A creative can be
    attached to a campaign once its media reaches PendingDeepValidation, but it
    may still fail validation afterwards and move to Failed, so a campaign can
    be rejected later. Only Available means the media finished processing and
    is published for use.

    /media/upload and /media/complete sit outside that contract. Probing
    /media/upload answers 403 IncompleteSignatureException before the router
    sees it, which suggests it expects an AWS SigV4 signature rather than the
    bearer token this client sends. /media/complete answers 500 with a
    NullPointerException on an empty body, so the route exists but its expected
    fields are unknown. Neither is verified.
    """

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
        """
        Notifies the service that an upload started by create_media finished.

        The upload location returned by create_media expires in 15 minutes, and
        this call closes the loop after the PUT to that location succeeds.

        The route answers 500 with a NullPointerException when the body is
        empty, so the body is required but its fields are not documented in any
        contract this package tracks. Pass a body as the registered example
        does and inspect the error if the service refuses it.

        Keyword Args
            | body **body** (string | dict): the completion payload. [required]

        Returns:
            | ApiResponse

        """
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/media/describe', method='GET')
    def describe_media(self, mediaId, **kwargs) -> ApiResponse:
        """
        Describes an uploaded media resource.

        The media id goes in the query string, as the contract requires. The
        answer carries a status of PendingDeepValidation, Available or Failed,
        and 404 means the id is unknown. A media id that does not exist answers
        400 InvalidMediaId, which means the route is live.

        Keyword Args
            | query **mediaId** (string): The media identifier. [required]

        Returns:
            | ApiResponse

        Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Media
        """
        return self._request(kwargs.pop('path'), params={'mediaId': mediaId, **kwargs})
