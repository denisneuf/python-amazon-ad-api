Targeting Categories
====================

Sponsored Brands targetable categories: the category tree, the refinements of a
category, and the number of products inside one.

All four routes are reads, and all four were probed against a live account. This is
the only family in the package with no unverified route.

.. autoclass:: ad_api.api.sb.TargetingCategories

    .. autofunction:: ad_api.api.sb.TargetingCategories.list_categories(self, supplySource, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.TargetingCategories.list_refinements(self, categoryRefinementId, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.TargetingCategories.get_product_count(self, category, **kwargs) -> ApiResponse:

    .. autofunction:: ad_api.api.sb.TargetingCategories.list_negative_brand_recommendations(self, **kwargs) -> ApiResponse:

    ### Endpoint map

    ==========================================================  ==========================  ======================  ======
    Path                                                        Method                      Media type              Status
    ==========================================================  ==========================  ======================  ======
    ``GET  /sb/targets/categories``                             ``list_categories``         ``vnd.sbtargeting.v4``  ``200``
    ``GET  /sb/targets/categories/{id}/refinements``            ``list_refinements``        ``vnd.sbtargeting.v4``  ``200``
    ``POST /sb/targets/products/count``                         ``get_product_count``       ``vnd.sbtargeting.v4``  ``200``
    ``GET  /sb/negativeTargets/brands/recommendations``         ``list_negative_brand_recommendations``  ``vnd.sbtargeting.v4``  ``200``
    ==========================================================  ==========================  ======================  ======

    Every route sends and receives ``application/vnd.sbtargeting.v4+json``.

    ### The category tree

    ``list_categories`` answers with the tree under **``categoryTree``**, a key the
    contract does not name. Each node looks like this:

    .. code-block:: json

        {
            "categoryRefinementId": "1909624031",
            "name": "Chupetes",
            "asinCountRange": {"min": 1247, "max": 2078},
            "isTargetable": true,
            "parentCategoryRefinementId": "1862267031"
        }

    ``asinCountRange`` gives the population of a category before committing to it,
    which is the useful part when building targeting.

    The nodes form a flat list linked by ``parentCategoryRefinementId``, so a tree
    is rebuilt by walking that reference.

    .. note::
        Large root categories come back with ``isTargetable`` set to ``false``:
        they have to be narrowed to their children before they can be used as a
        target. Use ``parentCategoryRefinementId`` to walk down.

    ### list_categories parameters

    ===========================  ========  ==================================================
    Parameter                    Required  Description
    ===========================  ========  ==================================================
    ``supplySource``             yes       ``AMAZON`` or ``STREAMING_VIDEO``.
    ``locale``                   no        ``es_ES``, ``en_US``, ``de_DE`` and 23 more.
    ``includeOnlyRootCategories`` no       Return root categories only.
    ``parentCategoryRefinementId`` no       Return the children of that category.
    ``nextToken``                no        Pagination token.
    ===========================  ========  ==================================================

    ### get_product_count body

    ``category`` is required; everything else narrows the count:

    .. code-block:: json

        {
            "category": "1909624031",
            "brands": ["YEYIAN"],
            "ageRanges": ["ADULT"],
            "genres": ["ACTION"],
            "isPrimeShipping": true,
            "ratingRange": {"min": 3, "max": 5},
            "priceRange": {"min": 10.0, "max": 150.0}
        }

    The optional members can be passed as keyword arguments:

    .. code-block:: python

        tc.get_product_count(category="1909624031",
                             priceRange={"min": 10.0, "max": 150.0})

    An empty body answers ``400`` naming ``category`` as the missing member.

    ### Example python

    .. code-block:: python

        from ad_api.api.sb import TargetingCategories

        tc = TargetingCategories(account='account_name', debug=False)

        # the whole tree
        tree = tc.list_categories(supplySource='AMAZON').payload

        # only roots
        roots = tc.list_categories(supplySource='AMAZON',
                                   includeOnlyRootCategories=True).payload

        # the children of one category
        children = tc.list_categories(supplySource='AMAZON',
                                      parentCategoryRefinementId='1703495031').payload

        # how many products sit in one category
        print(tc.get_product_count(category='1909624031').payload)

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi
