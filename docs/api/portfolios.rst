Portfolios
==========
`https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/portfolios/openapi.yaml`_

.. _https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/portfolios/openapi.yaml: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/portfolios/openapi.yaml

Portfolios consist of campaigns that are grouped together and linked to a distinct Advertiser Account. The term 'advertiser' refers to a brand, entity, account identifier, or claim identifier. Multiple portfolios are supported within an Advertiser Account.

.. autoclass:: ad_api.api.Portfolios

    .. note::

        This API **Portfolios** can be used as sandbox environment for testing

    .. autofunction:: ad_api.api.Portfolios.list_portfolios

    ### Example listing portfolios

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def list_portfolios(**kwargs):
            try:
                result = Portfolios(debug=True).list_portfolios(
                    **kwargs
                )

                if result.payload:
                    payload = result.payload
                    for portfolio in payload:
                        logging.info(portfolio)
                else:
                    logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            # list_portfolios()
            # list_portfolios(portfolioStateFilter="enabled")
            list_portfolios(portfolioIdFilter="84653842194444,183826157455614,92453628442009,31260007270996")
            # list_portfolios(portfolioNameFilter="Apple,Huawei,Sony")


    .. autofunction:: ad_api.api.Portfolios.list_portfolios_extended

    ### Example listing portfolios extended

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def list_portfolios_extended(**kwargs):
            try:
                result = Portfolios(debug=True).list_portfolios_extended(
                    **kwargs
                )

                if result.payload:
                    payload = result.payload
                    for portfolio in payload:
                        logging.info(portfolio)
                else:
                    logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            # list_portfolios_extended()
            # list_portfolios_extended(portfolioStateFilter="enabled")
            list_portfolios_extended(portfolioIdFilter="84653842194444,183826157455614,92453628442009,31260007270996")
            # list_portfolios_extended(portfolioNameFilter="Apple,Huawei,Sony")

    .. autofunction:: ad_api.api.Portfolios.get_portfolio

    ### Example getting a portfolio by portfolioId

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_portfolio(portfolio_id: int):
            try:
                result = Portfolios(debug=True).get_portfolio(
                    portfolioId=portfolio_id
                )
                payload = result.payload
                logging.info(payload)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            id_portfolio = 214026257044134
            get_portfolio(id_portfolio)

    .. autofunction:: ad_api.api.Portfolios.get_portfolio_extended

    ### Example getting a portfolio extended by portfolioId

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def get_portfolio_extended(portfolio_id: int):
            try:
                result = Portfolios(debug=True).get_portfolio_extended(
                    portfolioId=portfolio_id
                )
                payload = result.payload
                logging.info(payload)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            id_portfolio = 214026257044134
            get_portfolio_extended(id_portfolio)

    .. autofunction:: ad_api.api.Portfolios.create_portfolios

    ### Example creating a portfolio from a list or from a dict

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def create_portfolios(data: (list, str, dict)):
            try:
                result = Portfolios(debug=True).create_portfolios(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            request_portfolios = \
                [
                    {
                        "name": "Apple",
                        "budget": {
                            "amount": 100,
                            "currencyCode": "EUR",
                            "policy": "monthlyRecurring",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    },
                    {
                        "name": "Huawei",
                        "budget": {
                            "amount": 120,
                            "currencyCode": "EUR",
                            "policy": "dateRange",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    },
                    {
                        "name": "Sony",
                        "budget": {
                            "amount": 120,
                            "currencyCode": "EUR",
                            "policy": "dateRange",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    }
                ]

            create_single_dict_portfolio = \
                {
                    "name": "Pioneer",
                    "budget": {
                        "amount": 44.5,
                        "policy": "monthlyRecurring",
                        "startDate": "20220418"
                    },
                    "state": "enabled"
                }

            create_portfolios(request_portfolio)
            # create_portfolios(create_single_dict_portfolio)

    ### Example creating a portfolio from a static json file

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def create_portfolios(data: (list, str, dict)):
            try:
                result = Portfolios(debug=True).create_portfolios(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            filename = "../test/portfolios/create.json"
            create_portfolios(filename)


    # Static .json file in case want to use as example

    .. literalinclude:: ../../test/portfolios/create.json

    Download :download:`json <../../test/portfolios/create.json>` the file to use:

    .. autofunction:: ad_api.api.Portfolios.edit_portfolios

    ### Example editing a portfolio from a list or from a dict

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def edit_portfolios(data: (list, str, dict)):
            try:
                result = Portfolios(debug=True).edit_portfolios(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            update_portfolios = \
                [
                    {
                        "portfolioId": 183826157455614,
                        "name": "Apple-Macbook",
                        "budget": {
                            "amount": 77.5,
                            "currencyCode": "EUR",
                            "policy": "monthlyRecurring",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    },
                    {
                        "portfolioId": 84653842194444,
                        "name": "Huawei-Phone",
                        "budget": {
                            "amount": 25,
                            "currencyCode": "EUR",
                            "policy": "dateRange",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    },
                    {
                        "portfolioId": 92453628442009,
                        "name": "Sony-Headphones",
                        "budget": {
                            "amount": 55,
                            "currencyCode": "EUR",
                            "policy": "dateRange",
                            "startDate": "20220418"
                        },
                        "inBudget": False,
                        "state": "enabled"
                    }
                ]


            update_single_portfolio = \
                [
                    {
                        "portfolioId": 183826157455614,
                        "name": "Apple-iMac",
                        "budget": {
                            "amount": 30.5,
                            "policy": "monthlyRecurring",
                            "startDate": "20220418"
                        },
                        "inBudget": True,
                        "state": "enabled"
                    }
                ]

            update_single_dict_portfolio = \
                {
                    "portfolioId": 183826157455614,
                    "name": "Apple-All",
                    "budget": {
                        "amount": 80.5,
                        "policy": "monthlyRecurring",
                        "startDate": "20220418"
                    },
                    "inBudget": True,
                    "state": "enabled"
                }

            # edit_portfolios(update_portfolios)
            # edit_portfolios(update_single_portfolio)
            edit_portfolios(update_single_dict_portfolio)


    ### Example editing a portfolio from a static json file

    .. code-block:: python

        import logging
        from ad_api.api import Portfolios
        from ad_api.base import AdvertisingApiException


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s"
        )

        def edit_portfolios(data: (list, str, dict)):
            try:
                result = Portfolios(debug=True).edit_portfolios(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            filename = "../test/portfolios/edit.json"
            edit_portfolios(filename)

    # Static .json file in case want to use as example

    .. literalinclude:: ../../test/portfolios/edit.json

    Download :download:`json <../../test/portfolios/edit.json>` the file to use: