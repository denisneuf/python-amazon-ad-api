Targets
=======

Amazon Ads API v1 - unified Targets endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/targets``.

``TargetCreate`` requires ``adProduct``, ``negative``, ``state``,
``targetDetails`` and ``targetType``. ``targetDetails`` carries exactly one of
29 variants keyed to ``targetType`` (``keywordTarget``, ``productTarget``,
``audienceTarget``, ``deviceTarget``, ``dayPartTarget``, ...).

``TargetUpdate`` accepts only ``targetId`` plus mutable fields — to change what
a target points at, delete it and create a new one.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-targets
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLTargetsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.Targets

    .. autofunction:: ad_api.api.v1.Targets.query_targets

    .. autofunction:: ad_api.api.v1.Targets.create_targets

    .. autofunction:: ad_api.api.v1.Targets.update_targets

    .. autofunction:: ad_api.api.v1.Targets.delete_targets
