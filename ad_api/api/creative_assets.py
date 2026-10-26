from ad_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Utils


class CreativeAssets(Client):
    """ """

    @sp_endpoint('/assets/register', method='POST')
    def register_asset(self, **kwargs) -> ApiResponse:
        r"""
        register_asset(body: (dict, str, file)) -> ApiResponse

        Registers an uploaded asset with the creative assets library with optional contextual and tagging information.
        The API should be called once the asset is uploaded to the location provided by the /asset/upload API endpoint.

        body: | REQUIRED {'description': 'A caSearchRequestCommon}'

            | **url** | **string** | Required The url to upload the asset. The url expires in 15 minutes.
            | **name** | **string** | Required The name to be given to the asset being registered.
            | **asinList** | **list** | Optional Tagging assets with ASIN, promotes asset discoverability downstream. If ASIN is provided at the time of upload/during asset registration, it is applied as a tag on that asset. This allows for that asset to be searchable using that ASIN#. For e.g., An advertiser may want to search for assets tagged with ASIN BC10001, so they can create a store spotlight ad with product images for that ASIN.
            | **assetType** | **string** | The asset type you are registering [IMAGE]
            | **assetSubTypeList** | **list** | For assetType IMAGE acceptable assetSubTypes are LOGO, PRODUCT_IMAGE, AUTHOR_IMAGE, LIFESTYLE_IMAGE, OTHER_IMAGE.
            | **versionInfo** | **string** | The asset type you are registering [IMAGE]

                | linkedAssetId  | **string** | The registering asset will be created as a new version of this linkedAssetId.
                | versionNotes  | **string** | The version notes that client can associate to the asset.Versioning enables users to update an old asset, so that you can ensure the latest asset is being used. You can upload a new version of an existing asset along with version notes. Any tags/ASINs from previous version, will be retained on the new version too.

            | **tags** | **list** |
            | **registrationContext** | **caRegistrationContext** | This is used on registration of an asset, to associate DSP assets to a specific advertiser. This is required for assets being uploaded for use in DSP.
                | associatedPrograms  | **caAssociatedProgramcaAssociatedProgram** |

                    | **metadata** | **string** | Include key-value pairs related to the asset. For DSP use "dspAdvertiserId" = "ID". Include program as AMAZON_DSP.

                    | **programName** | **string** | Use this field to specify which program you are uploading an asset for. Currently, the accepted value here on registration is to associate an asset with a DSP advertiser. [ AMAZON_DSP ]

            | **associatedSubEntityList** | **caAssociatedSubEntityList** | This field is required for sellers, but not required for vendors. The brandEntityId is required for sellers uploading assets for use in Sponsored Brands. As a best practice, ensure to include brandEntityId when uploading assets for sellers.

                | caAssociatedSubEntity  |

                    | **brandEntityId** | **string** | The entity id of brand, which can be retrieved using GET /brands.

            | **skipAssetSubTypesDetection** | **boolean** | Select true if you want to set an asset to a specific assetSubType, if this is not included the system may reclassify your asset based on specifications.

        """
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs)

    @sp_endpoint('/assets/upload', method='POST')
    def upload_asset(self, **kwargs) -> ApiResponse:
        r"""

        upload_asset(body: (dict, str, file)) -> ApiResponse

        body: | REQUIRED

        |   {
        |   '**fileName**': *string* The fileName of the asset. pattern: [\w]+\.jpg|png|mp4|mov|wmv|avi
        |   }

        """
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs)

    @sp_endpoint('/assets/search', method='POST')
    def search_assets(self, **kwargs) -> ApiResponse:
        r"""

        search_assets(body: (dict, str, file)) -> ApiResponse

        Search the creative asset library.

        body: | REQUIRED {'description': 'A caSearchRequestCommon}'

            | **text** | **string** | The text used for searching assets, it matches asset name, asset name prefix, tags and ASINs associated with the assets
            | **filterCriteria** Optional this is used to filter results, we support two types of filters, valueFilter and rangeFilter

                | valueFilters  | **list** | Filter for certain values of asset attributes

                    | **values** | **list** |

                    | **valueField** | **string** | [ TAG, ASIN, CAMPAIGN_NAME, CAMPAIGN_ID, PROGRAM, ASSET_TYPE, ASSET_SUB_TYPE, APPROVED_AD_POLICY, ASSET_EXTENSION ]

                | rangeFilters

                    | **range** | **list** | Filter assets which have certain ranges of asset attributes. For example, filter assets which have file size in the range of [10,20] or [40,50].

                        | **start** | **string** |

                        | **end** | **string** |

            | **sortCriteria** Optional this is used to get sorted results

                | field  | **string** | Enum [ CREATED_TIME, SIZE, NAME, IMAGE_HEIGHT, IMAGE_WIDTH, EXTENSION ]

                | order  | **string** | Enum [ ASC, DESC ]

            | **pageCriteria** Optional this is used for pagination when searching for the first page, no need to put anything, otherwise, use the token returned from previous search call

                | identifier  | **dict** |

                    | **pageNumber** | **int** |

                    | **token** | **string** |

                | size  | **int** | default: 25 minimum: 1 maximum: 500

        """
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs)

    @sp_endpoint('/assets', method='GET')
    def get_asset(self, **kwargs) -> ApiResponse:
        r"""

        get_asset(assetId: str, version: str) -> ApiResponse

        Retrieves an asset along with the metadata

        query **assetId**:*string* | Required. The assetId

        query **version**:*string* | Optional. The versionId of the asset, if not included all versions will return.

        """
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/assets/batchRegister', method='POST')
    def batch_register_assets(self, **kwargs) -> ApiResponse:
        r"""
        Registers several uploaded assets in one call.

        This route is asynchronous. It answers a ``requestId`` and nothing else,
        so the result has to be read with ``get_batch_register_status``.

        Request Body (required)

        - ``assetDetailsList`` (array): between 1 and 50 entries, each one shaped
          like the body ``register_asset`` accepts:

          - ``url`` (string): where the file sits, from ``upload_asset``.
          - ``name`` (string): the name to give the asset.
          - ``assetType`` (string): ``IMAGE``.
          - ``assetSubTypeList`` (array): ``LOGO``, ``PRODUCT_IMAGE``,
            ``AUTHOR_IMAGE``, ``LIFESTYLE_IMAGE`` or ``OTHER_IMAGE``.
          - ``asinList`` (array): tags the asset with ASINs, so it can be found
            by product later.
          - ``associatedPrograms`` (array): up to 100 entries, one per program
            the asset belongs to.
          - ``otherMetadata`` (object): free key-value pairs of strings.
          - ``tagList`` (array): tags for the asset.
          - ``versionInfo`` (object): ``linkedAssetId`` and ``versionNotes``, to
            register this file as a new version of an existing asset.
          - ``skipAssetSubTypesDetection`` (boolean): keep the subtype as given
            instead of letting the service reclassify it.

        - ``batchRegistrationContext`` (object): the context applied to the whole
          batch.

        Returns
            ApiResponse with ``requestId``, which ``get_batch_register_status``
            takes.

        """
        headers = {
            'Accept': 'application/vnd.assetsbatchregisterresponse.v1+json',
            'Content-Type': 'application/vnd.assetsbatchregisterrequest.v1+json',
        }
        body = Utils.convert_body(kwargs.pop('body'), wrap=False)
        return self._request(kwargs.pop('path'), data=body, params=kwargs, headers=headers)

    @sp_endpoint('/assets/batchRegister/{}', method='GET')
    def get_batch_register_status(self, requestId, **kwargs) -> ApiResponse:
        r"""
        Reports whether a batch registration has finished.

        The ``requestId`` comes from ``batch_register_assets``. An id the service
        does not know answers ``400`` with
        ``AARServiceBadRequestException ... No request exists for the requestId``,
        not a ``404``: the route answers either way, and the message says the id
        was not found.

        Path

        - ``requestId`` (string): required. The identifier the batch call
          returned.

        Returns
            ApiResponse with the state of that batch.

        """
        headers = {'Accept': 'application/vnd.creativeassetsgetbatchregisterresponse.v3+json'}
        return self._request(fill_query_params(kwargs.pop('path'), requestId),
                             params=kwargs, headers=headers)
