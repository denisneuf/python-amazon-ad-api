from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class AdvertisingUserPermissions(Client):
    @sp_endpoint('/userPermissions', method='PUT')
    def update_user_permissions(self, **kwargs) -> ApiResponse:
        r"""
        update_user_permissions(body: (dict, str)) -> ApiResponse

        Update the permissions of one or more users on an advertising account.

        body: | Optional
            | **userPermissions** (list[dict]) One entry per user.
            |     **userId** (string) User ID of the user having their permissions updated.
            |     **permissionSet** (dict) The permission set to grant.
            |     **countryCodes** (list[str]) Two-letter ISO 3166 codes.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.MinosAuthorizationNativeServicePublicAPI.UpdateUserPermissionsResource.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/userPermissions/delete', method='POST')
    def delete_user_permissions(self, **kwargs) -> ApiResponse:
        r"""
        delete_user_permissions(body: (dict, str)) -> ApiResponse

        Remove the permissions of one or more users.

        body: | Optional
            | **users** (list[dict]) One entry per user, each with **userId** (string).

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.MinosAuthorizationNativeServicePublicAPI.DeleteUserPermissionsResource.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/userPermissions/list', method='POST')
    def query_user_permissions(self, **kwargs) -> ApiResponse:
        r"""
        query_user_permissions(body: (dict, str)) -> ApiResponse

        List the permissions of a user on an advertising account.

        body: | REQUIRED
            | **userId** (string) User ID for the request.
            | **accessScopeFilter** (dict) {'include': [AccessScope]}
            | **countryCodesFilter** (dict) {'include': [CountryCode]}
            | **maxResults** (number) Max results for pagination.
            | **nextToken** (string) The pagination token.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.queryuserpermissions.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/userRoles/list', method='POST')
    def query_user_roles(self, **kwargs) -> ApiResponse:
        r"""
        query_user_roles(body: (dict, str)) -> ApiResponse

        List the roles of a user on an advertising account.

        body: | REQUIRED
            | **userId** (string) User ID of the target of the query.
            | **countryCodesFilter** (dict) {'include': [CountryCode]}
            | **maxResults** (number) Max results for pagination.
            | **nextToken** (string) The pagination token.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.queryuserroles.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/users/list', method='POST')
    def list_users(self, **kwargs) -> ApiResponse:
        r"""
        list_users(body: (dict, str)) -> ApiResponse

        List the users of an advertising account.

        body: | Optional
            | **accessScopeFilter** (dict) {'include': [AccessScope]}
            | **countryCodesFilter** (dict) {'include': [CountryCode]}
            | **maxResults** (number) Max results for pagination.
            | **nextToken** (string) The pagination token.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.listusers.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)
