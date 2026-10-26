Stores
======

.. autoclass:: ad_api.api.sb.Stores
    :members:

    ### Request format

    ``create_asset`` takes ``multipart/form-data`` with two parts, not JSON:

    .. list-table::
        :header-rows: 1

       * - Part
         - Contents
       * - ``assetInfo``
         - A JSON string: ``{"brandEntityId": "...", "mediaType": "brandLogo"}``
       * - ``asset``
         - The image bytes. PNG, JPEG or GIF.

    Required headers:

    .. list-table::
        :header-rows: 1

       * - Header
         - Value
       * - ``Content-Type``
         - ``multipart/form-data`` with boundary, set by requests.
       * - ``Accept``
         - ``*/*``. A versioned media type answers ``406``.
       * - ``Content-Disposition``
         - ``attachment; filename="logo.png"``

    .. note::
        ``mediaType`` is a **string**, not an object. The contract's own example
        shows it as an object and that answers ``400 The assetInfo field is
        invalid``. ``brandEntityId`` is required for sellers even though the
        contract marks it optional, which applies to vendors only.

    Image constraints: smaller than 1MB, at least 400x400 pixels.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import Stores

        stores = Stores(account='account_name', debug=False)

        response = stores.create_asset(
            image='./logo.png',
            brandEntityId='ENTITY000000000000',
            mediaType='brandLogo',
        )
        print(response.payload)

    ### Notes

    ``list_stores`` and ``get_store`` were removed: both used ``/v2/stores``, which
    no longer exists. ``/v2/stores`` answers ``404 Method Not Found`` and
    ``/v2/stores/{id}`` answers ``404 Could not find resource``.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Stores
