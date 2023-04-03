from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class TargetsV3(Client):

    @sp_endpoint('/sp/targets/list', method='POST')
    def list_product_targets(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        Listing product targets.

        Request Body (optional)

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spTargetingClause.v' + str(version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)

    @sp_endpoint('/sp/targets', method='POST')
    def create_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Creating product targets.

        Request Body (required)
            | '**campaignId**': *string*, {'description': 'The number or recommendations returned in a single page.'}
            | '**adGroupId**': *string*, {'description': 'The page number in the result set to return.'}
            | '**expression**'
                | '**value**': *string*, {'description': 'The expression value.'}
                |  '**type**': *string*, {'description': '[ queryBroadMatches, queryPhraseMatches, queryExactMatches, asinCategorySameAs, asinBrandSameAs, asinPriceLessThan, asinPriceBetween, asinPriceGreaterThan, asinReviewRatingLessThan, asinReviewRatingBetween, asinReviewRatingGreaterThan, asinSameAs, queryBroadRelMatches, queryHighRelMatches, asinSubstituteRelated, asinAccessoryRelated, asinAgeRangeSameAs, asinGenreSameAs, asinIsPrimeShippingEligible ]'}
            | '**state**': *string*, {'description': 'The current resource state.' , 'Enum': '[ enabled, paused, archived ]'}
            | '**expressionType**': *string*, {'description': '[ auto, manual ]'}
            | '**bid**': *float*, {'description': 'The bid for ads sourced using the target. Min / Max 0.02 / 1000'}


        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spTargetingClause.v' + str(version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }

        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)

    @sp_endpoint('/sp/targets', method='PUT')
    def edit_product_targets(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        Updating product targets.

        Request Body (required)
            | '**targetId**':  *string*, (required) {'description': 'The identifer of the campaign to which the keyword is associated.'}
            | '**state**': *string*, {'description': 'The current resource state.' , 'Enum': '[ enabled, paused, archived ]'}
            | '**bid**': *float* {'description': 'Bid associated with this keyword. Applicable to biddable match types only.'}
            | '**expression**'
            |       '**value**': *string*, The expression value.
            |       '**type**': *string*, The type of nagative targeting expression. You can only specify values for the following predicates: Enum : [ASIN_BRAND_SAME_AS, ASIN_SAME_AS]
            | '**expressionType**' Enum : [AUTO, MANUAL]

        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spTargetingClause.v' + str(version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }

        prefer_value = 'return=representation'
        if prefer:
            headers.update({"Prefer": prefer_value})

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)

    @sp_endpoint('/sp/targets/delete', method='POST')
    def delete_product_targets(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        Deleting product targets

        Request Body (required)
            | **targetIdFilter** {} : Filter product targets by the list of objectIds
                include [string] : list of productTargetIds as String to be used as filter. MinItems : 0, MaxItems :1000


        Returns
            ApiResponse
        """
        json_version = 'application/vnd.spTargetingClause.v' + str(version) + "+json"
        headers = {
            "Accept": json_version,
            "Content-Type": json_version
        }

        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)
