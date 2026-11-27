Credential Headers (Beta)
=========================

Which routes need which credentials, as of 2.2.0. Every module below was
checked route by route; the count is how many of its routes carry the mark.

The OAuth trio is required by every route, wherever it comes from -- the
config file, a dict in code or the environment variables. None of the three
is a header of its own except the client id:

..  list-table::
    :header-rows: 1

    * - Credentials key
      - Where it goes
    * - ``client_id``
      - header ``Amazon-Advertising-API-ClientId``, on every request
    * - ``refresh_token``
      - body of the token exchange, with ``grant_type=refresh_token``
    * - ``client_secret``
      - body of the token exchange, never a header

What reaches the route as identity is the access token that exchange returns:
header ``Authorization: Bearer <token>``, on every request.

The three identifiers are optional and each route takes a fixed set of them:

..  list-table::
    :header-rows: 1

    * - Credentials key
      - Sent as
    * - ``profile_id``
      - ``Amazon-Advertising-API-Scope``
    * - ``account_id``
      - ``Amazon-Ads-AccountId``
    * - ``manager_account_id``
      - ``Amazon-Advertising-API-Manager-Account``

Routes that need no identifier
------------------------------

``refresh_token``, ``client_id`` and ``client_secret`` are enough. These routes
list the identifiers themselves, so they cannot require one, and they declare
``headers=[]``: the client sends none of the three. All four are done.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``account.py``
      - ``v0``
      - ``5/5``
      - ``done``
    * - ``advertising_test_account.py``
      - ``v0``
      - ``2/2``
      - ``done``
    * - ``manager_accounts.py``
      - ``v0``
      - ``4/4``
      - ``done``
    * - ``profiles.py``
      - ``v0``
      - ``4/4``
      - ``done``
Routes completed
----------------

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``account.py``
      - ``v0``
      - ``5/5``
      - ``completed``
    * - ``advertising_test_account.py``
      - ``v0``
      - ``2/2``
      - ``completed``
    * - ``attribution.py``
      - ``v0``
      - ``5/5``
      - ``completed``
    * - ``audiences.py``
      - ``v0``
      - ``2/2``
      - ``completed``
    * - ``audiences.py``
      - ``v0``
      - ``2/2``
      - ``completed``
    * - ``billing.py``
      - ``v0``
      - ``19/19``
      - ``completed``
    * - ``brand_metrics.py``
      - ``v0``
      - ``2/2``
      - ``completed``
    * - ``exports.py``
      - ``v0``
      - ``5/5``
      - ``completed``
    * - ``history.py``
      - ``v0``
      - ``1/1``
      - ``completed``
    * - ``insights.py``
      - ``v0``
      - ``1/1``
      - ``completed``
    * - ``manager_accounts.py``
      - ``v0``
      - ``4/4``
      - ``completed``
    * - ``metadata.py``
      - ``v0``
      - ``1/1``
      - ``completed``
    * - ``portfolios_v3.py``
      - ``v0``
      - ``4/4``
      - ``completed``
    * - ``profiles.py``
      - ``v0``
      - ``4/4``
      - ``completed``
    * - ``recommendations.py``
      - ``v0``
      - ``3/3``
      - ``completed``
    * - ``reports.py``
      - ``v0``
      - ``3/3``
      - ``completed``
    * - ``sp/campaigns_v3.py``
      - ``sp``
      - ``4/4``
      - ``completed``
    * - ``stores.py``
      - ``v0``
      - ``2/2``
      - ``completed``
    * - ``v1/campaigns.py``
      - ``v1``
      - ``4/4``
      - ``completed``
    * - ``validation_configurations.py``
      - ``v0``
      - ``2/2``
      - ``completed``
With ``Amazon-Ads-AccountId`` the v1 campaign routes answer only when the body
carries ``campaignIdFilter``; without it the service replies 400 "Multi marketplace
query requests only support query by primary resource id". ``Amazon-Advertising-API-Scope``
has no such restriction.

Routes pending
--------------

Sorted by family. State is partial when some routes are marked and pending
when none is; the last column groups what is left to do.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
      - Routes to mark
    * - dsp_advertiser.py
      - ``dsp``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sb/ad_creatives_v4.py
      - ``sb``
      - ``0/8``
      - ``pending``
      - ``8 unmarked``
    * - sb/ad_groups.py
      - ``sb``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sb/ad_groups_v4.py
      - ``sb``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sb/ads_v4.py
      - ``sb``
      - ``0/10``
      - ``pending``
      - ``10 unmarked``
    * - sb/benchmarks.py
      - ``sb``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - sb/bid_recommendations.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/brands.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/budget_rules.py
      - ``sb``
      - ``0/11``
      - ``pending``
      - ``11 unmarked``
    * - sb/campaigns.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/campaigns_v4.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/forecast.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/keywords.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/keywords_recommendations.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/landing_page_asins.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/media.py
      - ``sb``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - sb/migration.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/negative_keywords.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/negative_product_targeting.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/optimization_rules.py
      - ``sb``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - sb/product_targeting.py
      - ``sb``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sb/recommendations.py
      - ``sb``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sb/reports.py
      - ``sb``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sb/stores.py
      - ``sb``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sb/targeting_categories.py
      - ``sb``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sb/targeting_recommendations.py
      - ``sb``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - sb/themes.py
      - ``sb``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - sd/ad_groups.py
      - ``sd``
      - ``0/7``
      - ``pending``
      - ``7 unmarked``
    * - sd/bid_recommendations.py
      - ``sd``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sd/brand_safety.py
      - ``sd``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - sd/budget_rules.py
      - ``sd``
      - ``0/9``
      - ``pending``
      - ``9 unmarked``
    * - sd/campaigns.py
      - ``sd``
      - ``0/7``
      - ``pending``
      - ``7 unmarked``
    * - sd/campaigns_budget_usage.py
      - ``sd``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sd/creatives.py
      - ``sd``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - sd/forecast.py
      - ``sd``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sd/negative_product_targeting.py
      - ``sd``
      - ``0/7``
      - ``pending``
      - ``7 unmarked``
    * - sd/product_ads.py
      - ``sd``
      - ``0/7``
      - ``pending``
      - ``7 unmarked``
    * - sd/product_targeting.py
      - ``sd``
      - ``0/7``
      - ``pending``
      - ``7 unmarked``
    * - sd/recommendations.py
      - ``sd``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sd/reports.py
      - ``sd``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sd/snapshots.py
      - ``sd``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sd/targeting_recommendations.py
      - ``sd``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/ad_groups_v3.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/bid_recommendations_v3.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/budget_initial_recommendation.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/budget_recommendations.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/budget_rules.py
      - ``sp``
      - ``0/11``
      - ``pending``
      - ``11 unmarked``
    * - sp/budget_rules_recommendations.py
      - ``sp``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sp/campaign_consolidated_recommendations.py
      - ``sp``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sp/campaign_negative_keywords_v3.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/campaign_negative_targets.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/campaigns_budget_usage.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/campaings_optimization.py
      - ``sp``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - sp/global_recommendations.py
      - ``sp``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - sp/keyword_groups_recommendations.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/keywords_v3.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/negative_keywords_v3.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/negative_product_targeting_v3.py
      - ``sp``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - sp/product_ads_v3.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/product_recommendations.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/product_targeting_v3.py
      - ``sp``
      - ``0/8``
      - ``pending``
      - ``8 unmarked``
    * - sp/ranked_keywords_recommendations.py
      - ``sp``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - sp/schedule_based_bid_optimization.py
      - ``sp``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - sp/target_promotion_groups.py
      - ``sp``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - account_budgets.py
      - ``v0``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - advertising_invitations.py
      - ``v0``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - advertising_user_permissions.py
      - ``v0``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - brand_benchmarks.py
      - ``v0``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - creative_assets.py
      - ``v0``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - eligibility.py
      - ``v0``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - localization.py
      - ``v0``
      - ``0/5``
      - ``pending``
      - ``5 unmarked``
    * - marketing_mix_modeling.py
      - ``v0``
      - ``0/10``
      - ``pending``
      - ``10 unmarked``
    * - portfolios.py
      - ``v0``
      - ``0/6``
      - ``pending``
      - ``6 unmarked``
    * - stream.py
      - ``v0``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - v1/ad_associations.py
      - ``v1``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - v1/ad_extensions.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/ad_groups.py
      - ``v1``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - v1/ads.py
      - ``v1``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - v1/advertiser_accounts.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/brand_store_edition_publish_versions.py
      - ``v1``
      - ``0/2``
      - ``pending``
      - ``2 unmarked``
    * - v1/brand_store_editions.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/brand_store_pages.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/brand_stores.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/geo_locations.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/label_object_associations.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/labels.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/location_indexes.py
      - ``v1``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
    * - v1/manager_accounts.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/portfolios.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/recommendation_types.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/recommendations.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/reports.py
      - ``v1``
      - ``0/3``
      - ``pending``
      - ``3 unmarked``
    * - v1/selling_accounts.py
      - ``v1``
      - ``0/1``
      - ``pending``
      - ``1 unmarked``
    * - v1/targets.py
      - ``v1``
      - ``0/4``
      - ``pending``
      - ``4 unmarked``
