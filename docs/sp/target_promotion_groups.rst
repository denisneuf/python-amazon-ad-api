Target Promotion Groups
=======================

Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-products/3-0/openapi/prod

Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json

A target promotion group ties one auto-targeting ad group to the manual ad
groups that receive the targets promoted out of it: one keyword targeting ad
group and one product targeting ad group. The auto ad group discovers search
terms, the manual ad groups carry the promoted targets.

All five operations are ``POST`` and the body is not wrapped in a list, unlike
``/sp/campaigns/list``. The contract offers two content types, ``v1`` and
``v2``; ``version`` picks one and defaults to ``v1``.

.. autoclass:: ad_api.api.sp.TargetPromotionGroups
    :members:
