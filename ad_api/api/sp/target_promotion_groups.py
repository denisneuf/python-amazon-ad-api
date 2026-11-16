from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class TargetPromotionGroups(Client):
    r"""
    Amazon Ads API - Sponsored Products target promotion groups.

    A target promotion group ties one auto-targeting ad group to the manual
    ad groups that receive the targets promoted out of it: one keyword
    targeting ad group and one product targeting ad group. The auto ad group
    discovers search terms, the manual ad groups carry the promoted targets.
    """

    @sp_endpoint('/sp/targetPromotionGroups/list', method='POST')
    def list_target_promotion_groups(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        list_target_promotion_groups(body: (dict, str)) -> ApiResponse

        Returns the target promotion groups of an advertiser, and optionally
        of one ad group or one target promotion group.

        Request Body [optional]
            | **adGroupIdFilter** (object): Ad group identifiers to filter by.
            |   **include** (array of string)
            | **targetPromotionGroupIdFilter** (object): Target promotion group identifiers.
            |   **include** (array of string)
            | **maxResults** (int): 1 to 1000. Defaults to 1000.
            | **nextToken** (string): Token for the next page.

        Returns:
            ApiResponse
        """

        json_version = "application/vnd.sptargetpromotiongroup.v" + str(version) + "+json"

        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body', {}), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/targetPromotionGroups/targets/list', method='POST')
    def list_target_promotion_group_targets(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        list_target_promotion_group_targets(body: (dict, str)) -> ApiResponse

        Returns the targets created through target promotion groups, for an
        advertiser and optionally for one target promotion group.

        Request Body [optional]
            | **adGroupIdFilter** (object)
            |   **include** (array of string)
            | **targetPromotionGroupIdFilter** (object)
            |   **include** (array of string)
            | **maxResults** (int): 1 to 1000. Defaults to 1000.
            | **nextToken** (string): Token for the next page.

        Returns:
            ApiResponse
        """

        json_version = "application/vnd.sptargetpromotiongrouptarget.v" + str(version) + "+json"

        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body', {}), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/targetPromotionGroups/recommendations', method='POST')
    def get_target_promotion_groups_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        get_target_promotion_groups_recommendations(body: (dict, str)) -> ApiResponse

        Retrieves keyword and product targets of an auto-targeting campaign as
        recommendations for promoting them to a manual-targeting campaign, based
        on performance heuristics of those targets.

        Request Body [optional]
            | **adGroupIdFilter** (object)
            |   **include** (array of string)
            | **adIdFilter** (object)
            |   **include** (array of string)
            | **campaignIdFilter** (object)
            |   **include** (array of string)
            | **maxResults** (int): 1 to 1000. Defaults to 1000.
            | **nextToken** (string): Token for the next page.

        Returns:
            ApiResponse
        """

        json_version = "application/vnd.spTargetPromotionGroupsRecommendations.v1+json"

        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body', {}), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/targetPromotionGroups', method='POST')
    def create_target_promotion_groups(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        create_target_promotion_groups(body: (dict, str)) -> ApiResponse

        Creates a target promotion group, grouping the auto-targeting ad group
        with the manual keyword targeting ad group and the manual product
        targeting ad group.

        Request Body [required]
            | **adGroupId** (string): Source ad group of the auto-targeting campaign.
            | **adIds** (array of string): Product ads of that ad group. All the
            |   product ads are used when the list is omitted.
            | **existingCampaignDetails** (object): Existing manual ad groups.
            | **newCampaignDetails** (object): Manual campaigns and ad groups to create.

        Returns:
            ApiResponse
        """

        json_version = "application/vnd.sptargetpromotiongroup.v" + str(version) + "+json"

        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/targetPromotionGroups/targets', method='POST')
    def create_target_promotion_group_targets(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        create_target_promotion_group_targets(body: (dict, str)) -> ApiResponse

        Creates keyword and/or product targets in the manual ad group that is
        part of the target promotion group.

        Request Body [required]
            | **targetPromotionGroupId** (string): Where the targets are added.
            | **targets** (array): Up to 1000 targets.

        Returns:
            ApiResponse
        """

        json_version = "application/vnd.sptargetpromotiongrouptarget.v" + str(version) + "+json"

        headers = {"Accept": json_version, "Content-Type": json_version}

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
