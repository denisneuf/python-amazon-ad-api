from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils
import os
import json
from json.decoder import JSONDecodeError
from io import TextIOWrapper


class CampaignsV3(Client):
    r"""
    Amazon Ads API - Sponsored Products
    """

    @sp_endpoint('/sp/campaigns', method='POST')
    def create_campaigns(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        create_campaigns(body: (dict, str, list)) -> ApiResponse
        """
        schema_version = 'application/vnd.spCampaign.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation' # return=minimal
        if prefer:
            headers.update({"Prefer": prefer_value})
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaigns', method='PUT')
    def edit_campaigns(self, version: int = 3, prefer: bool = False, **kwargs) -> ApiResponse:
        r"""
        edit_campaigns(body: (dict, str, list)) -> ApiResponse
        """
        schema_version = 'application/vnd.spCampaign.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        prefer_value = 'return=representation' # return=minimal
        if prefer:
            headers.update({"Prefer": prefer_value})
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaigns/list', method='POST')
    def list_campaigns(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        list_campaigns(body: (dict, str, list)) -> ApiResponse
        """
        schema_version = 'application/vnd.spCampaign.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/sp/campaigns/delete', method='POST')
    def delete_campaigns(self, version: int = 3, **kwargs) -> ApiResponse:
        r"""
        delete_campaigns(body: (dict, str, list)) -> ApiResponse
        """
        schema_version = 'application/vnd.spCampaign.v' + str(version) + '+json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)