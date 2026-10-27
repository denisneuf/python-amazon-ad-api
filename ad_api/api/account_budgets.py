from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class AccountBudgets(Client):
    """ """

    @sp_endpoint('/accountBudgets/featureFlags', method='GET')
    def get_feature_flags(self, **kwargs) -> ApiResponse:
        r"""
        Reports whether the account has opted out of automatic budget increases.

        Returns
            ApiResponse with a ``featureFlags`` object holding one member,
            ``isOptedOutForAverageDailyBudgetIncrease``. At ``true`` the account
            has opted out, and the service will not raise a campaign's daily
            budget on its own; at ``false`` it may.

        """
        headers = {'Accept': 'application/vnd.accountBudgetFeatureFlags.v1+json'}
        return self._request(kwargs.pop('path'), params=kwargs, headers=headers)

    @sp_endpoint('/accountBudgets/featureFlags', method='POST')
    def update_feature_flags(self, **kwargs) -> ApiResponse:
        r"""
        Changes whether the account opts out of automatic budget increases.

        Request Body (required)

        - ``featureFlags`` (object): required. A ``FeatureFlags`` object holding
          ``isOptedOutForAverageDailyBudgetIncrease``. Set it to ``true`` to stop
          the service raising daily budgets on its own, ``false`` to allow it.

        .. warning::

            This changes how the account is charged. With the flag at ``false``
            the service may raise a campaign's daily budget without another call
            from you, and spend follows the budget. Not exercised here: the
            setting belongs to the account holder.

        Returns
            ApiResponse with ``code`` and ``details``, not with the flags read
            back. ``code`` is ``OK``, ``ENTRY_NOT_FOUND`` or
            ``INVALID_PARAMETER_VALUE``, so a ``200`` carrying something other
            than ``OK`` means the change did not land. Read the flags again with
            ``get_feature_flags`` to confirm.

        """
        headers = {
            'Accept': 'application/vnd.accountBudgetFeatureFlags.v1+json',
            'Content-Type': 'application/vnd.accountBudgetFeatureFlags.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)
