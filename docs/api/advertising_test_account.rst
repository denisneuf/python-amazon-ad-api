Advertising Test Account
========================

.. autoclass:: ad_api.api.AdvertisingTestAccount

    .. autofunction:: ad_api.api.AdvertisingTestAccount.create_test_account

    ### Example python

    .. code-block:: python

        import json
        from ad_api.api import AdvertisingTestAccount

        data = \
        {
            "countryCode": "ES",
            "accountMetaData":
                {
                    "vendorCode": "ABCDE"
                },
            "accountType": "VENDOR"
        }

        result = AdvertisingTestAccount(account=store, marketplace=marketplace, debug=True).create_test_account(
            body=json.dumps(data)
        )

    .. code-block:: python

        {
        'requestId': 'A7BCDGCEVXQ1CJJ4301V'
        }

    .. autofunction:: ad_api.api.AdvertisingTestAccount.get_test_account

    ### Example python

    .. code-block:: python

        from ad_api.api import AdvertisingTestAccount

        request_id = "A7BCDGCEVXQ1CJJ4301V"

        result = AdvertisingTestAccount(account=store, marketplace=marketplace, debug=True).get_test_account(
            requestId=request_id
        )


    .. code-block:: python

        {
        "accountType": "VENDOR",
        "asins": [],
        "countryCode": "ES",
        "id": "ENTITY1MBW4T9T7Z5PC",
        "status": "COMPLETED"
        }