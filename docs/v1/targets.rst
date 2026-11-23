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

.. rubric:: Account header

``query_targets`` accepts ``account_id`` as a keyword argument, and so do the other
three methods of this family. It is turned into the ``Amazon-Ads-AccountId``
header and removed from ``kwargs`` before the call is built, so it never
travels in the query string:

.. code-block:: python

    Targets(account='my_store', marketplace=Marketplaces.EU).query_targets(
        body={...},
        account_id='amzn1.ads-account.g.xxxxxxxxxxxxxxxxxxxxxxxx',
    )

The contract declares the header as optional on all four routes, alongside the
client id, which is required and always sent, and the profile scope, which
comes from the ``profile_id`` in the credentials. Without ``account_id`` the
call goes out on the profile scope alone.

.. rubric:: Endpoint map

.. list-table::
    :header-rows: 1

    * - Path
      - Operation
      - Body requires
    * - ``/adsApi/v1/create/targets``
      - CreateTarget
      - targets
    * - ``/adsApi/v1/delete/targets``
      - DeleteTarget
      - targetIds
    * - ``/adsApi/v1/query/targets``
      - QueryTarget
      - adProductFilter
    * - ``/adsApi/v1/update/targets``
      - UpdateTarget
      - targets

.. currentmodule:: ad_api.api.v1

.. autosummary::
    :toctree: targets/
    :nosignatures:

    Targets
    Targets.create_targets
    Targets.delete_targets
    Targets.query_targets
    Targets.update_targets
