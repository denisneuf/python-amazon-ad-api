from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class TargetingCategories(Client):
    """Sponsored Brands targetable categories.

    Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/4-0/openapi

    All three routes are reads, and all three were probed against a live account.

    .. note::
        ``list_categories`` returns the tree under ``categoryTree``, which the
        contract does not name. Each node carries ``categoryRefinementId``,
        ``name``, ``parentCategoryRefinementId``, ``isTargetable`` and, where the
        service knows it, ``asinCountRange`` with a ``min`` and ``max``.

    .. note::
        Large root categories come back with ``isTargetable`` set to ``false``:
        they have to be narrowed down to their children before they can be used
        as a target.
    """

    _MEDIA = 'application/vnd.sbtargeting.v4+json'

    @sp_endpoint('/sb/targets/categories', method='GET')
    def list_categories(self, supplySource, **kwargs) -> ApiResponse:
        """
        Gets the targetable category tree.

        Keyword Args
            | query **supplySource** (string): [required] ``AMAZON`` or
              ``STREAMING_VIDEO``.
            | query **locale** (string): [optional] Market locale, for instance
              ``es_ES``, ``en_US`` or ``de_DE``.
            | query **includeOnlyRootCategories** (boolean): [optional] Return
              root categories only.
            | query **parentCategoryRefinementId** (string): [optional] Return
              the children of that category.
            | query **nextToken** (string): [optional] Pagination token.

        Returns:
            | ApiResponse, ``200``, with the tree under ``categoryTree``.

        Example node::

            {"categoryRefinementId": "1909624031", "name": "Chupetes",
             "asinCountRange": {"min": 1247, "max": 2078},
             "isTargetable": true, "parentCategoryRefinementId": "1862267031"}
        """
        return self._request(kwargs.pop('path'), params=kwargs,
                             headers={'Accept': self._MEDIA, 'Content-Type': self._MEDIA})

    @sp_endpoint('/sb/targets/categories/{}/refinements', method='GET')
    def list_refinements(self, categoryRefinementId, **kwargs) -> ApiResponse:
        """
        Gets the refinements of a category.

        Keyword Args
            | path **categoryRefinementId** (string): [required]
            | query **locale** (string): [optional]
            | query **nextToken** (string): [optional]

        Returns:
            | ApiResponse, ``200``.
        """
        return self._request(fill_query_params(kwargs.pop('path'), categoryRefinementId),
                             params=kwargs,
                             headers={'Accept': self._MEDIA, 'Content-Type': self._MEDIA})

    @sp_endpoint('/sb/targets/products/count', method='POST')
    def get_product_count(self, category, **kwargs) -> ApiResponse:
        """
        Gets the number of products in a category.

        Request Body [Required]
            | **category** (string): [required] Category refinement identifier.
            | **ageRanges** (array of string): [optional]
            | **brands** (array of string): [optional]
            | **genres** (array of string): [optional]
            | **isPrimeShipping** (boolean): [optional]
            | **ratingRange** ({}): [optional] ``min`` and ``max`` integers.
            | **priceRange** ({}): [optional] ``min`` and ``max`` numbers.

        Returns:
            | ApiResponse, ``200``.

        Raises:
            | ``400`` when ``category`` is missing, naming that member.
        """
        body = {'category': category}
        for key in ('ageRanges', 'brands', 'genres', 'isPrimeShipping',
                    'ratingRange', 'priceRange'):
            if key in kwargs:
                body[key] = kwargs.pop(key)
        return self._request(kwargs.pop('path'),
                             data=Utils.convert_body(body, False),
                             params=kwargs, headers={'Accept': self._MEDIA,
                                                     'Content-Type': self._MEDIA})
