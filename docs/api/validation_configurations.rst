Validation Configuration
========================

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/ValidationConfigurationsAPI_prod_3p.json

.. autoclass:: ad_api.api.ValidationConfigurations
    :members:

    ### Example python

    .. code-block:: python

        from ad_api.api import ValidationConfigurations

        dictionary = \
        {
            "countryCodesList": [
                "ES"
            ],
            "entityTypesList": [
                "SELLER"
            ],
            "programTypesList": [
                "SB"
            ]
        }

        result = ValidationConfigurations().retrieve_validation_campaigns(
            body=dictionary
        )
        payload = result.payload

    ### Example python

    .. code-block:: python

        from ad_api.api import ValidationConfigurations

        dictionary = \
        {
            "countryCodesList": [
                "ES"
            ],
            "entityTypesList": [
                "VENDOR"
            ],
            "programTypesList": [
                "SP"
            ]
        }

        result = ValidationConfigurations().retrieve_validation_targeting_clauses(
            body=dictionary
        )
        payload = result.payload
