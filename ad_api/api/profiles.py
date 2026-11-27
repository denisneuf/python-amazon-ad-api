from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils
import json


class Profiles(Client):
    @sp_endpoint('/v2/profiles', method='GET', headers=[])
    def list_profiles(self, **kwargs) -> ApiResponse:
        r"""

        list_profiles(self, **kwargs) -> ApiResponse

        Gets a list of profiles.

            query **apiProgram**:*string* | Optional. Filters response to include profiles that have permissions for the specified Advertising API program only. Available values : billing, campaign, paymentMethod, store, report, account, posts

            query **accessLevel**:*string* | Optional. Filters response to include profiles that have specified permissions for the specified Advertising API program only. Available values : edit, view

            query **profileTypeFilter**:*string* | Optional. Filters response to include profiles that are of the specified types in the comma-delimited list. Available values : seller, vendor, agency

            query **validPaymentMethodFilter**:*string* | Optional. Filter response to include profiles that have valid payment methods. Available values : true, false


        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/v2/profiles', method='PUT', headers=[])
    @Utils.deprecated
    def update_single_profile_assistant(self, profile_id: int, daily_budget: int, **kwargs) -> ApiResponse:
        r"""
        update_single_profile_assistant(profile_id: int, daily_budget: int, **kwargs) -> ApiResponse

        Update the daily budget for one or more profiles. Note that this operation is only used for Sellers using Sponsored Products.

        '**profile_id**': *integer($int64)* | required {'description': 'The identifier of the profile.'}

        '**daily_budget**': *number*, | required  {'description': 'Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.'}

        '**\*\*kwargs**': You can add other keyword args like the original method (countryCode, currencyCode, timezone, accountInfo{}) but as they are read-only if you try to modify will get INVALID_ARGUMENT: Cannot modify "value" for profile
        Returns:

            ApiResponse

        """

        required = {
            'profileId': profile_id,
            'dailyBudget': daily_budget,
        }

        options = {}
        options.update({'path': kwargs.pop("path")})
        options.update({'method': kwargs.pop("method")})

        # The decorator injects its header list into kwargs, and this helper
        # copies everything left in kwargs into the body: drop it first or the
        # service answers 422 Unrecognized field "endpoint_headers".
        kwargs.pop('endpoint_headers', None)

        required.update(kwargs)

        data_str = json.dumps([required])
        return self._request(options.pop('path'), data=data_str, params=options)

    @sp_endpoint('/v2/profiles', method='PUT', headers=[])
    def update_profile(self, **kwargs) -> ApiResponse:
        r"""

        update_profile(body: (dict, list, str)) -> ApiResponse

        Update the daily budget for one or more profiles. Note that this operation is only used for Sellers using Sponsored Products.

        body: | REQUIRED {'description': 'An array of ad groups.}'

            | '**profileId**': *integer($int64)* | required {'description': 'The identifier of the profile.'}
            | '**countryCode**': *string* | readOnly {'description': 'The countryCode for a given country'}
            | '**currencyCode**': *string* | readOnly {'description': 'The currency used for all monetary values for entities under this profile.'}
            | '**dailyBudget**': *number* | required {'description': 'Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.'}
            | '**timezone**': *string* | readOnly {'description': 'The time zone used for all date-based campaign management and reporting.'}
            | '**accountInfo**': *AccountInfoAccountInfo* | readOnly {}

        Returns:

            ApiResponse

        """
        body = Utils.convert_body(kwargs.pop('body'))
        return self._request(kwargs.pop('path'), data=body, params=kwargs)

    @sp_endpoint('/v2/profiles/{}', method='GET', headers=[])
    def get_profile(self, profileId, **kwargs) -> ApiResponse:
        r"""

        get_profile(self, profileId, **kwargs) -> ApiResponse

        Gets a profile specified by identifier.

            path **profileId**:*number* | Required. The identifier of an existing profile Id.


        Returns:

            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), profileId), params=kwargs)
