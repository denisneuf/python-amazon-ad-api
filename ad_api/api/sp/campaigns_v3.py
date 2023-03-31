from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils
import os
import json
from json.decoder import JSONDecodeError
from io import TextIOWrapper


class CampaignsV3(Client):
    r"""
    Campaigns(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API - Sponsored Products

    """

    @sp_endpoint('/sp/campaigns/list', method='POST')
    def list_campaigns(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        """
        schema_version = 'application/vnd.spCampaign.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
