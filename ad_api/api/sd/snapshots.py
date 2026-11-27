from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class Snapshots(Client):
    """
    Request and read Sponsored Display snapshots.

    A snapshot is an asynchronous record of what the account held at a moment:
    the POST asks for one and answers 202 with no body, and the GET polls by
    snapshot id until the record is ready. Both routes are marked deprecated in
    the 3.0 contract, so they may stop answering; they are kept because the
    account still uses them.

    The contract also carries GET /sd/snapshots/{snapshotId}/download, which
    answers 307 and redirects to the file. It is not wrapped here: a direct
    download of the location returned by get_snapshot answers 401 unless the
    client sends its own headers, which download_snapshot below already does.
    """

    @sp_endpoint('/sd/{}/snapshot', method='POST')
    def post_snapshot(self, recordType, **kwargs) -> ApiResponse:
        """
        Requests a snapshot of one record type.

        The contract answers 202 with an empty body and no snapshot id, so the
        id has to be read from the account afterwards. Marked deprecated in the
        3.0 contract.

        Keyword Args
            | path **recordType** (string): the record the snapshot covers. [required]

        Returns:
            | ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), recordType), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs)

    @sp_endpoint('/sd/snapshots/{}', method='GET')
    def get_snapshot(self, snapshotId, **kwargs) -> ApiResponse:
        r"""
        Gets the status of a requested snapshot.

        Answers 202 while the record is still being built. Once it is ready the
        location field points at the file, and passing that location to
        download_snapshot saves it. Marked deprecated in the 3.0 contract.

        Keyword Args
            | path **snapshotId** (string): the identifier of the snapshot. [required]

        Returns:
            | ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), snapshotId), params=kwargs)

    def download_snapshot(self, **kwargs) -> ApiResponse:
        r"""
        Downloads the snapshot previously get report specified by location (this is not part of the official Amazon Advertising API, is a helper method to download the snapshot). Take in mind that a direct download of location returned in get_snapshot will return 401 - Unauthorized.

        kwarg parameter **file** if not provided will take the default amazon name from path download (add a path with slash / if you want a specific folder, do not add extension as the return will provide the right extension based on format choosed if needed)

        kwarg parameter **format** if not provided a format will return a url to download the snapshot (this url has a expiration time)

        Keyword Args
            | **url** (string): the location obtained from get_snapshot [required]
            | **file** (string): The path to save the file if mode is download json, zip or gzip. [optional]
            | **format** (string): The mode to download the snapshot: data (list), raw, url, json, zip, gzip. Default (url) [optional]

        Returns:
            ApiResponse
        """
        return self._download(self, params=kwargs)
