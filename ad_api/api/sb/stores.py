import json
import mimetypes

import requests

from ad_api.base import Client, sp_endpoint, ApiResponse


class Stores(Client):
    """
    Use the Amazon Advertising API for Sponsored Brands for campaign, ad group, keyword, negative keyword, drafts, Stores, landing pages, and Brands management operations. For more information about Sponsored Brands, see the Sponsored Brands Support Center. For onboarding information, see the account setup topic.
    """

    @sp_endpoint('/stores/assets', method='GET')
    def list_assets(self, **kwargs) -> ApiResponse:
        """
        For sellers or vendors, gets an array of assets associated with the specified brand entity identifier. Vendors are not required to specify a brand entity identifier, and in this case all assets associated with the vendor are returned.

        Keyword Args
            | query **brandEntityId** (string): For sellers, this field is required. It is the Brand entity identifier of the Brand for which assets are returned. This identifier is retrieved using the getBrands operation. For vendors, this field is optional. If a vendor does not specify this field, all assets associated with the vendor are returned. For more information about the difference between a seller and a vendor, see the Amazon Advertising FAQ. [required]

            | query **mediaType** (string): Specifies the media types used to filter the returned array. Currently, only the brandLogo type is supported. If not specified, all media types are returned. Available values : brandLogo, image [optional]

        Returns:
            | ApiResponse
        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/stores/assets', method='POST')
    def create_asset(self, image, brandEntityId, mediaType='brandLogo', filename=None, **kwargs) -> ApiResponse:
        """
        Creates a new image asset and stores it in the Store Assets Library.

        The endpoint takes ``multipart/form-data`` with two parts, not JSON:

            ``assetInfo``  A JSON string with ``brandEntityId`` and ``mediaType``.
            ``asset``      The image bytes. PNG, JPEG or GIF, under 1MB and at
                           least 400x400 pixels.

        Keyword Args
            | path **image** (str or bytes): A file path, or the raw image bytes. [required]
            | path **brandEntityId** (string): The Brand entity identifier. Required for sellers, optional for vendors. [required]
            | path **mediaType** (string): Only ``brandLogo`` is supported. [optional]
            | path **filename** (string): Name sent in ``Content-Disposition``. Taken from the path when a path is given. [optional]

        Returns:
            | ApiResponse

        Documentation: https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Stores
        """
        if isinstance(image, (str, bytes)):
            if isinstance(image, bytes):
                data = image
            else:
                filename = filename or image.split('/')[-1]
                with open(image, 'rb') as handle:
                    data = handle.read()
        else:
            data = image.read()

        filename = filename or 'image'

        content_type = mimetypes.guess_type(filename)[0] or 'image/png'
        if content_type not in ('image/png', 'image/jpeg', 'image/gif'):
            raise ValueError(f"Unsupported image type {content_type}; use PNG, JPEG or GIF.")

        asset_info = {'brandEntityId': brandEntityId, 'mediaType': mediaType}

        headers = self.headers.copy()
        # requests must set Content-Type itself to add the multipart boundary
        headers.pop('Content-Type', None)
        headers['Accept'] = '*/*'
        headers['Content-Disposition'] = f'attachment; filename="{filename}"'

        response = requests.post(
            self.endpoint + '/stores/assets',
            headers=headers,
            files={
                'assetInfo': (None, json.dumps(asset_info), 'application/json'),
                'asset': (filename, data, content_type),
            },
            params=kwargs,
            timeout=self.timeout or 60,
            proxies=self.proxies,
            verify=self.verify,
        )

        return self._check_response(response)
