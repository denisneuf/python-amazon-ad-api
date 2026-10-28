Ad Associations
================

Amazon Ads API v1 - unified AdAssociations endpoints

An ad association links one ``adId`` to one ``adGroupId`` and decides how much of
the group's traffic that ad receives. ``weight`` is the relative percentage
directed to the creative, and ``startDateTime`` / ``endDateTime`` bound when the
association applies.

All four methods talk to ``/adsApi/v1/*/adAssociations``. This is the first v1
family in this client with the full set: the others stop at update.

Update cannot move an association to another ad or ad group — only the dates,
the state and the weight are accepted, so reassigning means delete and create.

The delete route names its array ``adAssociationIds``, not ``adAssociations`` as
create and update do. Sending the wrong name is a rejected request.

This is not an ad-product resource, so there is no ``adProductFilter```: the query
filters by association, ad group or ad.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adassociations
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdAssociationsContract_prod_3p.json

.. autoclass:: ad_api.api.v1.AdAssociations
    :members:

