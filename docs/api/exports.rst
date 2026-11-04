Exports
=======

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIExports_prod_3p.json
Documentation: not indexed by Amazon; the vendor page has not been found yet.

The export resource takes a request for a snapshot of one entity type and answers
an identifier. The file is built asynchronously, so the identifier is polled
afterwards until the export is ready.

Each request names its own media type, ``application/vnd.<entity>export.v1+json``,
and the client sends that version in both the ``Content-Type`` and the ``Accept``
header. The version argument defaults to 1.

.. autoclass:: ad_api.api.Exports
    :members:

    ### Endpoint map

    .. list-table::
        :header-rows: 1

       * - Path
         - Method
         - Media type
       * - ``/ads/export``
         - POST
         - ``application/vnd.adsexport.v1+json``
       * - ``/campaigns/export``
         - POST
         - ``application/vnd.campaignsexport.v1+json``
       * - ``/adGroups/export``
         - POST
         - ``application/vnd.adgroupsexport.v1+json``
       * - ``/targets/export``
         - POST
         - ``application/vnd.targetsexport.v1+json``
       * - ``/exports/{exportId}``
         - GET
         - -

    ### Example python

    .. code-block:: python

        import json
        from ad_api.api import Exports

        result = Exports(account=store).ads_export(
            body=json.dumps({
                "adProductFilter": {"include": ["SPONSORED_PRODUCTS"]}
            })
        )

        export_id = result.payload.get("exportId")

        status = Exports(account=store).get_export(
            exportId=export_id,
            typeExport="ads",
        )
