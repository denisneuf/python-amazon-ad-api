Ad Groups
=========

Amazon Ads API v1 - unified Ad Groups endpoints

The product is selected in the request body with ``adProductFilter``, not in the
URL. All four methods talk to ``/adsApi/v1/*/adGroups``.

Documentation: https://advertising.amazon.com/API/docs/en-us/api-spec-v1-adgroups
Specification: https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPIALLAdGroupsContract_prod_3p.json

The account header on query_ad_groups
--------------------------------------

The contract declares three parameters on this route: the client id, which is
required and which the client always sends; the profile scope, optional and
sent from the ``profile_id`` in the credentials; and ``Amazon-Ads-AccountId``,
optional. **There is no manager-account header on this route.**

``query_ad_groups`` accepts ``account_id`` as a keyword argument. It is turned
into the ``Amazon-Ads-AccountId`` header and removed from ``kwargs`` before the
query is built, so it never travels as a query parameter:

.. code-block:: python

    AdGroups(account='leadtech_es').query_ad_groups(
        body={...},
        account_id='amzn1.ads-account.g.3u0jlizk9go4xfk8pkgfc59e8',
    )

None of the three is required from the caller's side: without ``account_id``
the call goes out on the profile scope alone, which is what every other v1
family does.

.. autoclass:: ad_api.api.v1.AdGroups
    :members:
