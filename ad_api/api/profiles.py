from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse

class Profiles(Client):
    """
    Profiles AD-API Client
    :link:
    With the Profiles.
    """

    @sp_endpoint('/v2/profiles', method='GET')
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

    @sp_endpoint('/v2/profiles', method='PUT')
    def update_profile(self, **kwargs) -> ApiResponse:
        r"""

        update_profile(self, **kwargs) -> ApiResponse

        Update the daily budget for one or more profiles. Note that this operation is only used for Sellers using Sponsored Products.

        body: | REQUIRED {'description': 'An array of ad groups.}'

            | '**profileId**': *integer($int64)*, {'description': 'The identifier of the profile.'}
            | '**countryCode**': *string*, {'description': 'The countryCode for a given country'}
            | '**currencyCode**': *string*, {'description': 'The currency used for all monetary values for entities under this profile.'}
            | '**dailyBudget**': *number*, {'description': 'Note that this field applies to Sponsored Product campaigns for seller type accounts only. Not supported for vendor type accounts.'}
            | '**timezone**': *string*, {'description': 'The time zone used for all date-based campaign management and reporting.'}
            | '**accountInfo**': *AccountInfoAccountInfo*, {}

        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/profiles/{}', method='GET')
    def get_profile(self, profileId, **kwargs) -> ApiResponse:
        r"""

        get_profile(self, profileId, **kwargs) -> ApiResponse

        Gets a profile specified by identifier.

            path **profileId**:*number* | Required. The identifier of an existing profile Id.


        Returns:

            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), profileId), params=kwargs)


    @sp_endpoint('/v2/profiles/registerBrand', method='PUT')
    def register_brand(self, **kwargs) -> ApiResponse:
        r"""

        register_brand(self, **kwargs) -> ApiResponse

        SANDBOX ONLY - Create a vendor profile for sandbox.

        body: | REQUIRED

            '**countryCode**': *string*, {'description': 'The countryCode for a given country'}
            '**brand**': *string*, {'description': 'The brand for the vendor account'}


        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)

    @sp_endpoint('/v2/profiles/register', method='PUT')
    def register(self, **kwargs) -> ApiResponse:
        r"""

        register_brand(self, \*\*kwargs) -> ApiResponse

        SANDBOX ONLY - Create a seller profile for sandbox.

        body: REQUIRED

            '**countryCode**': *string*, {'description': 'The countryCode for a given country'}


        Returns:

            ApiResponse

        """
        return self._request(kwargs.pop('path'), data=kwargs.pop('body'), params=kwargs)
