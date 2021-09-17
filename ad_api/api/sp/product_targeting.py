from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Targets(Client):

    @sp_endpoint('/v2/sp/targets', method='POST')
    def create_products_targets(self, **kwargs) -> ApiResponse:
        r"""
        create_products_targets(self, \*\*kwargs) -> ApiResponse:

        Creates one or more targeting expressions.

        body: | REQUIRED {'description': 'An array of asins objects.}'

            | '**campaignId**': *number*, {'description': 'The number or recommendations returned in a single page.'}
            | '**adGroupId**': *number*, {'description': 'The page number in the result set to return.'}
            | '**expression**'
            |       '**value**': *string*, {'description': 'The expression value.'}
            |       '**type**': *string*, {'description': '[ queryBroadMatches, queryPhraseMatches, queryExactMatches, asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween, asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs, queryBroadRelMatches, queryHighRelMatches, asinSubstituteRelated, asinAccessoryRelated, asinAgeRangeSameAs, asinGenreSameAs, asinIsPrimeShippingEligible ]'}
            | '**resolvedExpression**'
            |       '**value**': *string*, {'description': 'The expression value.'}
            |       '**type**': *string*, {'description': '[ queryBroadMatches, queryPhraseMatches, queryExactMatches, asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween, asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs, queryBroadRelMatches, queryHighRelMatches, asinSubstituteRelated, asinAccessoryRelated, asinAgeRangeSameAs, asinGenreSameAs, asinIsPrimeShippingEligible ]'}
            | '**expressionType**': *string*, {'description': '[ auto, manual ]'}
            | '**bid**': *number*, {'description': 'The bid for ads sourced using the target. Min / Max 0.02 / 1000'}

        Returns:

            ApiResponse


        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/targets', method='PUT')
    def edit_products_targets(self, **kwargs) -> ApiResponse:
        r"""
        edit_products_targets(self, \*\*kwargs) -> ApiResponse:

        Updates one or more targeting clauses.

        body: | REQUIRED {'description': 'An array of asins objects.}'

            | '**targetId**': *number*, {'description': 'The target id.'}
            | '**state**': *string*, {'description': '[ enabled, paused, archived ]'}
            | '**expression**'
            |       '**value**': *string*, {'description': 'The expression value.'}
            |       '**type**': *string*, {'description': '[ queryBroadMatches, queryPhraseMatches, queryExactMatches, asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween, asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs, queryBroadRelMatches, queryHighRelMatches, asinSubstituteRelated, asinAccessoryRelated, asinAgeRangeSameAs, asinGenreSameAs, asinIsPrimeShippingEligible ]'}
            | '**resolvedExpression**'
            |       '**value**': *string*, {'description': 'The expression value.'}
            |       '**type**': *string*, {'description': '[ queryBroadMatches, queryPhraseMatches, queryExactMatches, asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween, asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs, queryBroadRelMatches, queryHighRelMatches, asinSubstituteRelated, asinAccessoryRelated, asinAgeRangeSameAs, asinGenreSameAs, asinIsPrimeShippingEligible ]'}
            | '**expressionType**': *string*, {'description': '[ auto, manual ]'}
            | '**bid**': *number*, {'description': 'The bid for ads sourced using the target. Min / Max 0.02 / 1000'}

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/targets', method='GET')
    def list_products_targets(self, **kwargs) -> ApiResponse:
        r"""
        list_products_targets(self, \*\*kwargs) -> ApiResponse

        Gets a list of targeting clauses filtered by specified criteria.

            query **startIndex**:*integer* | Optional. 0-indexed record offset for the result set. Default value : 0

            query **count**:*integer* | Optional. Number of records to include in the paged response. Defaults to max page size.

            query **stateFilter**:*string* | Optional. The returned array is filtered to include only ad groups with state set to one of the values in the specified comma-delimited list. Available values : enabled, paused, archived, enabled, paused, enabled, archived, paused, archived, enabled, paused, archived Default value : enabled, paused, archived.

            query **campaignIdFilter**:*string* | Optional. A comma-delimited list of campaign identifiers.

            query **adGroupIdFilter**:*string* | Optional. Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list.

            query **targetIdFilter**:*string* | Optional. A comma-delimited list of target identifiers.

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/v2/sp/targets/{}', method='GET')
    def get_products_target(self, targetId, **kwargs) -> ApiResponse:
        r"""

        get_products_targets(self, targetId, \*\*kwargs) -> ApiResponse

        Get a targeting clause specified by identifier.

        :param targetId | Required. The target identifier.
        :type targetId path :*number*

        :returns:
            :200: Success. Get a targeting ApiResponse
            :401: Unauthorized

        """
        return self._request(fill_query_params(kwargs.pop('path'), targetId), params=kwargs)

    @sp_endpoint('/v2/sp/targets/{}', method='DELETE')
    def delete_products_target(self, targetId, **kwargs) -> ApiResponse:
        r"""

        delete_products_targets(self, targetId, \*\*kwargs) -> ApiResponse

        Archives a targeting clause.

            path **targetId**:*number* | Required. The target identifier.

        Returns:

            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), targetId), params=kwargs)

    @sp_endpoint('/v2/sp/targets/extended', method='GET')
    def list_products_targets_extended(self, **kwargs) -> ApiResponse:
        r"""
        list_products_targets_extended(self, \*\*kwargs) -> ApiResponse

        Gets a list of targeting clauses filtered by specified criteria.

            query **startIndex**:*integer* | Optional. 0-indexed record offset for the result set. Default value : 0

            query **count**:*integer* | Optional. Number of records to include in the paged response. Defaults to max page size.

            query **stateFilter**:*string* | Optional. The returned array is filtered to include only ad groups with state set to one of the values in the specified comma-delimited list. Available values : enabled, paused, archived, enabled, paused, enabled, archived, paused, archived, enabled, paused, archived Default value : enabled, paused, archived.

            query **campaignIdFilter**:*string* | Optional. A comma-delimited list of campaign identifiers.

            query **adGroupIdFilter**:*string* | Optional. Restricts results to keywords associated with ad groups specified by identifier in the comma-delimited list.

            query **targetIdFilter**:*string* | Optional. A comma-delimited list of target identifiers.

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/v2/sp/targets/extended/{}', method='GET')
    def get_products_target_extended(self, targetId, **kwargs) -> ApiResponse:
        r"""

        get_products_targets_extended(self, targetId, \*\*kwargs) -> ApiResponse

        Get a targeting clause specified by identifier.

            path **targetId**:*number* | Required. The target identifier.

        Returns:

            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), targetId), params=kwargs)

    @sp_endpoint('/v2/sp/targets/productRecommendations', method='POST')
    def get_products_targets_recommendations(self, **kwargs) -> ApiResponse:
        r"""
        get_products_targets_recommendations(self, \*\*kwargs) -> ApiResponse:

        Gets a list of recommended products for targeting.

            path **keyword**:*string* | Optional Unique exclude categoryId. A keyword for which to get recommended brands.
            path **categoryId**:*number* | Optional Unique exclude keyword. Gets the top 50 brands for the specified category identifier.


        Returns:

            ApiResponse


        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/sp/targets/brands', method='GET')
    def get_brand_targets(self, **kwargs) -> ApiResponse:
        r"""
        get_brand_targets(self, \*\*kwargs) -> ApiResponse:

        Gets a list of recommended products for targeting.

        body: | REQUIRED {'description': 'An array of asins objects.}'

            | '**pageSize**': *number*, {'description': 'The number or recommendations returned in a single page.'}
            | '**pageNumber**': *number*, {'description': 'The page number in the result set to return.'}
            | '**asins**': *string*, {'description': 'A list of ASINs.'}

        Returns:

            ApiResponse


        """
        return self._request(kwargs.pop('path'), params=kwargs)
