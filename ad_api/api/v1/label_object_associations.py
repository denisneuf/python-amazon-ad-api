from ad_api.base import Client, sp_endpoint, ApiResponse, Utils


class LabelObjectAssociations(Client):
    r"""
    LabelObjectAssociations(account='default', marketplace: Marketplaces = Marketplaces.EU, credentials=None, debug=False)

    Amazon Ads API v1 - label to object associations

    One route, read only:

        POST /adsApi/v1/query/labelObjectAssociations

    Labels itself lists the labels that exist. This family lists what each
    label is applied to, so the pair answers "which labels do I have" and
    "what is tagged".

    The required member is ``labelObjectTypeFilter``, not the adProductFilter
    the campaign families carry, and it takes exactly one value:

        AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP
    """

    @sp_endpoint('/adsApi/v1/query/labelObjectAssociations', method='POST')
    def query_label_object_associations(self, **kwargs) -> ApiResponse:
        r"""
        query_label_object_associations(body: dict) -> ApiResponse

        Amazon Ads API v1 - Query Label Object Associations (operationId: QueryLabelObjectAssociation)

        Request Body [Required]
            | **labelObjectTypeFilter** (dict) : [required] exactly one value
                | **include** (list<LabelObjectType>) : Enum [ AD_GROUP, CAMPAIGN, DEAL, INVENTORY_GROUP ]
            | **adProductFilter** (dict) : [optional] exactly one value
            | **labelIdFilter** (dict) : [optional] 1..50 ids
            | **labelObjectIdFilter** (dict) : [optional] 1..50 ids
            | **maxResults** (int) : 1..5000, default 100
            | **nextToken** (string)

        Returns
            | **labelObjectAssociations** (list<LabelObjectAssociation>) : 0..5000
                | **labelObjectAssociationId** (string) : [required]
                | **labelId** (string) : [required] the label being applied
                | **labelObjectId** (string) : [required] the object, e.g. a deal id or an ad group id
                | **labelObjectType** (LabelObjectType) : [required]
                | **adProduct** (AdProduct)
            | **nextToken** (string)

        maxResults reaches 5000 here, far above the 100 of the campaign
        families, because associations grow with the number of tagged objects.

        Requires one of these permissions:
            campaign_edit, campaign_view
        """
        schema_version = 'application/json'
        headers = {"Accept": schema_version, "Content-Type": schema_version}
        return self._request(kwargs.pop('path'), data=Utils.convert_body(kwargs.pop('body'), False), params=kwargs, headers=headers)
