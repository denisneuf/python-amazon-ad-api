Credential Headers (Beta)
=========================

Which routes need which credentials, as of 2.1.15. Every module below was
checked route by route; the count is how many of its routes carry the mark.
The rule and the ``selector=`` argument are on :doc:`config`.

The OAuth trio is required by every route, wherever it comes from -- the
config file, a dict in code or the environment variables:

..  list-table::
    :header-rows: 1

    * - Credentials key
      - Sent as
    * - ``refresh_token``
      - the bearer token
    * - ``client_id``
      - ``Amazon-Advertising-API-ClientId``
    * - ``client_secret``
      - used to obtain the token

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
-------------------------------

``refresh_token``, ``client_id`` and ``client_secret`` are enough. The three
identifiers may be set and are not sent: these routes list the identifiers
themselves, so they cannot require one.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``account.py``
      - v0
      - 5/5
      - done
    * - ``advertising_test_account.py``
      - v0
      - 2/2
      - done
    * - ``manager_accounts.py``
      - v0
      - 4/4
      - done
    * - ``profiles.py``
      - v0
      - 4/4
      - done

Routes that need ``profile_id``
--------------------------------

One marketplace per answer. The client sends ``Amazon-Advertising-API-Scope``
and drops the other two headers, even when the credentials carry them.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``history.py``
      - v0
      - 1/1
      - done
    * - ``stores.py``
      - v0
      - 2/2
      - done
    * - ``v1/campaigns.py``
      - v1
      - 1/4
      - query only
    * - ``sp/campaigns_v3.py``
      - v3
      - 4/4
      - list only
    * - ``billing.py``
      - v0
      - 2/19
      - ``list_invoices`` and ``get_invoice``

Routes that need ``account_id`` or ``manager_account_id``
---------------------------------------------------------

These routes accept neither a marketplace scope nor a second account.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``billing.py``
      - v0
      - 4/19
      - ``get_billing_document``, ``apply_billing_profile``, ``create_billing_profiles``, ``update_billing_profiles``

Routes that accept any of the three
-----------------------------------

The call picks with ``selector=``. With more than one identifier in the
credentials and no selector, the client raises ``AmbiguousEndpointHeader``
instead of guessing.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``billing.py``
      - v0
      - 13/19
      - ``selector=`` on each call

Routes pending
--------------

Every module that still has routes without a mark. ``partial`` means some
routes are marked and the rest are not; ``pending`` means none is.

..  list-table::
    :header-rows: 1

    * - Module
      - Family
      - Routes marked
      - State
    * - ``account.py``
      - v0
      - 0/5
      - pending
    * - ``account_budgets.py``
      - v0
      - 0/2
      - pending
    * - ``advertising_invitations.py``
      - v0
      - 0/5
      - pending
    * - ``advertising_test_account.py``
      - v0
      - 0/2
      - pending
    * - ``advertising_user_permissions.py``
      - v0
      - 0/5
      - pending
    * - ``attribution.py``
      - v0
      - 0/5
      - pending
    * - ``audiences.py``
      - v0
      - 0/2
      - pending
    * - ``brand_benchmarks.py``
      - v0
      - 0/2
      - pending
    * - ``brand_metrics.py``
      - v0
      - 0/2
      - pending
    * - ``creative_assets.py``
      - v0
      - 0/6
      - pending
    * - ``dsp_advertiser.py``
      - dsp
      - 0/2
      - pending
    * - ``eligibility.py``
      - v0
      - 0/3
      - pending
    * - ``exports.py``
      - v0
      - 0/5
      - pending
    * - ``insights.py``
      - v0
      - 0/1
      - pending
    * - ``localization.py``
      - v0
      - 0/5
      - pending
    * - ``manager_accounts.py``
      - v0
      - 0/4
      - pending
    * - ``marketing_mix_modeling.py``
      - v0
      - 0/10
      - pending
    * - ``metadata.py``
      - v0
      - 0/1
      - pending
    * - ``portfolios.py``
      - v0
      - 0/6
      - pending
    * - ``portfolios_v3.py``
      - v0
      - 0/4
      - pending
    * - ``profiles.py``
      - v0
      - 0/8
      - pending
    * - ``recommendations.py``
      - v0
      - 0/3
      - pending
    * - ``reports.py``
      - v0
      - 0/3
      - pending
    * - ``sb/ad_creatives_v4.py``
      - sb
      - 0/8
      - pending
    * - ``sb/ad_groups.py``
      - sb
      - 0/2
      - pending
    * - ``sb/ad_groups_v4.py``
      - sb
      - 0/4
      - pending
    * - ``sb/ads_v4.py``
      - sb
      - 0/10
      - pending
    * - ``sb/benchmarks.py``
      - sb
      - 0/3
      - pending
    * - ``sb/bid_recommendations.py``
      - sb
      - 0/1
      - pending
    * - ``sb/brands.py``
      - sb
      - 0/1
      - pending
    * - ``sb/budget_rules.py``
      - sb
      - 0/11
      - pending
    * - ``sb/campaigns.py``
      - sb
      - 0/5
      - pending
    * - ``sb/campaigns_v4.py``
      - sb
      - 0/5
      - pending
    * - ``sb/forecast.py``
      - sb
      - 0/1
      - pending
    * - ``sb/keywords.py``
      - sb
      - 0/5
      - pending
    * - ``sb/keywords_recommendations.py``
      - sb
      - 0/1
      - pending
    * - ``sb/landing_page_asins.py``
      - sb
      - 0/1
      - pending
    * - ``sb/media.py``
      - sb
      - 0/3
      - pending
    * - ``sb/migration.py``
      - sb
      - 0/5
      - pending
    * - ``sb/negative_keywords.py``
      - sb
      - 0/5
      - pending
    * - ``sb/negative_product_targeting.py``
      - sb
      - 0/5
      - pending
    * - ``sb/optimization_rules.py``
      - sb
      - 0/6
      - pending
    * - ``sb/product_targeting.py``
      - sb
      - 0/5
      - pending
    * - ``sb/recommendations.py``
      - sb
      - 0/1
      - pending
    * - ``sb/reports.py``
      - sb
      - 0/2
      - pending
    * - ``sb/stores.py``
      - sb
      - 0/2
      - pending
    * - ``sb/targeting_categories.py``
      - sb
      - 0/4
      - pending
    * - ``sb/targeting_recommendations.py``
      - sb
      - 0/3
      - pending
    * - ``sb/themes.py``
      - sb
      - 0/3
      - pending
    * - ``sd/ad_groups.py``
      - sd
      - 0/7
      - pending
    * - ``sd/bid_recommendations.py``
      - sd
      - 0/1
      - pending
    * - ``sd/brand_safety.py``
      - sd
      - 0/6
      - pending
    * - ``sd/budget_rules.py``
      - sd
      - 0/9
      - pending
    * - ``sd/campaigns.py``
      - sd
      - 0/7
      - pending
    * - ``sd/campaigns_budget_usage.py``
      - sd
      - 0/1
      - pending
    * - ``sd/creatives.py``
      - sd
      - 0/5
      - pending
    * - ``sd/forecast.py``
      - sd
      - 0/1
      - pending
    * - ``sd/negative_product_targeting.py``
      - sd
      - 0/7
      - pending
    * - ``sd/product_ads.py``
      - sd
      - 0/7
      - pending
    * - ``sd/product_targeting.py``
      - sd
      - 0/7
      - pending
    * - ``sd/recommendations.py``
      - sd
      - 0/1
      - pending
    * - ``sd/reports.py``
      - sd
      - 0/2
      - pending
    * - ``sd/snapshots.py``
      - sd
      - 0/2
      - pending
    * - ``sd/targeting_recommendations.py``
      - sd
      - 0/1
      - pending
    * - ``sp/ad_groups_v3.py``
      - sp
      - 0/4
      - pending
    * - ``sp/bid_recommendations_v3.py``
      - sp
      - 0/1
      - pending
    * - ``sp/budget_initial_recommendation.py``
      - sp
      - 0/1
      - pending
    * - ``sp/budget_recommendations.py``
      - sp
      - 0/1
      - pending
    * - ``sp/budget_rules.py``
      - sp
      - 0/11
      - pending
    * - ``sp/budget_rules_recommendations.py``
      - sp
      - 0/2
      - pending
    * - ``sp/campaign_consolidated_recommendations.py``
      - sp
      - 0/2
      - pending
    * - ``sp/campaign_negative_keywords_v3.py``
      - sp
      - 0/4
      - pending
    * - ``sp/campaign_negative_targets.py``
      - sp
      - 0/4
      - pending
    * - ``sp/campaigns_budget_usage.py``
      - sp
      - 0/1
      - pending
    * - ``sp/campaigns_v3.py``
      - sp
      - 1/4
      - partial
    * - ``sp/campaings_optimization.py``
      - sp
      - 0/6
      - pending
    * - ``sp/global_recommendations.py``
      - sp
      - 0/2
      - pending
    * - ``sp/keyword_groups_recommendations.py``
      - sp
      - 0/1
      - pending
    * - ``sp/keywords_v3.py``
      - sp
      - 0/4
      - pending
    * - ``sp/negative_keywords_v3.py``
      - sp
      - 0/4
      - pending
    * - ``sp/negative_product_targeting_v3.py``
      - sp
      - 0/6
      - pending
    * - ``sp/product_ads_v3.py``
      - sp
      - 0/4
      - pending
    * - ``sp/product_recommendations.py``
      - sp
      - 0/1
      - pending
    * - ``sp/product_targeting_v3.py``
      - sp
      - 0/8
      - pending
    * - ``sp/ranked_keywords_recommendations.py``
      - sp
      - 0/1
      - pending
    * - ``sp/schedule_based_bid_optimization.py``
      - sp
      - 0/4
      - pending
    * - ``sp/target_promotion_groups.py``
      - sp
      - 0/5
      - pending
    * - ``stream.py``
      - v0
      - 0/4
      - pending
    * - ``v1/ad_associations.py``
      - v1
      - 0/4
      - pending
    * - ``v1/ad_extensions.py``
      - v1
      - 0/3
      - pending
    * - ``v1/ad_groups.py``
      - v1
      - 0/4
      - pending
    * - ``v1/ads.py``
      - v1
      - 0/4
      - pending
    * - ``v1/advertiser_accounts.py``
      - v1
      - 0/3
      - pending
    * - ``v1/brand_store_edition_publish_versions.py``
      - v1
      - 0/2
      - pending
    * - ``v1/brand_store_editions.py``
      - v1
      - 0/1
      - pending
    * - ``v1/brand_store_pages.py``
      - v1
      - 0/1
      - pending
    * - ``v1/brand_stores.py``
      - v1
      - 0/1
      - pending
    * - ``v1/geo_locations.py``
      - v1
      - 0/1
      - pending
    * - ``v1/label_object_associations.py``
      - v1
      - 0/1
      - pending
    * - ``v1/labels.py``
      - v1
      - 0/1
      - pending
    * - ``v1/location_indexes.py``
      - v1
      - 0/4
      - pending
    * - ``v1/manager_accounts.py``
      - v1
      - 0/3
      - pending
    * - ``v1/portfolios.py``
      - v1
      - 0/3
      - pending
    * - ``v1/recommendation_types.py``
      - v1
      - 0/1
      - pending
    * - ``v1/recommendations.py``
      - v1
      - 0/3
      - pending
    * - ``v1/reports.py``
      - v1
      - 0/3
      - pending
    * - ``v1/selling_accounts.py``
      - v1
      - 0/1
      - pending
    * - ``v1/targets.py``
      - v1
      - 0/4
      - pending
    * - ``validation_configurations.py``
      - v0
      - 0/2
      - pending
