from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils

class CampaignNegativeKeywordsV3(Client):

    @sp_endpoint('/sp/campaignNegativeKeywords/list', method='POST')
    def list_campaign_negative_keywords(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        """
        schema_version = 'application/vnd.spCampaignNegativeKeyword.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)

    @sp_endpoint('/sp/campaignNegativeKeywords/delete', method='POST')
    def delete_campaign_negative_keyword(self, **kwargs) -> ApiResponse:
        r"""
        """
        schema_version = 'application/vnd.spCampaignNegativeKeyword.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)

    @sp_endpoint('/sp/campaignNegativeKeywords', method='POST')
    def create_campaign_negative_keywords(self, **kwargs) -> ApiResponse:
        r"""

        """
        schema_version = 'application/vnd.spCampaignNegativeKeyword.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)


    @sp_endpoint('/sp/campaignNegativeKeywords', method='PUT')
    def edit_campaign_negative_keywords(self, **kwargs) -> ApiResponse:
        r"""

        """
        schema_version = 'application/vnd.spCampaignNegativeKeyword.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs,
                             headers=headers)
