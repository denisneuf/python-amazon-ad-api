Manager Account
===============

`https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json`_

.. _https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json: https://dtrnk0o2zy01c.cloudfront.net/openapi/en-us/dest/ManagerAccount_prod_3p.json

A Manager Account lets you manage a group of Amazon Advertising accounts.

.. autoclass:: ad_api.api.ManagerAccounts

    .. autofunction:: ad_api.api.ManagerAccounts.list_manager_accounts

    ### Example getting a list of manager accounts

    .. code-block:: python

        import logging
        from ad_api.api import ManagerAccounts
        from ad_api.base import AdvertisingApiException

        def list_manager_accounts():

            try:
                result = ManagerAccounts(account="bestq", debug=True).list_manager_accounts()
                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            list_manager_accounts()

    .. autofunction:: ad_api.api.ManagerAccounts.create_manager_account

    ### Example creating a manager account

    .. code-block:: python

        import logging
        from ad_api.api import ManagerAccounts
        from ad_api.base import AdvertisingApiException


        def create_manager_account(data: dict or str):
            try:
                result = ManagerAccounts(debug=True).create_manager_account(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            manager_account_name = 'ManagerMyAccount'
            manager_account_type = 'Agency'  # Agency Advertiser

            account = \
                {
                    'managerAccountName': manager_account_name,
                    'managerAccountType': manager_account_type,
                }

            create_manager_account(account)

    .. autofunction:: ad_api.api.ManagerAccounts.associate_manager_accounts

    ### Example associating a manager account with and advertiser account

    .. code-block:: python

        import logging
        from ad_api.api import ManagerAccounts
        from ad_api.base import AdvertisingApiException

        def associate_manager_accounts(manager_account_id: str, data: dict or str):
            try:
                result = ManagerAccounts(debug=True).associate_manager_accounts(
                    managerAccountId=manager_account_id,
                    body=data,
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            amz_manager_account_id = 'amzn1.ads1.ma1.ewpohpn123456789987654321'
            account_id = 'ENTITY1123456789012'
            roles = ['ENTITY_VIEWER']
            type_account = 'ACCOUNT_ID'

            association = \
                {
                    'accounts':
                        [
                            {
                                'roles': roles,
                                'id': account_id,
                                'type': type_account
                            }
                        ]
                }

            associate_manager_accounts(amz_manager_account_id, association)

    .. autofunction:: ad_api.api.ManagerAccounts.disassociate_manager_accounts

    ### Example unlinking a manager account with and advertiser account

    .. code-block:: python

        import logging
        from ad_api.api import ManagerAccounts
        from ad_api.base import AdvertisingApiException

        def disassociate_manager_accounts(manager_account_id: str, data: dict or str):
            try:
                result = ManagerAccounts(debug=True).disassociate_manager_accounts(
                    managerAccountId=manager_account_id,
                    body=data,
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            amz_manager_account_id = 'amzn1.ads1.ma1.ewpohpn123456789987654321'
            account_id = 'ENTITY1123456789012'
            type_account = 'ACCOUNT_ID'

            disassociation = \
                {
                    'accounts':
                        [
                            {
                                'id': account_id,
                                'type': type_account
                            }
                        ]
                }

            disassociate_manager_accounts(amz_manager_account_id, disassociation)