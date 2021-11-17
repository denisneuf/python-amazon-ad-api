From Code
=========

You can override/set credentials from code by passing a ``dict`` to the client.

If you pass a value in credentials, other credentials from env variables or from a config file will be ignored.

Required fields:

..  code-block:: python


    credentials = dict(
        refresh_token='your-refresh_token',
        client_id='your-client_id',
        client_secret='your-client_secret',
        profile_id='your-profile_id',
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




