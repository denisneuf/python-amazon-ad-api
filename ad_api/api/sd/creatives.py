from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Creatives(Client):

    @sp_endpoint('/sd/creatives', method='GET')
    def list_creatives(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/sd/creatives', method='PUT')
    def edit_creatives(self, **kwargs) -> ApiResponse:
        # print(kwargs.get('body'))
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sd/creatives', method='POST')
    def create_creatives(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/sd/moderation/creatives', method='GET')
    def list_moderation_creatives(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/sd/creatives/preview', method='POST')
    def show_creative_preview(self, **kwargs) -> ApiResponse:
        #'not a valid key=value pair (missing equal-sign) in '
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)