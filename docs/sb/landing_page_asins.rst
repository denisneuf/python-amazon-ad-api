Landing Page Asins
==================

.. autoclass:: ad_api.api.sb.PageAsins

    .. autofunction:: ad_api.api.sb.PageAsins.get_page_asins(self, **kwargs) -> ApiResponse:

    ### Example python

    .. code-block:: python

        from ad_api.api.sb.landing_page_asins import PageAsins

        page_url = 'https://www.amazon.es/stores/page/49D4CB50-9C2F-46D5-8E50-5505529C790D'

        result = PageAsins().get_page_asins(
            pageUrl=page_url
        )

        logging.info(result)


    ### Payload

    .. code-block:: python

        {'asinList': ['B08N5WRTN2',
                      'B081G9YQ73',
                      'B008ATNJNS',
                      'B08N5VXMK6',
                      'B016UPAVDE',
                      'B08N5S5HH5',
                      'B016MUBL4U',
                      'B08N5WM84C',
                      'B08N5TLVQ2',
                      'B0863B2L69',
                      'B08N5TLB5J',
                      'B081GBLPTB',
                      'B081G4SK26',
                      'B08N5VT5SV',
                      'B0863G2M7F',
                      'B07BRLMY93',
                      'B08N5V4CKB',
                      'B086395QZM',
                      'B081GC15CY',
                      'B086395QZP'],
         'code': 'SUCCESS'}

NOT AVAILABLE SANDBOX [NOT_FOUND - Could not find resource for full path]