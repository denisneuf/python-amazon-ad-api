Creative Assets
===============
`https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml`_

.. _https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml

Advertisers can use creative assets to store, organize and reuse brand content,
such as logos and images. Stored content can be used for Amazon Ads and on Amazon
shopping pages, so a brand can carry the same material across its campaigns.

.. autoclass:: ad_api.api.CreativeAssets
    :members:

    .. note::

        The contract is version 3.0 and carries no beta marker: no ``x-beta``,
        no ``x-amz-*`` and no deprecation notice. The page is listed as stable
        because of that.

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Version
         - Answer
       * - ``POST /assets/search``
         - ``search_assets``
         - v3
         - ``200``
       * - ``GET /assets``
         - ``get_asset``
         - v3
         - ``200``
       * - ``POST /assets/upload``
         - ``upload_asset``
         - v3
         - ``200``
       * - ``POST /assets/register``
         - ``register_asset``
         - v3
         - ``200``
       * - ``POST /assets/batchRegister``
         - ``batch_register_assets``
         - **v1**
         - ``200``
       * - ``GET /assets/batchRegister/{requestId}``
         - ``get_batch_register_status``
         - v3
         - ``200``

    ``batchRegister`` is the one route on v1 rather than v3. Its request and
    answer both carry ``vnd.assetsbatchregisterrequest.v1``, which is what the
    method sends.

    ### About the media types

    The contract names a media type on every route, and the service serves the
    current version when a call arrives without one. ``search_assets`` and
    ``get_asset`` send no ``Accept`` and answer ``200`` all the same. That is not
    the case everywhere in this package: the Insights routes answer ``415`` when
    the version is wrong, so the difference is worth knowing when a call
    surprises you.

    The two ``batchRegister`` methods do send their types, because their version
    does not follow the module's default.

    ### The upload, register, batch chain

    Assets arrive in three steps, and each one hands the next its input.

    .. list-table::
        :header-rows: 1

       * - Step
         - Call
         - Hands over
       * - 1
         - ``upload_asset({"fileName": "x.jpeg"})``
         - a signed S3 ``url``, valid for 15 minutes
       * - 2
         - ``PUT`` the file to that url
         - the stored file
       * - 3
         - ``register_asset({"url": ..., "name": ...})``
         - the registered ``assetId``

    ``batch_register_assets`` replaces step 3 when there are several files: it
    takes the list of urls and answers a ``requestId`` instead of the assets.

    ### search_assets body

    Every member is optional. An empty object returns the library.

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``text``
         - string
         - Free text to match against asset names.
       * - ``filterCriteria.valueFilters``
         - array
         - Each carries ``values`` and a ``valueField``, such as ``ASIN``.
       * - ``sortCriteria``
         - object
         - ``field`` and ``order``, such as ``CREATED_TIME`` and ``ASC``.
       * - ``size``
         - integer
         - Page size, default 25, between 1 and 500.
       * - ``token``
         - string
         - Token from a previous answer.

    The answer carries ``assetList``, ``token`` and ``totalRecords``.

    ### get_asset

    ``assetId`` is required. Without it the service answers ``400 Request input
    is required to get asset.``

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``assetId``
         - string
         - Required. The asset to read.
       * - ``version``
         - string
         - A version id such as ``version_v3``. Omit it and every version comes
           back.

    The answer carries ``assetGlobal`` and ``assetVersionList``.

    ### register_asset body

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``url``
         - string
         - Required. The signed location from ``upload_asset``. It expires in
           15 minutes.
       * - ``name``
         - string
         - Required. The name given to the asset.
       * - ``assetType``
         - string
         - ``IMAGE``.
       * - ``assetSubTypeList``
         - array
         - ``LOGO``, ``PRODUCT_IMAGE``, ``AUTHOR_IMAGE``, ``LIFESTYLE_IMAGE`` or
           ``OTHER_IMAGE``.
       * - ``asinList``
         - array
         - Tags the asset with ASINs so it can be found by product later.
       * - ``versionInfo``
         - object
         - ``linkedAssetId`` and ``versionNotes``, to register this file as a
           new version of an existing asset.
       * - ``associatedSubEntityList``
         - array
         - Each carries ``brandEntityId``. Required for sellers, not for
           vendors.
       * - ``registrationContext``
         - object
         - Associates the asset with a DSP advertiser.
       * - ``tags``
         - array
         - Tags for the asset.
       * - ``skipAssetSubTypesDetection``
         - boolean
         - Keep the subtype as given instead of letting the service reclassify
           it.

    ### batch_register_assets

    Asynchronous. It answers a ``requestId`` and nothing else, so the result is
    read with ``get_batch_register_status``.

    .. list-table::
        :header-rows: 1

       * - Field
         - Type
         - Meaning
       * - ``assetDetailsList``
         - array
         - Between 1 and 50 entries, each shaped like the ``register_asset``
           body above.
       * - ``batchRegistrationContext``
         - object
         - The context applied to the whole batch.

    ### Example searching the library

    .. code-block:: python

        from ad_api.api import CreativeAssets

        client = CreativeAssets(account='my_account', debug=False)

        res = client.search_assets(body={})
        payload = res.payload

        print(payload["totalRecords"])
        for asset in payload["assetList"]:
            print(asset["assetId"], asset.get("name"))

    ### Example reading one asset

    .. code-block:: python

        from ad_api.api import CreativeAssets

        client = CreativeAssets(account='my_account', debug=False)

        res = client.get_asset(
            assetId="amzn1.assetlibrary.asset1.c560c6b3fd3b38f93df58c01ffcc86bc")
        print(res.payload["assetGlobal"])
        print(res.payload["assetVersionList"])

    ### Example uploading and registering one file

    .. code-block:: python

        from ad_api.api import CreativeAssets
        from requests import put

        client = CreativeAssets(account='my_account', debug=False)

        # 1. ask where to put it
        res = client.upload_asset(body={"fileName": "Logo-1000x1000.jpeg"})
        url = res.payload["url"]

        # 2. put the bytes there, outside this package
        put(url, data=open("Logo-1000x1000.jpeg", "rb"))

        # 3. register it
        res = client.register_asset(body={
            "url": url,
            "name": "PRODUCT-IMAGE-NAME",
            "assetType": "IMAGE",
            "assetSubTypeList": ["PRODUCT_IMAGE"],
            "skipAssetSubTypesDetection": True,
        })
        print(res.payload)

    ### Example registering several files at once

    .. code-block:: python

        import time
        from ad_api.api import CreativeAssets

        client = CreativeAssets(account='my_account', debug=False)

        res = client.batch_register_assets(body={
            "assetDetailsList": [
                {
                    "url": "https://.../one.jpeg",
                    "name": "ONE",
                    "assetType": "IMAGE",
                    "assetSubTypeList": ["PRODUCT_IMAGE"],
                },
                {
                    "url": "https://.../two.jpeg",
                    "name": "TWO",
                    "assetType": "IMAGE",
                    "assetSubTypeList": ["PRODUCT_IMAGE"],
                },
            ]
        })
        request_id = res.payload["requestId"]

        # the batch runs in the background, so poll it
        while True:
            status = client.get_batch_register_status(request_id)
            print(status.payload)
            time.sleep(5)

    ### A note on an unknown requestId

    ``get_batch_register_status`` with an id the service does not know answers
    ``400``, not ``404``:

    .. code-block:: text

        AARServiceBadRequestException while executing registration workflow:
        No request exists for the requestId 00000000-0000-0000-0000-000000000000

    The route answered, so the message is about the id rather than the path.
