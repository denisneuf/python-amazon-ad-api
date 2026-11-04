from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Exports(Client):
    """
    Ask for a snapshot of one entity type and poll it until it is ready.

    Four routes request an export, one per entity, and a fifth reads the result.
    A request answers 202 with an export id; the file is built afterwards, so the
    id is polled until its status reads COMPLETED and a download url appears.

    The route picks the entity, not the body: /ads/export exports ads,
    /campaigns/export exports campaigns, and so on. The body only narrows which
    rows of that entity come back, by ad product and by state.

    The status moves through PROCESSING, COMPLETED and FAILED. Only COMPLETED
    carries a url, and that url expires at urlExpiresAt. On FAILED the answer
    carries an error object with the reason.

    Every route names its own media type, application/vnd.<entity>export.v<n>+json,
    built from the entity and the version argument. The service routes on that
    type, so the wrong one answers 406.
    """
    @sp_endpoint('/ads/export', method='POST')
    def ads_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the ads.

        Keyword Args
            | body **body** (string | dict): filters. Every field is optional, and
              omitting one leaves its default in place.
                | **adProductFilter** (array): which ad products to include. One to
                  three of SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS.
                  Omitted, all three are included.
                | **stateFilter** (array): which states to include. One to three of
                  ARCHIVED, ENABLED, PAUSED. Omitted, only ENABLED and PAUSED come
                  back, never ARCHIVED.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id
        """
        content_type = 'application/vnd.adsexport.v' + str(version) + '+json'
        accept = 'application/vnd.adsexport.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/campaigns/export', method='POST')
    def campaigns_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the campaigns.

        Keyword Args
            | body **body** (string | dict): filters. Every field is optional, and
              omitting one leaves its default in place.
                | **adProductFilter** (array): which ad products to include. One to
                  three of SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS.
                  Omitted, all three are included.
                | **stateFilter** (array): which states to include. One to three of
                  ARCHIVED, ENABLED, PAUSED. Omitted, only ENABLED and PAUSED come
                  back, never ARCHIVED.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id
        """
        content_type = 'application/vnd.campaignsexport.v' + str(version) + '+json'
        accept = 'application/vnd.campaignsexport.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adGroups/export', method='POST')
    def adgroups_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the ad groups.

        Keyword Args
            | body **body** (string | dict): filters. Every field is optional, and
              omitting one leaves its default in place.
                | **adProductFilter** (array): which ad products to include. One to
                  three of SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS.
                  Omitted, all three are included.
                | **stateFilter** (array): which states to include. One to three of
                  ARCHIVED, ENABLED, PAUSED. Omitted, only ENABLED and PAUSED come
                  back, never ARCHIVED.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id
        """
        content_type = 'application/vnd.adgroupsexport.v' + str(version) + '+json'
        accept = 'application/vnd.adgroupsexport.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/targets/export', method='POST')
    def targets_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the targets.

        This route adds two filters of its own on top of the shared pair.

        Keyword Args
            | body **body** (string | dict): filters. Every field is optional, and
              omitting one leaves its default in place.
                | **adProductFilter** (array): which ad products to include. One to
                  three of SPONSORED_BRANDS, SPONSORED_DISPLAY, SPONSORED_PRODUCTS.
                  Omitted, all three are included.
                | **stateFilter** (array): which states to include. One to three of
                  ARCHIVED, ENABLED, PAUSED. Omitted, only ENABLED and PAUSED come
                  back, never ARCHIVED.
                | **negativeFilter** (array): booleans choosing negative targets,
                  positive targets, or both. Omitted, both come back.
                | **targetLevelFilter** (array): AD_GROUP, CAMPAIGN, or both.
                  Omitted, both levels come back.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id
        """
        content_type = 'application/vnd.targetsexport.v' + str(version) + '+json'
        accept = 'application/vnd.targetsexport.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/exports/{}', method='GET')
    def get_export(self, exportId, typeExport, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Reads the state of an export requested earlier.

        Answers the export with its status and, once COMPLETED, the download url
        and its expiry. A FAILED export carries an error object instead.

        Keyword Args
            | path **exportId** (string): the id returned when the export was
              requested. [required]
            | **typeExport** (string): the entity the export covers, used to build
              the media type: ads, campaigns, adGroups or targets. [required]
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse
                | **exportId** (string), **status** (string)
                | **url** (string), **urlExpiresAt** (string)
                | **createdAt**, **generatedAt**, **fileSize**, **error**
        """
        content_type = 'application/vnd.' + typeExport + 'export.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': content_type}
        return self._request(fill_query_params(kwargs.pop('path'), exportId), params=kwargs, headers=headers)
