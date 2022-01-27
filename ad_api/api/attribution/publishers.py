from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Publishers(Client):
    @sp_endpoint("/attribution/publishers", method="GET")
    def get_publishers(self, **kwargs) -> ApiResponse:
        """

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)
