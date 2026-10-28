from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class AdAssociations(Client):
    r"""
    AdAssociations(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - unified AdAssociations endpoints

    An ad association links one ``adId`` to one ``adGroupId`` and decides how
    much of the group's traffic that ad receives. ``weight`` is the relative
    percentage directed to the creative, and ``startDateTime`` / ``endDateTime``
    bound when the association applies.

    This is the first v1 family in this client with all four operations: the
    others stop at update, while this one also has a delete.

    Update cannot move an association to another ad or ad group: only the dates,
    the state and the weight are accepted, so reassigning means delete and
    create.

    Like AdvertiserAccounts, this is not an ad-product resource and takes no
    ``adProductFilter`` -- the query filters by association, ad group or ad.
    """

    @sp_endpoint('/adsApi/v1/query/adAssociations', method='POST')
    def query_ad_associations(self, **kwargs) -> ApiResponse:
        r"""
        query_ad_associations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query AdAssociations (operationId: QueryAdAssociation)

        Request Body
            | **adAssociationIdFilter** (dict) [optional]
                | **include** (list<string>) : association identifiers
            | **adGroupIdFilter** (dict) [optional]
                | **include** (list<string>) : ad group identifiers
            | **adIdFilter** (dict) [optional]
                | **include** (list<string>) : ad identifiers
            | **maxResults** (int) [optional] Maximum number of records in the response
            | **nextToken** (string) [optional] Token to navigate to the next page

        Returns
            ApiResponse. ``payload`` holds ``adAssociations`` and ``nextToken``.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/create/adAssociations', method='POST')
    def create_ad_associations(self, **kwargs) -> ApiResponse:
        r"""
        create_ad_associations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Create AdAssociations (operationId: CreateAdAssociation)

        Request Body [Required]
            | **adAssociations** (list, 1..20) [required]

              Each element:
                | **adGroupId** (string) [required] the ad group the ad belongs to
                | **adId** (string) [required] the ad being associated
                | **state** (string) [required] Enum [ ENABLED, PAUSED ]
                | **startDateTime** (string) [optional] when the association starts
                | **endDateTime** (string) [optional] when it stops
                | **weight** (integer) [optional] relative share of the ad
                  group's traffic directed to this creative

        Returns
            ApiResponse. Per-entity result carrying ``success`` and ``error``,
            not the created objects.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/update/adAssociations', method='POST')
    def update_ad_associations(self, **kwargs) -> ApiResponse:
        r"""
        update_ad_associations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Update AdAssociations (operationId: UpdateAdAssociation)

        The ad and the ad group cannot be changed here. To point the same creative
        at a different ad, delete the association and create a new one.

        Request Body [Required]
            | **adAssociations** (list, 1..20) [required]

              Each element:
                | **adAssociationId** (string) [required] association to update
                | **startDateTime** (string) [optional]
                | **endDateTime** (string) [optional]
                | **state** (string) [optional] Enum [ ENABLED, PAUSED, ARCHIVED ]
                | **weight** (integer) [optional]

        Returns
            ApiResponse. Per-entity result carrying ``success`` and ``error``.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )

    @sp_endpoint('/adsApi/v1/delete/adAssociations', method='POST')
    def delete_ad_associations(self, **kwargs) -> ApiResponse:
        r"""
        delete_ad_associations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Delete AdAssociations (operationId: DeleteAdAssociation)

        The array is named ``adAssociationIds`` here, not ``adAssociations`` as in
        create and update. Sending the wrong name is a rejected request.

        Request Body [Required]
            | **adAssociationIds** (list, 1..20) [required] associations to delete

        Returns
            ApiResponse. Per-entity result carrying ``success`` and ``error``.
        """
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        return self._request(
            kwargs.pop('path'),
            data=Utils.convert_body(kwargs.pop('body'), False),
            params=kwargs,
            headers=headers,
        )
