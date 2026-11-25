From Code
=========

You can override/set credentials from code by passing a ``dict`` to the client.

If you pass a value in credentials, other credentials from env variables or from a config file will be ignored.

Required fields, plus the optional identifiers the routes may need:

..  code-block:: python


    credentials = dict(
        refresh_token='your-refresh_token',
        client_id='your-client_id',
        client_secret='your-client_secret',
        profile_id='your-profile_id',
        account_id='your-advertiser_account_id',        # optional
        manager_account_id='your_manager_account_id',   # optional
    )

*****
Usage
*****

..  code-block:: python

    import logging
    from ad_api.base import AdvertisingApiException
    from ad_api.api import sponsored_products

    credentials = dict(
        refresh_token='your-refresh_token',
        client_id='your-client_id',
        client_secret='your-client_secret',
        profile_id='your-profile_id',
        # account_id='your-advertiser_account_id',
        # manager_account_id='your_manager_account_id',
    )

    try:

        status = 'enabled'

        result=sponsored_products.Campaigns(credentials=credentials, debug=True).list_campaigns(
            stateFilter=status
        )

        payload = result.payload

        logging.info(payload)

    except AdvertisingApiException as error:

        logging.info(error)






********************************
Choosing the account identifier
********************************

The dict above may also carry ``account_id`` and ``manager_account_id``; the
client turns whichever applies into its header. A route accepts one or more of
them, and when more than one is available the call picks it with ``selector=``:

.. code-block:: python

    credentials = dict(
        refresh_token='...',
        client_id='...',
        client_secret='...',
        profile_id='your-profile-id',
        account_id='your-advertiser-account-id',
    )

    api = Billing(credentials=credentials)

    api.invoice_summaries(body={}, selector="profile_id")   # one marketplace
    api.invoice_summaries(body={}, selector="account_id")   # every marketplace

With a single identifier the argument is unnecessary: the client sends that one.
The full table, the default and the two errors it can raise are in
:doc:`config`.
