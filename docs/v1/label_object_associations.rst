Label Object Associations
=========================

Amazon Ads API v1 - label to object associations

Documentation: not indexed by Amazon; the vendor page has not been found yet.
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

.. warning::

    The route answers ``401 Unauthorized`` with ``Customer <account> is not
    authorized to access account`` on a Sponsored Ads seller profile, for both
    ``CAMPAIGN`` and ``AD_GROUP``. Its sibling ``Labels`` refuses the same way,
    so the whole label family is not enabled for such a profile even though
    ``campaign_view`` is declared as sufficient.

    The call is built from the contract and verified offline; it has not been
    exercised against the service from this account.

.. autoclass:: ad_api.api.v1.LabelObjectAssociations
    :members:
