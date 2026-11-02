Labels
======

Amazon Ads API v1 - unified Labels endpoints

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-labels
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLLabelsContract_prod_3p.json

Labels has a single route and it is read only: the contract declares no
create, update or delete.

    POST /adsApi/v1/query/labels

The required member is not the ``adProductFilter`` the other v1 families
carry, but ``labelObjectTypeFilter``, and it takes exactly one value:

    AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP

A body without it is a rejected request rather than an empty answer, so every
call needs that member even when the other filters are left out.

The remaining filters are all optional, and each takes its own list:

    adProductFilter      exactly one AdProduct
    labelIdFilter        1 to 50 ids
    labelNameFilter      1 to 10 names
    maxResults           1 to 1000, default 100

.. warning::

    ``DEAL`` and ``INVENTORY_GROUP`` are deal-domain object types. A Sponsored
    Ads seller profile answers ``401`` on the deal domain, the same way it does
    on the DSP families, so only ``CAMPAIGN`` and ``AD_GROUP`` can be exercised
    here.

.. autoclass:: ad_api.api.v1.Labels
    :members:
