from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class KeywordsRecommendations(Client):

    _ACCEPT = 'application/vnd.sbkeywordrecommendation.v3+json'

    @classmethod
    def _accept(cls):
        """Response media type the v3 contract declares for these routes."""
        return {"Accept": cls._ACCEPT}

    @sp_endpoint('/sb/recommendations/keyword', method='POST')
    def list_keywords_recommendations(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False),
                             params=kwargs, headers=self._accept())
