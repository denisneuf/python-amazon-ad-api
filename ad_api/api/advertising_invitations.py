from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class AdvertisingInvitations(Client):
    @sp_endpoint('/user-invitations', method='POST')
    def create_user_invitations(self, **kwargs) -> ApiResponse:
        r"""
        create_user_invitations(body: (dict, str)) -> ApiResponse

        Invite users to an advertising account.

        body: | REQUIRED
            | **userInvitationRequests** (list[dict]) List of invitations to be sent to users.
            |     **user** (dict) {'emailAddress': string, 'userName': string} both required.
            |     **permissionSet** (dict) {'type': 'ROLE' | 'CUSTOM_PERMISSION_SET', 'role': {'name': string}, 'customPermissionSet': [{'name': string}]}
            |     **countries** (list[dict]) [{'countryCode': string}] two-letter ISO 3166 codes.
            | **notifyInvitedUsers** (boolean) Indicates if an invitation email will be sent to the invited user.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.CreateUserInvitations.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/user-invitations', method='PUT')
    def update_user_invitations(self, **kwargs) -> ApiResponse:
        r"""
        update_user_invitations(body: (dict, str)) -> ApiResponse

        Update a set of invitations, for example to revoke them.

        body: | REQUIRED
            | **updates** (list[dict]) List of updates to perform for a set of invitations.
            |     **invitationId** (string) Identifier of the invitation you want to update.
            |     **state** (string) State to change your invitation to. Supported states: REVOKE.
            | **notifyInvitedUsers** (boolean) Indicates if an invitation email will be sent to the invited user.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.UpdateUserInvitations.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/user-invitations/list', method='POST')
    def list_user_invitations(self, **kwargs) -> ApiResponse:
        r"""
        list_user_invitations(body: (dict, str)) -> ApiResponse

        List the invitations of an advertising account.

        body: | Optional
            | **maxResults** (number) Max results to fetch per page.
            | **nextToken** (string) Identifier of the next pagination token.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.ListUserInvitations.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/user-invitations/redeem', method='PUT')
    def redeem_user_invitation(self, **kwargs) -> ApiResponse:
        r"""
        redeem_user_invitation(body: (dict, str)) -> ApiResponse

        Redeem an invitation.

        body: | REQUIRED
            | **invitationId** (string) Identifier of the invitation to be redeemed.

        The contract declares no 2xx response for this operation, only 400, 403,
        404 and 500.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.RedeemUserInvitation.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/user-invitations/{}', method='GET')
    def get_user_invitation(self, invitationId: str, **kwargs) -> ApiResponse:
        r"""
        get_user_invitation(invitationId: str) -> ApiResponse

        Request the attributes of a given invitation.

        path **invitationId**:string | Required. Identifier of the invitation.

        Returns:

            ApiResponse

        """
        schema_version = 'application/vnd.GetUserInvitation.v1+json'
        headers = {'Accept': schema_version, 'Content-Type': schema_version}

        return self._request(fill_query_params(kwargs.pop('path'), invitationId), params=kwargs, headers=headers)
