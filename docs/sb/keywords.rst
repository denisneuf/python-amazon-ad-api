Keywords
========

.. autoclass:: ad_api.api.sb.Keywords

    .. autofunction:: ad_api.api.sb.Keywords.list_keywords(self, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sb.keywords import Keywords

            result = Keywords().list_keywords()
            print(result)

    .. autofunction:: ad_api.api.sb.Keywords.edit_keywords(self, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sb.keywords import Keywords

            file = open("edit.json")
            data = file.read()
            file.close()
            result = Keywords().edit_keywords(
                body=data
            )
            print(result)


        ### Example json

        .. literalinclude:: ../../test/keywords/sb-sx-edit-keywords.json

    .. autofunction:: ad_api.api.sb.Keywords.create_keywords(self, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sb.keywords import Keywords

            file = open("create.json")
            data = file.read()
            file.close()
            result = Keywords().create_keywords(
                body=data
            )
            logging.info(result)

        ### Example json

        .. literalinclude:: ../../test/keywords/sb-sx-create-keywords.json

    .. autofunction:: ad_api.api.sb.Keywords.get_keyword(self, keywordId, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sb.keywords import Keywords

            keyword_id = 144148613757234151
            result = Keywords().get_keyword(
                keywordId=keyword_id
            )
            print(result)

    .. autofunction:: ad_api.api.sb.Keywords.delete_keyword(self, keywordId, **kwargs) -> ApiResponse:

        ### Example python

        .. code-block:: python

            from ad_api.api.sb.keywords import Keywords

            keyword_id = 144148613757234151
            result = Keywords().delete_keyword(
                keywordId=keyword_id
            )
            print(result)
