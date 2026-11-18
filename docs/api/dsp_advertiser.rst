DSP Advertiser Accounts
========================

.. list-table::
    :header-rows: 0
    :widths: 18 82

    * - **Vendor docs**
      - https://advertising.amazon.com/API/docs/en-us/dsp-advertiser
    * - **Specification**
      - https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/dsp/3-0/advertiser.yaml

Retrieve information of DSP advertisers. Contract version 3.0.

Two read-only routes. There is no write operation in this contract and no
versioned media type: both answer ``application/json``.

.. warning::

   Both routes require a **DSP profile**: ``accountInfo.type`` must be
   ``agency`` and ``subType`` must not be ``AMAZON_ATTRIBUTION``. A seller or
   vendor profile is not enough and the service answers 403.

   **These two routes have not been exercised against the API from this
   package.** The code is covered offline only: import, signatures and the
   prepared request. A seller profile cannot reach them.

.. list-table::
    :header-rows: 1
    :widths: 10 30 30 30

    * - Method
      - Endpoint
      - Parameters
      - Python
    * - GET
      - ``/dsp/advertisers``
      - ``startIndex``, ``count``, ``advertiserIdFilter``
      - :meth:`ad_api.api.DspAdvertiser.list_advertisers`
    * - GET
      - ``/dsp/advertisers/{advertiserId}``
      - ``advertiserId`` (path)
      - :meth:`ad_api.api.DspAdvertiser.get_advertiser`

.. autoclass:: ad_api.api.DspAdvertiser
    :members:
    :noindex:
