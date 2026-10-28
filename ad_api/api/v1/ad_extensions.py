from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class AdExtensions(Client):
    r"""
    AdExtensions(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified AdExtensions endpoints

    An ad extension adds delivery detail to an existing Sponsored Products ad
    rather than creating a new one. The contract declares exactly two types:

    - ``PROMPTS`` -- a prompt-style text extension.
    - ``VIDEO`` -- a video extension.

    There is no delete route. An extension is created, queried and updated; the
    only thing ``update`` changes is ``state``, so ending one means pausing or
    archiving it. Editing its content means creating a new extension and
    archiving the old one.

    Like every v1 resource, the product is chosen in the body through
    ``adProductFilter`` / ``adProduct``, never in the path. For this contract
    the enum is a single value, ``SPONSORED_PRODUCTS``.
    """

    @sp_endpoint('/adsApi/v1/query/adExtensions', method='POST')
    def query_ad_extensions(self, **kwargs) -> ApiResponse:
        r"""
        query_ad_extensions(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query AdExtensions (operationId: SPQueryAdExtension)

        Request Body
            | **adProductFilter** (dict) [optional here, required by the service in practice]
                | **include** (list<AdProduct>) : Enum [ SPONSORED_PRODUCTS ]
            | **adIdFilter** (dict) [optional]
                | **include** (list<string>) : 1..300 ad identifiers
            | **adGroupIdFilter** (dict) [optional]
                | **include** (list<string>) : ad group identifiers
            | **adExtensionIdFilter** (dict) [optional]
                | **include** (list<string>) : extension identifiers
            | **adExtensionStatusFilter** (dict) [optional]
                | **include** (list<AdExtensionStatus>)
            | **adExtensionTypeFilter** (dict) [optional]
                | **include** (list<AdExtensionType>) : Enum [ PROMPTS, VIDEO ], exactly one value
            | **stateFilter** (dict) [optional]
                | **include** (list<State>) : Enum [ ENABLED, PAUSED, ARCHIVED ], 1..3 values
            | **maxResults** (int) [optional] Maximum number of records in the response
            | **nextToken** (string) [optional] Token to navigate to the next page

        Every filter object is shaped ``{"include": [...]}``, and ``include`` is
        required inside each one. An empty ``{}`` body is not the same as no
        filter: send the body you mean.

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/create/adExtensions', method='POST')
    def create_ad_extensions(self, **kwargs) -> ApiResponse:
        r"""
        create_ad_extensions(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create AdExtensions (operationId: SPCreateAdExtension)

        Request Body [Required]
            | **adExtensions** (list, 1..50) [required]

              Each element:
                | **adExtensionSettings** (SPCreateAdExtensionSettings) [required]
                | **adExtensionType** (string) [required] Enum [ PROMPTS, VIDEO ]
                | **adProduct** (string) [required] Enum [ SPONSORED_PRODUCTS ]
                | **marketplaceScope** (string) [required] Enum [ SINGLE_MARKETPLACE ]
                | **marketplaces** (list<string>) [required] marketplaces the extension applies to
                | **state** (string) [required] Enum [ ENABLED, PAUSED ]
                | **adExtensionStatus** (SPAdExtensionStatus) [optional]
                | **adGroupId** (string) [optional] ad group the extension belongs to
                | **adId** (string) [optional] ad the extension belongs to

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/update/adExtensions', method='POST')
    def update_ad_extensions(self, **kwargs) -> ApiResponse:
        r"""
        update_ad_extensions(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update AdExtensions (operationId: SPUpdateAdExtension)

        The contract accepts only an identifier and a state here. There is no
        field to change the extension's own content, so this route switches an
        extension on, off or out of the way; it does not rewrite it.

        Request Body [Required]
            | **adExtensions** (list, 1..50) [required]

              Each element:
                | **adExtensionId** (string) [required] extension to update
                | **state** (string) [optional] Enum [ ENABLED, PAUSED, ARCHIVED ]

        Returns
            ApiResponse
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
