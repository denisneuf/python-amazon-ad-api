from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class Themes(Client):
    """
    Amazon Ads API - Sponsored Brands - Theme Targeting
    
    Theme targeting automatically targets keywords related to your brand or landing pages.
    """

    @sp_endpoint('/sb/themes/list', method='POST')
    def list_themes(self, **kwargs) -> ApiResponse:
        r"""
        Gets a list of theme targets associated with the client identifier, filtered by specified criteria.

        Request Body
            | '**nextToken**': *string*, {'description': 'Token for pagination. Operations that return paginated results include a pagination token in this field.'}
            | '**maxResults**': *number*, {'description': 'Maximum number of results to return. Defaults to API maximum.'}
            | '**campaignIdFilter**': *object*, {'description': 'List of campaign identifiers to filter by (max 100).'}
            | '**adGroupIdFilter**': *object*, {'description': 'List of ad group identifiers to filter by (max 100).'}
            | '**themeIdFilter**': *object*, {'description': 'List of theme target identifiers to filter by (max 100).'}
            | '**stateFilter**': *object*, {'description': 'List of theme target states to filter by. Valid values: enabled, paused, archived. Default: enabled, paused.'}
            | '**themeTypeFilter**': *object*, {'description': 'List of theme types to filter by. Valid values: KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES.'}

        Returns:
            | ApiResponse
        """
        headers = {'Accept': 'application/vnd.sbthemeslistresponse.v3+json'}
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/sb/themes', method='POST')
    def create_themes(self, **kwargs) -> ApiResponse:
        r"""
        Create one or more theme targets.

        Note that theme targets can be created on multi-adGroup campaigns where campaign serving status is not archived, terminated, rejected, or ended.
        Note that ad group state must not be archived.
        Note that only one target can be created for each themeType per adGroup.
        Note that this operation supports a maximum list size of 100 theme targets.

        Request Body
            | '**themes**': *array*, {'description': 'List of theme targets to create (max 100).'}
                | '**adGroupId**': *string*, {'description': 'The identifier of the ad group'}
                | '**campaignId**': *string*, {'description': 'The identifier of the campaign'}
                | '**themeType**': *string*, {'description': 'Theme type', 'Enum': 'KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES'}
                | '**bid**': *number*, {'description': 'The bid amount'}

        Returns:
            | ApiResponse
        """
        headers = {'Accept': 'application/vnd.sbthemescreateresponse.v3+json'}
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/sb/themes', method='PUT')
    def update_themes(self, **kwargs) -> ApiResponse:
        r"""
        Updates one or more theme targets.

        Note that theme targets can be updated on multi-adGroup campaigns where campaign serving status is not archived, terminated, rejected, or ended.
        Note that ad group state must not be archived.
        Note that this operation supports a maximum list size of 100 theme targets.
        Note that bid is only mutable when the corresponding campaign does not have any enabled optimization rule.

        Request Body
            | '**themes**': *array*, {'description': 'List of theme targets to update (max 100).'}
                | '**themeId**': *string*, {'description': 'The identifier of the theme target'}
                | '**adGroupId**': *string*, {'description': 'The identifier of the ad group'}
                | '**campaignId**': *string*, {'description': 'The identifier of the campaign'}
                | '**state**': *string*, {'description': 'Theme target state', 'Enum': 'enabled, paused, archived'}
                | '**bid**': *number*, {'description': 'The bid amount'}

        Returns:
            | ApiResponse
        """
        headers = {'Accept': 'application/vnd.sbthemesupdateresponse.v3+json'}
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)