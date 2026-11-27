Profiles
========

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/reference/2/profiles
    * - **Specification**
      - https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml

Profiles represent an advertiser and their account's marketplace, and are used in all subsequent API calls via a management scope, Amazon-Advertising-API-Scope. Reports and all entity management operations are associated with a single profile. Advertisers cannot have more than one profile for each marketplace.

Advertisers who operate in more than one marketplace (for example, Amazon.com, Amazon.co.uk, Amazon.co.jp) will have only one profile associated with each marketplace. See `this link`_ for a list of marketplaces associated with each endpoint.

.. _this link: https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints

To retrieve your profile IDs, call the listProfiles operation, and include a valid authorization access token in the header. Use a profileId from the returned list as the value for the management scope (Amazon-Advertising-API-Scope) in the headers for subsequent API calls.


.. toctree::
    :maxdepth: 1
    :titlesonly:

    profiles/list_profiles
    profiles/get_profile
    profiles/update_single_profile_assistant
    profiles/update_profile

.. note::

   The vendor contract declares three operations: ``listProfiles``,
   ``getProfile`` and ``updateProfiles``. This class exposes four methods on
   top of them, because ``update_single_profile_assistant`` is a convenience
   over ``update_profile``: instead of building the request body yourself,
   you pass ``profile_id`` and ``daily_budget`` and the method wraps them in
   the array the service expects.

   The four ``register`` operations that used to live here were removed in
   2.1.16. They targeted the sandbox test environment, which Amazon has
   retired: both ``/v2/profiles/register`` and ``/v2/profiles/registerBrand``
   answer ``404 NOT_FOUND``. They are not part of the 3.0 contract.

.. autoclass:: ad_api.api.Profiles
    :members:
    :member-order: bysource
    :noindex:

    ### Example getting a list of profiles

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def list_profiles(**kwargs):

            logging.info("-------------------------------------")
            logging.info("Profiles > list_profiles(%s)" % kwargs)
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).list_profiles(
                    **kwargs
                )
                logging.info(result)

                accounts_info = result.payload

                for account_info in accounts_info:
                    logging.info(account_info)

            except AdvertisingApiException as error:
                logging.info(error)

        list_profiles()
        # list_profiles(profileTypeFilter="seller")
        # list_profiles(profileTypeFilter="vendor")
        # list_profiles(profileTypeFilter="agency")
        # list_profiles(accessLevel="edit")
        # list_profiles(apiProgram="store")
        # list_profiles(validPaymentMethodFilter="true")

    ### Example updating the budget of a single profile

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def update_single_profile_assistant(account_profile_id: int, account_daily_budget: float, **kwargs):

            logging.info("-------------------------------------")
            logging.info("Profiles > update_single_profile_assistant({}, {}, {})".format(str(account_profile_id), str(account_daily_budget), str(kwargs)))
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).update_single_profile_assistant(
                    profile_id=account_profile_id,
                    daily_budget=account_daily_budget,
                    **kwargs

                )
                logging.info(result)
                payload = result.payload
                logging.info(payload)

            except AdvertisingApiException as error:
                logging.info(error)

        amz_profile_id = 1495806522428699
        amz_daily_budget = 21.50
        update_single_profile_assistant(amz_profile_id, amz_daily_budget)
        # update_single_profile_assistant(amz_profile_id, amz_daily_budget, countryCode="ES", timezone="Europe/London")

    ### Example updating the budget of one or more profiles

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def update_profile(data: (dict, list, str)):

            logging.info("-------------------------------------")
            logging.info("Profiles > update_profile(%s)" % str(data))
            logging.info("-------------------------------------")

            try:
                result = Profiles(account=store, debug=True).update_profile(
                    body=data
                )
                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        amz_profile_id = 1495806522428699
        amz_daily_budget = 21.50

        # Using a dict wrapped in a list. Note: countryCode, currencyCode, timezone and accountInfo are read only
        # try to update this fields will lead to INVALID ARGUMENT so in my opinion better no need to send unless
        # you store the data and you retrieve all the fields

        update_data_list = \
        [
            {
                'profileId': amz_profile_id,
                'dailyBudget': amz_daily_budget,
                'countryCode': 'ES',
                'currencyCode': 'EUR',
                'timezone': 'Europe/Paris',
                'accountInfo': {
                    'id': 'A30E1B2F3U4K5Y',
                     'marketplaceStringId': 'A1RKKUPIHCS9HS',
                     'type': 'seller'
                }
            }
        ]

        update_profile(update_data_list)

        # The most simple and useful way to update the budget of a single profile
        update_data_dict = \
        {
            'profileId': amz_profile_id,
            'dailyBudget': amz_daily_budget,
        }

        update_profile(update_data_dict)

        # The most simple and useful way to update the budget of a bunch of profiles

        update_profiles_list = \
        [
            {
                'profileId': 1495806522428699,
                'dailyBudget': 10.5,
            },
            {
                'profileId': 1495806522428698,
                'dailyBudget': 20,
            }
        ]

        update_profile(update_profiles_list)

    ### Example getting a profiles by profileId

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def get_profile(profile_id: int):

            logging.info("-------------------------------------")
            logging.info("Profiles > get_profile(%s)" % profile_id)
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).get_profile(
                    profileId=profile_id
                )
                logging.info(result)

                profile_info = result.payload

            except AdvertisingApiException as error:
                logging.info(error)

        amz_profile_id = 1495806522428699
        get_profile(amz_profile_id)


