Campaigns
=========

.. deprecated:: 4.0.2

.. warning::

    There is a new version 3 of Sponsored Product API, please check the `migration guide`_.



.. autoclass:: ad_api.api.sp.Campaigns

    .. warning::

        This method is a helper that basically will build the json body for you based on params. If you are happy building your own dictinary and passing to the api as json you could use the **create_campaigns** method who follow the Amazon api strictly accepting only the keyword argument body which is a json string and allow to create more than one campaign at the same time.

    .. autofunction:: ad_api.api.sp.Campaigns.create_single_campaign_assistant

    .. note::

        The minimal campaign should contain at least a campaign_name, targeting_type, daily_budget and start_date. Once set-up the targeting type, auto or manual, cannot be edited.

    .. note::

        If the targeting_type="auto" it cannot combine with premium_bid_adjustment=True. INVALID_ARGUMENT: Cannot have premium bid adjustment on auto targeted campaign. Ignore the premium_bid_adjustment will result in 'premiumBidAdjustment': False.


    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def create_single_campaign_assistant(**kwargs):
        try:

            result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).create_single_campaign_assistant(
                **kwargs
            )

            logging.info(result)

        except AdvertisingApiException as error:
            logging.info(error)


        if __name__ == '__main__':

            # Create a campaign targeting auto
            create_single_campaign_assistant(
                campaign_name="Test Auto Basic",
                targeting_type="auto",
                start_date="20220415",
                daily_budget=5
                )

            # Create a campaign targeting manual
            create_single_campaign_assistant(
                campaign_name="Test Manual Basic",
                targeting_type="manual",
                start_date="20220415",
                daily_budget=7.0
                )

            # Create a campaign targeting manual with single adjustment
            create_single_campaign_assistant(
                campaign_name="Test targeting_type manual strategy + Predicate + Percentage",
                targeting_type="manual",
                start_date="20220415",
                daily_budget=20.5,
                strategy="autoForSales",
                predicate="placementProductPage",
                percentage=25
            )

            # Create a campaign targeting manual with complete adjustments as tuple
            create_single_campaign_assistant(
                campaign_name="Test targeting_type manual strategy + Tuple Predicate + Percentage",
                targeting_type="manual",
                start_date="20220415",
                daily_budget=20.5,
                strategy="legacyForSales",
                predicate=("placementProductPage", "placementTop"),
                percentage=(10, 15)
            )

            # Note that automatically create 'premiumBidAdjustment': True,
            '''

            {
                'bidding':
                    {
                        'adjustments':
                            [
                                {
                                    'percentage': 10,
                                    'predicate': 'placementProductPage'
                                },
                                {
                                    'percentage': 15,
                                    'predicate': 'placementTop'
                                }
                            ],
                            'strategy': 'legacyForSales'
                    },
                'campaignId': 21102815236563,
                'campaignType': 'sponsoredProducts',
                'creationDate': 1649301115000,
                'dailyBudget': 20.5,
                'lastUpdatedDate': 1649301115000,
                'name': 'Test targeting_type manual // strategy + Tuple Predicate + Percentage',
                'premiumBidAdjustment': True,
                'servingStatus': 'PENDING_START_DATE',
                'startDate': '20220415',
                'state': 'enabled',
                'targetingType': 'manual'
            }

            '''

            # Create a complete campaign targeting manual with premium_bid_adjustment True
            create_single_campaign_assistant(
                campaign_name="Test manual + premium_bid_adjustment True",
                targeting_type="manual",
                campaign_status="paused",
                start_date="20220415",
                end_date="20230415",
                daily_budget=25.00,
                portfolio_id=141331265528226,
                po_number="23774",
                account_manager="exampleAccountManager",
                premium_bid_adjustment=True,
            )

            # Note that adjustments are automaticallly created {'adjustments': [{'percentage': 50, 'predicate': 'placementTop'}], 'strategy': 'legacyForSales'}
            '''

            {
                'bidding':
                    {
                    'adjustments':
                        [
                            {
                                'percentage': 50,
                                'predicate': 'placementTop'
                            }
                        ],
                        'strategy': 'legacyForSales'},
                        'campaignId': 189457270490886,
                        'campaignType': 'sponsoredProducts',
                        'creationDate': 1649302267000,
                        'dailyBudget': 25.0,
                        'endDate': '20230415',
                        'lastUpdatedDate': 1649302267000,
                        'name': 'Test manual + premium_bid_adjustment True',
                        'portfolioId': 141331265528226,
                        'premiumBidAdjustment': True,
                        'servingStatus': 'CAMPAIGN_PAUSED',
                        'startDate': '20220415',
                        'state': 'paused',
                        'tags':
                            {
                                'PONumber': '23774',
                                'accountManager': 'exampleAccountManager'
                            },
                        'targetingType': 'manual'
                }
            }

            '''

    .. warning::

       This method is a helper that basically will build the json body for you based on params. If you are happy building your own dictinary and passing to the api as json you could use the **edit_campaign** method who follow the Amazon api strictly accepting only the keyword argument body which is a json string.


    .. autofunction:: ad_api.api.sp.Campaigns.edit_single_campaign_assistant

    .. note::

        If the targeting_type="manual" and premium_bid_adjustment=True it results in {'bidding': {'adjustments': [{'percentage': 50, 'predicate': 'placementTop'}], 'strategy': 'legacyForSales'} The premium_bid_adjustment can be edited to premium_bid_adjustment=False, even without providing, predicate and percentage. The result is {'bidding': {'adjustments': [], 'strategy': 'legacyForSales'} and is allowed to roll back to premium_bid_adjustment=True

    .. note::

        If you already set some adjustments automatically is set 'premiumBidAdjustment': True, so if you try only set to False. INVALID_ARGUMENT: Campaign has been adopted to enhanced bidding controls. 'premiumBidAdjustment' can not be set any more. If you want reset the adjustments you need pass (...,strategy="legacyForSales",predicate=("placementProductPage", "placementTop"),percentage=(0, 0),...). The percentage 0 reset and clean the adjustments. Since no adjustments you can edit again and set premium_bid_adjustment=True. After that you could set premium_bid_adjustment=True or define a strategy, predicate and percent which will make premiumBidAdjustment=True but not both. INVALID_ARGUMENT: Either 'premiumBidAdjustment' or enhanced bidding controls should be specified, but not both.


    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def edit_single_campaign_assistant(**kwargs):
            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).edit_single_campaign_assistant(
                    **kwargs
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            sp_campaign_id = 21102815236563

            # Updating the budget and reset to False the premium_bid_adjustment
            edit_single_campaign_assistant(
                campaign_id=sp_campaign_id,
                daily_budget=28.5,
                strategy="legacyForSales",
                predicate=("placementProductPage", "placementTop"),
                percentage=(0, 0)
            )



    .. autofunction:: ad_api.api.sp.Campaigns.create_campaigns

    .. versionadded:: 0.2.7
        The support to pass the body as dictionary, list, path to file or content of file.

    .. warning::

       The **regular way** to create a campaign is pass a keyword argument body as JSON string but now we could support a variety of other types and will cast to feed the right string in JSON format


    ### Example Sending a dictionary or a list

    .. code-block:: python

        import logging
        import json
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def create_campaigns(data: (dict, list)):

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).create_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        # If you submit a dictionary the method create_campaigns(body=data) will check if is a
        # instance of dict and wrap and dumps in JSON string: body = json.dumps([body])

        single_dictionary = \
        {
            'name': 'Campaign as a dict with no []',
            'campaignType': 'sponsoredProducts',
            'targetingType': 'auto',
            'state': 'paused',
            'dailyBudget': 9,
            'startDate': '20221230'
        }

        create_campaigns(single_dictionary)

        # If you submit a list[{dict},{dict}] which is a right way the wrapper will check if is a
        # instance of list and dumps in JSON string: body = json.dumps(body)
        # This allow you to create 1 or more campaigns at once.

        list_dictionary = \
            [
                {
                    'portfolioId': 214026257044134,
                    'name': 'Campaign manual bid true',
                    'tags': {
                        'PONumber': 'examplePONumber',
                        'accountManager': 'exampleAccountManager'
                    },
                    'campaignType': 'sponsoredProducts',
                    'targetingType': 'manual',
                    'state': 'enabled',
                    'dailyBudget': 22.0,
                    'startDate': '20220430',
                    'endDate': '20420430',
                    'premiumBidAdjustment': True,
                },
                {
                    'portfolioId': 214026257044134,
                    'name': 'Campaign manual adjustments true',
                    'tags': {
                      'PONumber': 'examplePONumber',
                      'accountManager': 'exampleAccountManager'
                    },
                    'campaignType': 'sponsoredProducts',
                    'targetingType': 'manual',
                    'state': 'enabled',
                    'dailyBudget': 22.0,
                    'startDate': '20220430',
                    'endDate': '20420430',
                    'bidding': {
                        'strategy': 'legacyForSales',
                        'adjustments':
                        [
                            {
                              'predicate': 'placementTop',
                              'percentage': 15
                            }
                        ]
                    }
                }
            ]

        create_campaigns(list_dictionary)
        # Note that you could dump by yourself the list[dict] as was the classical way
        # create_campaigns(json.dumps(list_dictionary))

    ### Example Sending a path to a .json file

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException, AdvertisingTypeException

        def create_campaigns(data: str):

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).create_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

            # Is possible to capture the exceptions if the json contains some errors
            # "<class 'json.decoder.JSONDecodeError'>",
            # JSONDecodeError('Expecting value: line 15 column 33 (char 431)'
            except AdvertisingTypeException as type_error:
                logging.info(type_error)

        file_name = "../test/campaigns/sp-sx-create-campaigns.json"

        create_campaigns(file_name)

        # Or More elegant in your side catching the FileNotFoundError
        '''
        try:

            with open(file_name, mode="r", encoding="utf-8") as file:
                create_campaigns(file_name)
                file.close()

        except FileNotFoundError as e:
            logging.info(e)
        '''


    ### Example Sending the content of a .json file

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException, AdvertisingTypeException

        def create_campaigns(data: str):

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).create_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)
            except AdvertisingTypeException as type_error:
                logging.info(type_error)


        file_name = "../test/campaigns/sp-sx-create-campaigns.json"

        # Read the file and call the create_campaigns(f) before closing the file or
        # will raise ValueError: I/O operation on closed file.

        try:

            with open(file_name, mode="r", encoding="utf-8") as file:
                f = file.read()
                create_campaigns(f)
                file.close()

        except FileNotFoundError as e:
            logging.info(e)


    ### Example json

    Download :download:`json <../../test/campaigns/sp-sx-create-campaigns.json>` the file to use:

    .. literalinclude:: ../../test/campaigns/sp-sx-create-campaigns.json

    .. autofunction:: ad_api.api.sp.Campaigns.edit_campaigns

    .. versionadded:: 0.2.7
        The support to pass the body as dictionary, list, path to file or content of file.

    .. warning::

       The **regular way** to create a campaign is pass a keyword argument body as JSON string but now we could support a variety of other types and will cast to feed the right string in JSON format

    ### Example Sending a dictionary or a list

    .. code-block:: python

        import logging
        import json
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def edit_campaigns(data: (dict, list)):
            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).edit_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        # If you submit a dictionary the method create_campaigns(body=data) will check if is a
        # instance of dict and wrap and dumps in JSON string: body = json.dumps([body])

        single_dictionary = \
            {
                'campaignId': 247123430252449,
                'state': 'enabled',
                'dailyBudget': 99,
            }

        edit_campaigns(single_dictionary)


        # If you submit a list[{dict},{dict}] which is a right way the wrapper will check if is a
        # instance of list and dumps in JSON string: body = json.dumps(body)
        # This allow you to create 1 or more campaigns at once.

        list_dictionary = \
            [
                {
                    'campaignId': 247123430252449,
                    'tags': {
                        'PONumber': '203384',
                        'accountManager': 'Manager003'
                    },
                    'state': 'enabled',
                    'dailyBudget': 29.0,
                },
                {
                    'campaignId': 1280722862611,
                    'state': 'paused',
                    'dailyBudget': 22.0,
                    'bidding': {
                        'strategy': 'legacyForSales',
                        'adjustments':
                        [
                            {
                                'predicate': 'placementTop',
                                'percentage': 20
                            },
                            {
                                'predicate': 'placementProductPage',
                                'percentage': 25
                            }
                        ]
                    }
                },
                {
                    'campaignId': 7164447325502,
                    'state': 'paused'
                }
            ]

        edit_campaigns(list_dictionary)

    ### Example Sending a path to a .json file

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def edit_campaigns(data: str):
            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).edit_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        file_name = "../test/campaigns/sp-sx-edit-campaigns.json"
        edit_campaigns(file_name)

    ### Example Sending the content of a .json file

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def edit_campaigns(data: str):
            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).edit_campaigns(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)



        file_name = "../test/campaigns/sp-sx-edit-campaigns.json"

        # Open the file or read, then call the create_campaigns(f) before closing the file or
        # will raise ValueError: I/O operation on closed file.

        try:

            with open(file_name, mode="r", encoding="utf-8") as file:

                # Is also possible to send the instance of TextIOWrapper
                # edit_campaigns(file)

                # But recommend to read it and send the content as str
                f = file.read()
                edit_campaigns(f)
                file.close()

        except FileNotFoundError as e:
            logging.info(e)

    ### Example json

    Download :download:`json <../../test/campaigns/sp-sx-edit-campaigns.json>` the file to use:

    .. literalinclude:: ../../test/campaigns/sp-sx-edit-campaigns.json

    .. autofunction:: ad_api.api.sp.Campaigns.list_campaigns

    ### Example getting a list of campaigns

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_list_campaigns(**kwargs):

            logging.info("---------------------------------")
            logging.info("Sponsored Products > list_campaigns(%s)" % str(kwargs))
            logging.info("---------------------------------")

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).list_campaigns(
                    **kwargs
                )

                campaigns = result.payload
                logging.info(len(campaigns))
                for campaign in campaigns:
                    logging.info(campaign)

            except AdvertisingApiException as error:
                logging.info(error)

        # if no filters provided will return all campaigns
        sp_list_campaigns()

        # Examples using filters
        # sp_list_campaigns(portfolioIdFilter="214026257044134")
        # sp_list_campaigns(stateFilter="enabled,paused")
        # sp_list_campaigns(stateFilter="enabled", count=10)
        # sp_list_campaigns(startIndex=10, stateFilter="enabled", count=10)
        # sp_list_campaigns(name="API.ES.Campaign.Manual.JSON.Edit.3")
        # sp_list_campaigns(campaignIdFilter="247123430252449,1280722862611,7164447325502")

    .. autofunction:: ad_api.api.sp.Campaigns.get_campaign

    ### Example getting a campaign

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_get_campaign(campaign_id: int):

            logging.info("---------------------------------")
            logging.info("Sponsored Products > get_campaign(%s)" % campaign_id)
            logging.info("---------------------------------")

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).get_campaign(
                    campaignId=campaign_id
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        sp_campaign_id = 247123430252449
        sp_get_campaign(sp_campaign_id)

    .. autofunction:: ad_api.api.sp.Campaigns.delete_campaign


    .. warning::

        Sets the campaign status to archived. Archived entities cannot be made active again. Consider editing the campaign and setting the status to "paused".

    ### Example deleting a campaign

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_delete_campaign(campaign_id: int):

            logging.info("---------------------------------")
            logging.info("Sponsored Products > delete_campaign(%s)" % campaign_id)
            logging.info("---------------------------------")

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).delete_campaign(
                    campaignId=campaign_id
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        sp_campaign_id = 217954743666143
        sp_delete_campaign(sp_campaign_id)


    .. autofunction:: ad_api.api.sp.Campaigns.list_campaigns_extended


    ### Example getting a list of campaigns with extended data

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_list_campaigns_extended(**kwargs):

            logging.info("---------------------------------")
            logging.info("Sponsored Products > sp_list_campaigns_extended(%s)" % str(kwargs))
            logging.info("---------------------------------")

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).list_campaigns_extended(
                    **kwargs
                )

                campaigns = result.payload
                logging.info(len(campaigns))
                for campaign in campaigns:
                    logging.info(campaign)

            except AdvertisingApiException as error:
                logging.info(error)

        # sp_list_campaigns_extended()
        sp_list_campaigns_extended(stateFilter="paused")


    .. autofunction:: ad_api.api.sp.Campaigns.get_campaign_extended

    ### Example getting a campaign with extended fields

    .. code-block:: python

        import logging
        from ad_api.api import sponsored_products
        from ad_api.base import AdvertisingApiException

        def sp_get_campaign_extended(campaign_id: int):

            logging.info("---------------------------------")
            logging.info("Sponsored Products > get_campaign_extended(%s)" % campaign_id)
            logging.info("---------------------------------")

            try:

                result = sponsored_products.Campaigns(account=store, marketplace=marketplace, debug=True).get_campaign_extended(
                    campaignId=campaign_id
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        sp_campaign_id = 247123430252449
        sp_get_campaign_extended(sp_campaign_id)


**********
References
**********

.. target-notes::

.. _`migration guide`: https://advertising.amazon.com/API/docs/en-us/sponsored-products/v3-migration-guide