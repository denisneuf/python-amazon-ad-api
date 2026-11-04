from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Exports(Client):
    """
    Ask for a snapshot of one entity type and poll it until it is ready.

    Four routes request an export, one per entity, and a fifth reads the result.
    A request answers 202 with an export id; the file is built afterwards, so the
    id is polled until its status reads COMPLETED and a download url appears.

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
            | body **body** (string | dict): filters for the export.
                | **adProductFilter** (array): the ad products to include.
                | **stateFilter** (array): the states to include.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id

        """
        content_type = 'application/vnd.adsexport.v'+ str(version) +'+json'
        accept = 'application/vnd.adsexport.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/campaigns/export', method='POST')
    def campaigns_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the campaigns.

        Keyword Args
            | body **body** (string | dict): filters for the export.
                | **adProductFilter** (array): the ad products to include.
                | **stateFilter** (array): the states to include.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id

        """
        content_type = 'application/vnd.campaignsexport.v'+ str(version) +'+json'
        accept = 'application/vnd.campaignsexport.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/adGroups/export', method='POST')
    def adgroups_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the ad groups.

        Keyword Args
            | body **body** (string | dict): filters for the export.
                | **adProductFilter** (array): the ad products to include.
                | **stateFilter** (array): the states to include.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id

        """
        content_type = 'application/vnd.adgroupsexport.v'+ str(version) +'+json'
        accept = 'application/vnd.adgroupsexport.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/targets/export', method='POST')
    def targets_export(self, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Requests an export of the targets.

        This one takes its own request schema, TargetsUniversalApiExportRequest,
        which declares no fields of its own, so an empty body is accepted.

        Keyword Args
            | body **body** (string | dict): filters for the export.
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse, 202 with an export id

        """
        content_type = 'application/vnd.targetsexport.v'+ str(version) +'+json'
        accept = 'application/vnd.targetsexport.v'+ str(version) +'+json'
        headers = {'Content-Type': content_type, 'Accept': accept}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)

    @sp_endpoint('/exports/{}', method='GET')
    def get_export(self, exportId, typeExport, version: int = 1, **kwargs) -> ApiResponse:
        r"""
        Reads the state of an export requested earlier.

        Answers the export with its status and, once COMPLETED, the download url
        and its expiry. A FAILED export carries an error object instead.

        Keyword Args
            | path **exportId** (string): the id returned when the export was requested. [required]
            | **typeExport** (string): the entity the export covers, used to build
              the media type: ads, campaigns, adGroups or targets. [required]
            | **version** (int): media type version. Defaults to 1.

        Returns:
            | ApiResponse
                | **exportId** (string), **status** (string)
                | **url** (string), **urlExpiresAt** (string)
                | **createdAt**, **generatedAt**, **fileSize**, **error**

        """
        content_type = 'application/vnd.'+typeExport+'export.v' + str(version) + '+json'
        headers = {'Content-Type': content_type, 'Accept': content_type}
        return self._request(fill_query_params(kwargs.pop('path'), exportId), params=kwargs, headers=headers)
