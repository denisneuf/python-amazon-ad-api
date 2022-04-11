Profiles
=================

.. autoclass:: ad_api.api.Profiles

    Profiles represent an advertiser and their account's marketplace, and are used in all subsequent API calls via a management scope, Amazon-Advertising-API-Scope. Reports and all entity management operations are associated with a single profile. Advertisers cannot have more than one profile for each marketplace.

    Advertisers who operate in more than one marketplace (for example, Amazon.com, Amazon.co.uk, Amazon.co.jp) will have only one profile associated with each marketplace. See `this link`_ for a list of marketplaces associated with each endpoint.

    .. _this link: https://advertising.amazon.com/API/docs/en-us/info/api-overview#api-endpoints

    To retrieve your profile IDs, call the listProfiles operation, and include a valid authorization access token in the header. Use a profileId from the returned list as the value for the management scope (Amazon-Advertising-API-Scope) in the headers for subsequent API calls.

    `Profiles 3.0`_.

    .. _Profiles 3.0: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/profiles/3-0/openapi.yaml

    .. autofunction:: ad_api.api.Profiles.list_profiles

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

    .. autofunction:: ad_api.api.Profiles.update_single_profile_assistant

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

    .. autofunction:: ad_api.api.Profiles.update_profile

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


    .. autofunction:: ad_api.api.Profiles.get_profile

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


    .. warning::

       Note that this **register_brand_assistant** operation is only used for SANDBOX test environment.

    .. autofunction:: ad_api.api.Profiles.register_brand_assistant

    ### Example creating a Vendor profile for sandbox

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def register_brand_assistant(country_code: str, brand: str):

            logging.info("-------------------------------------")
            logging.info("Profiles > register_brand_assistant({},{})".format(country_code, brand))
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).register_brand_assistant(
                    country_code=country_code,
                    brand=brand
                )
                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        amz_country_code = "UK"
        vendor_brand = "LEADTECH"

        register_brand_assistant(amz_country_code, vendor_brand)

    .. warning::

       Note that this **register_brand** operation is only used for SANDBOX test environment.

    .. autofunction:: ad_api.api.Profiles.register_brand

    ### Example creating a Vendor profile for sandbox with a regular dict

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def register_brand(dictionary: dict):

        logging.info("-------------------------------------")
        logging.info("Profiles > register_brand(%s)" % str(dictionary))
        logging.info("-------------------------------------")

        try:

            result = Profiles(account=store, debug=True).register_brand(
                body=dictionary
            )
            logging.info(result)

        except AdvertisingApiException as error:
            logging.info(error)

        amz_dict_brand = \
        {
            'countryCode': amz_country_code,
            'brand': vendor_brand
        }

        register_brand(amz_dict_brand)


    .. warning::

       Note that this **register_assistant** is only used for SANDBOX test environment. Using in PRODUCTION will get a
       AdvertisingApiException: {'status_code': 404, 'code': 'NOT_FOUND', 'details': 'HTTP 404 Not Found', 'requestId': 'HEMG4AR2NRF5HCW8BH8S'}

    .. note::
        You only can create one profile per country, If you try to create again the same country will get a
        Payload: {'profileId': 81562378459925, 'status': 'SUCCESS', 'statusDetails': 'Merchant is already registered'}

    .. autofunction:: ad_api.api.Profiles.register_assistant

    ### Example creating a profiles por a specific country

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def register_assistant(value: str):

            logging.info("-------------------------------------")
            logging.info("Profiles > register_assistant(%s)" % value)
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).register_assistant(
                    country_code=value
                )
                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        amz_country_code = "DE"
        register_assistant(amz_country_code)


    ### Payload

    .. code-block:: python

        {
            'registerProfileId': '82465ad1-e8cd-4d24-beb0-5cb8423f4260DE',
            'status': 'IN_PROGRESS',
            'statusDetails': 'Registration workflow has been started'
        }


    .. warning::

       Note that this **register** operation is only used for SANDBOX test environment.

    .. autofunction:: ad_api.api.Profiles.register

    ### Example creating a profiles por a specific country with a dict

    .. code-block:: python

        import logging
        from ad_api.api import Profiles
        from ad_api.base import AdvertisingApiException

        def register(dictionary: dict):

            logging.info("-------------------------------------")
            logging.info("Profiles > register(%s)" % str(dictionary))
            logging.info("-------------------------------------")

            try:

                result = Profiles(account=store, debug=True).register(
                    body=dictionary
                )
                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

            amz_country_code = "DE"
            amz_dict_country_code = \
                {
                    "countryCode": amz_country_code
                }

            register(amz_dict_country_code)