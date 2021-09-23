Brands
======

.. autoclass:: ad_api.api.sb.Brands

    .. autofunction:: ad_api.api.sb.Brands.list_brands(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.brands import Brands

        result = Brands().list_brands()

        logging.info(result)



    ### Payload

    .. code-block:: python

        [{'brandEntityId': 'ENTITY5ON7M22396H',
          'brandId': 'A387T2Q1UNXHJK',
          'brandRegistryName': 'Apple'},
         {'brandEntityId': 'ENTITY218756GCCQ6CF',
          'brandId': 'A36UAF6UNGFFAR',
          'brandRegistryName': 'Huawei'},
         {'brandEntityId': 'ENTITY1PRG7GD8FVXA3',
          'brandId': 'A87RK5OLHEBUU5',
          'brandRegistryName': 'Xiaomi'}]


NOT AVAILABLE SANDBOX [NOT_FOUND - Could not find resource for full path]