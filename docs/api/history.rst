Change History open beta
========================
`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/Eligibility_prod_3p.json

Provides information about changes made to campaigns, adgroups, ads, etc

.. autoclass:: ad_api.api.History

    .. autofunction:: ad_api.api.History.get_history

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import History
        from ad_api.base import AdvertisingApiException

        def get_history(data: (str, dict)):

            try:

                result = History(debug=True).get_history(
                    body=json.dumps(data)
                )
                payload = result.payload
                events = payload.get("events")
                for event in events:
                    logging.info(event)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':


            # fromDate cannot be more than 90 days ago
            from_date = datetime(2022, 2, 1, 0, 0, 0).strftime('%s%f')[:-3]
            to_date = datetime.now().strftime('%s%f')[:-3]

            request = \
                {
                    "fromDate": int(from_date),
                    "toDate": int(to_date),
                    "eventTypes": {
                        "CAMPAIGN": {
                            "filters": [
                                "BUDGET_AMOUNT",
                                "STATUS"
                            ],
                            "eventTypeIds": [
                                "45662011530311"
                            ]
                        }
                    }
                }

            get_history(request)

    ### Example query.json

    Download :download:`json <../../test/history/query.json>` the file to use:

    .. literalinclude:: ../../test/history/query.json