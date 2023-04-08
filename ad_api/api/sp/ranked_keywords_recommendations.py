from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils

class RankedKeywordsRecommendations(Client):
    """
    Sponsored Products Targeting API.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod#/

    Specification: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

    """

    @sp_endpoint('/sp/targets/keywords/recommendations', method='POST')
    def list_ranked_keywords_recommendations(self, version: int = 3, **kwargs) -> ApiResponse:


        r"""
        Get keyword recommendations

        Request Body (oneOf)
            | This request type is used to retrieve recommended keyword targets for an existing ad group. Set the recommendationType to KEYWORD_FOR_ADGROUP to use this request type.

            | AdGroupKeywordTargetRankRecommendationRequest {
            | **maxRecommendations** (number): The max size of recommended target. Set it to 0 if you only want to rank user-defined keywords. default: 200 maximum: 200 minimum: 0
            | **sortDimension** (string): The ranking metric value. Supported values: CLICKS, CONVERSIONS, DEFAULT. DEFAULT will be applied if no value passed in. Enum: ['CLICKS', 'CONVERSIONS', 'DEFAULT']
            | **locale** (string): Translations are for readability and do not affect the targeting of ads. Supported marketplace to locale mappings can be found at the <a href='https://advertising.amazon.com/API/docs/en-us/localization/#/Keyword%20Localization'>POST /keywords/localize</a> endpoint. Note: Translations will be null if locale is unsupported. Enum: ['ar_EG', 'de_DE', 'en_AE', 'en_AU', 'en_CA', 'en_GB', 'en_IN', 'en_SA', 'en_SG', 'en_US', 'es_ES', 'es_MX', 'fr_FR', 'it_IT', 'ja_JP', 'nl_NL', 'pl_PL', 'pt_BR', 'sv_SE', 'tr_TR', 'zh_CN']
            | **targets** [
            | minItems: 0. maxItems: 100. A list of targets that need to be ranked.
            |   {
            |    **matchType** (string): Keyword match type. The default value will be BROAD. Enum: ['BROAD', 'EXACT', 'PHRASE']
            |    **keyword** (string): The keyword value
            |    **bid** number (double): The bid value for the keyword. The default value will be the suggested bid.
            |    **userSelectedKeyword** (boolean): Flag that tells if keyword was selected by the user or was recommended by KRS
            |   }
            | ]
            | **campaignId**\*(string): The identifier of the campaign
            | **recommendationType**\*(string): The recommendationType to retrieve recommended keyword targets for an existing ad group. Enum: ['KEYWORDS_FOR_ADGROUP']
            | **dGroupId**\*(string): The identifier of the ad group
            | }

            | This request type is used to retrieve recommended keyword targets for ASINs. Set the recommendationType to KEYWORD_FOR_ASINS to use this request type.

            | AsinsKeywordTargetRankRecommendationRequest {
            | **maxRecommendations** (number): The max size of recommended target. Set it to 0 if you only want to rank user-defined keywords. default: 200 maximum: 200 minimum: 0
            | **sortDimension** (string): The ranking metric value. Supported values: CLICKS, CONVERSIONS, DEFAULT. DEFAULT will be applied if no value passed in. Enum: ['CLICKS', 'CONVERSIONS', 'DEFAULT']
            | **locale** (string): Translations are for readability and do not affect the targeting of ads. Supported marketplace to locale mappings can be found at the <a href='https://advertising.amazon.com/API/docs/en-us/localization/#/Keyword%20Localization'>POST /keywords/localize</a> endpoint. Note: Translations will be null if locale is unsupported. Enum: ['ar_EG', 'de_DE', 'en_AE', 'en_AU', 'en_CA', 'en_GB', 'en_IN', 'en_SA', 'en_SG', 'en_US', 'es_ES', 'es_MX', 'fr_FR', 'it_IT', 'ja_JP', 'nl_NL', 'pl_PL', 'pt_BR', 'sv_SE', 'tr_TR', 'zh_CN']
            | **targets** [
            | minItems: 0. maxItems: 100. A list of targets that need to be ranked.
            |   {
            |    **matchType** (string): Keyword match type. The default value will be BROAD. Enum: ['BROAD', 'EXACT', 'PHRASE']
            |    **keyword** (string): The keyword value
            |    **bid** number (double): The bid value for the keyword. The default value will be the suggested bid.
            |    **userSelectedKeyword** (boolean): Flag that tells if keyword was selected by the user or was recommended by KRS
            |   }
            | **asins**\* (array) maxItems: 50. An array list of Asin.
            | **recommendationType**\* (string): The recommendationType to retrieve recommended keyword targets for a list of ASINs. Enum: ['KEYWORDS_FOR_ASINS']
            | }
        """

        contentType = 'application/vnd.spkeywordsrecommendation.v' + str(version) + "+json"
        headers = {'Content-Type': contentType}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
