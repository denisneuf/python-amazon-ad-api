from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class CampaignNegativeTargets(Client):
    @sp_endpoint('/sp/campaignNegativeTargets/delete', method='POST')
    def delete_campaign_negative_targets(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        Deleting campaign negative targets.

        Request Body (required)
            | SponsoredProductsDeleteSponsoredProductsCampaignNegativeTargetingClausesRequestContent {
            | campaignNegativeTargetIdFilter* SponsoredProductsObjectIdFilter {
            | Filter entities by the list of objectIds
            |       **include**\* (array) minItems: 0 maxItems: 1000 [
            |           string entity object identifier
            |       ]
            |    }
            | }

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spcampaignNegativeTargetingClause.v' + str(version) + "+json"
        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaignNegativeTargets', method='POST')
    def create_campaign_negative_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Create campaign negative targets.

        Keyword Args

        - ``prefer`` (bool): send ``Prefer: return=representation`` so create and
          update return the full object rather than only the ids. [optional]

        Request Body (required)

        - ``campaignNegativeTargetingClauses`` (array): the clauses to create.

          Each clause carries:

          - ``campaignId`` (string): the campaign the target belongs to.
          - ``state`` (string): ``ENABLED`` or ``PAUSED``.
          - ``expression`` (array): one predicate with ``type`` and ``value``.
            ``type`` is ``ASIN_BRAND_SAME_AS`` or ``ASIN_SAME_AS``.

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spCampaignNegativeTargetingClause.v' + str(version) + "+json"
        headers = {"Accept": json_version, "Content-Type": json_version}
        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaignNegativeTargets', method='PUT')
    def edit_negative_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Update campaign negative targets.

        Keyword Args

        - ``prefer`` (bool): send ``Prefer: return=representation`` so create and
          update return the full object rather than only the ids. [optional]

        Request Body (required)

        - ``campaignNegativeTargetingClauses`` (array): the clauses to update.

          Each clause carries:

          - ``targetId`` (string): the target to update.
          - ``state`` (string): ``ENABLED`` or ``PAUSED``.
          - ``expression`` (array): one predicate with ``type`` and ``value``.
            ``type`` is ``ASIN_BRAND_SAME_AS`` or ``ASIN_SAME_AS``.

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spCampaignNegativeTargetingClause.v' + str(version) + "+json"
        headers = {"Accept": json_version, "Content-Type": json_version}

        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaignNegativeTargets/list', method='POST')
    def list_campaign_negative_targets(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        List campaign negative targets.

        Request Body (optional)

        - ``campaignIdFilter`` (object): narrow to those campaigns. Carries
          ``include``, a list of campaign ids.
        - ``campaignNegativeTargetIdFilter`` (object): narrow to those targets.
          Carries ``include``, a list of target ids.
        - ``stateFilter`` (object): narrow by state. Carries ``include``, a list
          drawn from ``ENABLED``, ``PAUSED``, ``ARCHIVED``, ``ENABLING``,
          ``USER_DELETED`` and ``OTHER``.
        - ``asinFilter`` (object): narrow by ASIN. Carries ``include``, a list of
          ASINs, and ``queryTermMatchType``, either ``BROAD_MATCH`` or
          ``EXACT_MATCH``.
        - ``maxResults`` (integer): page size. Defaults to the API maximum.
        - ``nextToken`` (string): pagination token.
        - ``includeExtendedDataFields`` (boolean): also return ``creationDate``,
          ``lastUpdateDate`` and ``servingStatus``.

        Returns
            ApiResponse
        """
        content_type = 'application/vnd.spcampaignNegativeTargetingClause.v' + str(version) + '+json'
        accept = 'application/vnd.spCampaignNegativeTargetingClause.v' + str(version) + '+json'
        headers = {"Accept": accept, "Content-Type": content_type}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
