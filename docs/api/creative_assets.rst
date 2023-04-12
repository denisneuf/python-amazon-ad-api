Creative Asset Library beta
===========================
`https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml`_

.. _https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml: https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/creative-asset-library/creative-asset-library-openapi.yaml

Advertisers can use creative assets to store, organize and reuse brand content, such as logos, images, etc. Stored content can be used for Amazon Ads and on Amazon shopping pages. Creative assets enables brands to provide a consistent shopping experience by easily applying brand content across Amazon.

.. autoclass:: ad_api.api.CreativeAssets

    .. autofunction:: ad_api.api.CreativeAssets.search_assets

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import CreativeAssets
        from ad_api.base import AdvertisingApiException

        def search_assets(data: dict or str):
            try:
                result = CreativeAssets(debug=True).search_assets(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            search = \
                {
                    "text": "Logo",
                    "filterCriteria": {
                        "valueFilters": [
                            {
                                "values": [
                                    "B08XW4FDJV"
                                ],
                                "valueField": "ASIN"
                            }
                        ]
                    },
                    "sortCriteria": {
                        "field": "CREATED_TIME",
                        "order": "ASC"
                    }
                }

        # If you send a empty query search = {} it will return all the assets in library
        search_assets(search)

    ### Example search.json

    Download :download:`json <../../test/creative_assets/search.json>` template

    .. literalinclude:: ../../test/creative_assets/search.json

    .. autofunction:: ad_api.api.CreativeAssets.get_asset

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import CreativeAssets
        from ad_api.base import AdvertisingApiException


        def get_asset(**kwargs):
            try:
                result = CreativeAssets(debug=True).get_asset(
                    **kwargs
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            amz_asset_id = "amzn1.assetlibrary.asset1.c2867a8671670fc7a5d0bf1efa295d599"
            amz_version = "version_v3"
            # get a specific version of the asset
            get_asset(assetId=amz_asset_id, version=amz_version)
            # get all versions of the asset
            get_asset(assetId=amz_asset_id)


    .. autofunction:: ad_api.api.CreativeAssets.upload_asset

    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import CreativeAssets
        from ad_api.base import AdvertisingApiException


        def upload_asset(data: dict or str):
            try:
                result = CreativeAssets(debug=True).upload_asset(
                    body=data
                )

                url = result.payload.get("url")
                logging.info(url)

            except AdvertisingApiException as error:
                logging.info(error)

        if __name__ == '__main__':

            file_name = "Sample-1000x1000.jpeg"

            asset = \
                {
                    "fileName": file_name
                }

            upload_asset(asset)

    .. warning:: After upload the assets it will return a url is the url location to which you will be uploading your asset

    .. note:: This is not part of the Creative Assets api is just an example to upload the file using requests in python if your response.status_code is 200 everything is fine

    .. code-block:: python

        from requests import request


        def upload_file(_method, _url, _img):

            response = request(
                _method,
                _url,
                data=open(_img, 'rb')
            )

            logging.info(response.status_code)
            logging.info(response.headers)
            logging.info(response.content)
            logging.info(response.raw)


        if __name__ == '__main__':

            file_name = "Sample-1200x1200.jpeg"
            url = "https://al-eu-726f4d26-7fdb.s3-accelerate.amazonaws.com/037764c3-6b70-4da9-b9af-8ef6ed136def.jpeg?x-amz-meta-filename=Sample-1200x1200.jpeg&X-Amz-Security-Token=token&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220421T035013Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=credential%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a9cbeb0bd3d31e0c1a71c4ad27be23cd7725438581cc4e8a1f9f3f8d"
            method = "PUT"
            upload_file(method, url, file_name)

    .. autofunction:: ad_api.api.CreativeAssets.register_asset


    ### Example python

    .. code-block:: python

        import logging
        from ad_api.api import CreativeAssets
        from ad_api.base import AdvertisingApiException


        def register_asset(data: dict or str):
            try:
                result = CreativeAssets(debug=True).register_asset(
                    body=data
                )

                logging.info(result)

            except AdvertisingApiException as error:
                logging.info(error)


        if __name__ == '__main__':

            # the url was obtained with upload_asset method and was used to upload the file and finally register
            url = "https://al-eu-726f4d26-7fdb.s3-accelerate.amazonaws.com/037764c3-6b70-4da9-b9af-8ef6ed136def.jpeg?x-amz-meta-filename=Sample-1200x1200.jpeg&X-Amz-Security-Token=token&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220421T035013Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=credential%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a9cbeb0bd3d31e0c1a71c4ad27be23cd7725438581cc4e8a1f9f3f8d"

            # register and assets already uploaded as a new asset
            register = \
                {
                    "url": url,
                    "name": "PRODUCT-IMAGE-NAME",
                    "assetType": "IMAGE",
                    "assetSubTypeList": [
                        "PRODUCT_IMAGE"
                    ],
                    "associatedSubEntityList": [
                        {
                            "brandEntityId": "ENTITY288756GCCQ6CF"
                        }
                    ],
                    "skipAssetSubTypesDetection": True
                }


            # register and assets already uploaded as a new version of an existing assets

            register = \
                {
                    "url": url,
                    "name": "PRODUCT-IMAGE-NAME-2",
                    "assetType": "IMAGE",
                    "assetSubTypeList": [
                        "PRODUCT_IMAGE"
                    ],
                    "versionInfo": {
                        "linkedAssetId": "amzn1.assetlibrary.asset1.c2867a8671670fc7a5d0bf1efa295d599",
                        "versionNotes": "version v2 of an existing asset"
                    },
                    "associatedSubEntityList": [
                        {
                            "brandEntityId": "ENTITY1234567890123"
                        }
                    ],
                    "skipAssetSubTypesDetection": True
                }


            register_asset(register)