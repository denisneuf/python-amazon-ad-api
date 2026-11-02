Label Object Associations
=========================

Amazon Ads API v1 - label to object associations

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-label-object-associations
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLabelObjectAssociationsContract_prod_3p.json

One route, read only:

    POST /adsApi/v1/query/labelObjectAssociations

``Labels`` lists the labels that exist; this family lists what each one is
applied to, so the pair answers "which labels do I have" and "what is tagged".

The required member is ``labelObjectTypeFilter``, not the ``adProductFilter``
the campaign families carry, and it takes exactly one value:

    AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP

``adProductFilter``, ``labelIdFilter`` and ``labelObjectIdFilter`` are all
optional, and the two id filters take 1 to 50 values each.

``maxResults`` reaches 5000 here, far above the 100 of the campaign families,
because associations grow with the number of tagged objects.

.. warning::

    ``DEAL`` and ``INVENTORY_GROUP`` are deal-domain object types, where a
    Sponsored Ads seller profile answers 401, the same way it does on the DSP
    families.

.. autoclass:: ad_api.api.v1.LabelObjectAssociations
    :members:
