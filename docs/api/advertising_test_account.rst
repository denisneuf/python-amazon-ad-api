Advertising Test Account
========================

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AdvertisingTestAccount_prod_3p.json
Documentation: https://advertising.amazon.com/API/docs/en-us/test-accounts/openapi

Two routes, both on /testAccounts:

    POST /testAccounts    createAccount          body: accountMetaData
    GET  /testAccounts    GetAccountInformation  query: requestId

createAccount takes an account type and a marketplace, and answers a request id:

    accountType    AUTHOR or VENDOR
    countryCode    AE, AU, BE, BR, CA, DE, EG, ES, FR, IT, JP, MX, NL, PL,
                   SA, SE, SG, TR, UK, US

An account allows one test account per type and marketplace, so a second POST
for the same pair is refused rather than added.

The GET is keyed by that request id and answers the account once it exists:

    {"accountType": "VENDOR", "asins": [], "countryCode": "ES",
     "id": "ENTITY1MBW4T9T7Z5PC", "status": "COMPLETED"}

.. autoclass:: ad_api.api.AdvertisingTestAccount
    :members:

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
