Ad Extensions
=============

Amazon Ads API v1 - unified AdExtensions endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. The three methods talk to ``/adsApi/v1/*/adExtensions``.

An ad extension adds delivery detail to an existing Sponsored Products ad rather
than creating a new one. The contract declares exactly two types:

- ``PROMPTS`` -- a prompt-style text extension.
- ``VIDEO`` -- a video extension.

There is no delete route. ``AdExtensionUpdate`` accepts only ``adExtensionId``
plus ``state``, so ending an extension means pausing or archiving it. Changing
its content means creating a new one and archiving the old.

``adProduct`` is a single-value enum here (``SPONSORED_PRODUCTS``), and every
filter is shaped ``{"include": [...]}`` with ``include`` required inside.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adextensions
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdExtensionsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.AdExtensions
    :members:

