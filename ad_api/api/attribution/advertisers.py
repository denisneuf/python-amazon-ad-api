from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Advertisers(Client):
    @sp_endpoint("/attribution/advertisers", method="GET")
    def get_advertisers(self, **kwargs) -> ApiResponse:
        """
        
        Use the response to determine whether to use either the macroTags or nonMacroTemplateTags resource to get tags for a certain publisher.

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)
