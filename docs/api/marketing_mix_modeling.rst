Marketing Mix Modeling
=======================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/marketing-mix-modeling
    * - **Specification**
      - https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/MarketingMixModeling_prod_3p.json

.. toctree::
    :maxdepth: 1
    :titlesonly:

    marketing_mix_modeling/list_brand_groups
    marketing_mix_modeling/get_brand_group_campaigns
    marketing_mix_modeling/get_brand_group_products
    marketing_mix_modeling/create_brand_group_overrides
    marketing_mix_modeling/list_brand_group_overrides
    marketing_mix_modeling/delete_brand_group_overrides
    marketing_mix_modeling/create_report
    marketing_mix_modeling/list_reports
    marketing_mix_modeling/get_report
    marketing_mix_modeling/delete_report

The ten routes split into three groups that depend on each other:

    POST /mmm/v1/brandGroups/list                                -> pick a brandGroupId
    GET  /mmm/v1/brandGroups/{brandGroupId}/campaigns            -> what the group covers
    GET  /mmm/v1/brandGroups/{brandGroupId}/products             -> what the group covers
    POST /mmm/v1/brandGroupOverrides                             -> force an ASIN or campaign in or out
    POST /mmm/v1/brandGroupOverrides/list                        -> read them back
    POST /mmm/v1/brandGroupOverrides/delete                      -> remove them by id
    POST /mmm/v1/reports                                         -> request a report
    POST /mmm/v1/reports/list                                    -> list the reports so far
    GET  /mmm/v1/reports/{reportId}                              -> poll it, read the urls
    DELETE /mmm/v1/reports/{reportId}                            -> cancel or discard it

No brandGroupId can be guessed: the identifier comes from ``brandGroups/list``,
which answers one entry per brand group with ``brandGroupName``, ``countryCode``
and ``permittedMetricsTypes``. Every route below it takes that id.

Report lifecycle
----------------

``create_report`` answers a handle, not data. It carries ``reportId`` and
``status``; poll ``get_report`` until ``SUCCEEDED``. The status set is
``PENDING``, ``PROCESSING``, ``SUCCEEDED``, ``FAILED`` and ``CANCELED``, which is
not the wording of the v3 reporting family (that one says ``COMPLETED``): a caller
that shares a status check between both families reads the wrong value.

A finished report carries ``urls``, a **list**, and ``urlsExpireAt``. Each entry is
a signed url, so read the whole list and download before the expiry; a report split
in parts answers more than one.

The report body takes two date formats that the contract bounds differently:
``startDate`` and ``endDate`` are inclusive, and with ``timeUnit`` set to
``WEEKLY`` the start must be a Sunday or Monday and the end a Saturday or Sunday.
``dueDate`` only prioritises the job in the queue.

Configuration
-------------

``configuration`` requires four members and each one changes the output shape:

.. list-table::
    :header-rows: 1
    :widths: 20 22 58

    * - Field
      - Values
      - Effect
    * - ``brandGroupId``
      - string
      - The brand group being reported on.
    * - ``geoDimension``
      - COUNTRY, DMA, POSTAL_CODE
      - Geographic granularity. ``DMA`` is valid only in the US, ``POSTAL_CODE`` only in select countries.
    * - ``metricsType``
      - MEDIA_ONLY, MEDIA_AND_SALES
      - Core advertising metrics, or advertising plus retail metrics.
    * - ``timeUnit``
      - DAILY, WEEKLY
      - Time granularity, and it bounds the report dates when ``WEEKLY``.

Overrides
----------

An override forces a product or a campaign into or out of a brand group report by
its ``identifierType`` (``ASIN`` or ``CAMPAIGN_ID``) and ``identifier`` value. It
reads back with a ``status`` of ``APPROVED``, ``PENDING_REVIEW`` or
``NOT_APPROVED``, so a create that answers ``207`` with the override in ``success``
is queued, not applied.

Create and delete both answer ``207 MultiStatus`` with ``success`` and ``error``
lists: one call can accept some entries and refuse others, so check both.
``overrideIdFilter`` and ``brandGroupIdFilter`` take ``include`` arrays of at most
100 values, and delete takes the ids in the **body** because the route has no path
variant.

A create is refused with ``403`` when the brand group does not permit that
identifier type -- read ``permittedMetricsTypes`` on the brand group first.

.. autoclass:: ad_api.api.MarketingMixModeling
    :noindex:

    ### Example python

    .. code-block:: python

        from ad_api.api import MarketingMixModeling

        mmm = MarketingMixModeling()

        brand_groups = mmm.list_brand_groups(body={}).payload
        brand_group_id = brand_groups['brandGroups'][0]['brandGroupId']

        mmm.create_report(body={
            'configuration': {
                'brandGroupId': brand_group_id,
                'geoDimension': 'COUNTRY',
                'metricsType': 'MEDIA_ONLY',
                'timeUnit': 'DAILY',
            },
            'startDate': '2026-11-01',
            'endDate': '2026-11-10',
            'reportName': 'mmm-november',
        })

    ### Example json

    A report handle, from ``POST /mmm/v1/reports``::

        {
          'reportId': '7f2c...',
          'status': 'PENDING',
          'reportName': 'mmm-november',
          'startDate': '2026-11-01',
          'endDate': '2026-11-10',
          'createdAt': '2026-11-18T12:00:00Z',
          'dueDate': None,
          'urls': [],
          'urlsExpireAt': None,
        }
