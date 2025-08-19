Themes
======

.. autoclass:: ad_api.api.sb.Themes

   .. autofunction:: ad_api.api.sb.Themes.list_themes

      ### Example Python

      .. code-block:: python

         from ad_api.api.sb.themes import Themes

         result = Themes().list_themes()
         print(result)

   .. autofunction:: ad_api.api.sb.Themes.create_themes

      ### Example Python

      .. code-block:: python

         from ad_api.api.sb.themes import Themes
         import json

         # Example data for themes
         themes_to_create = [
             {
                 "adGroupId": "YOUR_ADGROUP_ID",
                 "campaignId": "YOUR_CAMPAIGN_ID",
                 "themeType": "KEYWORDS_RELATED_TO_YOUR_BRAND",
                 "bid": 0.75
             }
             # Add more theme objects as needed, up to 100
         ]

         # For a real scenario, you might read this from a file like in your Keywords example
         # file = open("create_themes.json")
         # data = file.read()
         # file.close()
         # result = Themes().create_themes(body=data)

         result = Themes().create_themes(themes=themes_to_create)
         print(result)

      ### Example JSON (for request body)

      .. code-block:: json

         {
             "themes": [
                 {
                     "adGroupId": "string",
                     "campaignId": "string",
                     "themeType": "KEYWORDS_RELATED_TO_YOUR_BRAND|KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES",
                     "bid": 0.75
                 }
             ]
         }


   .. autofunction:: ad_api.api.sb.Themes.update_themes

      ### Example Python

      .. code-block:: python

         from ad_api.api.sb.themes import Themes
         import json

         # Example data for themes to update
         themes_to_update = [
             {
                 "themeId": "YOUR_THEME_ID",
                 "adGroupId": "YOUR_ADGROUP_ID",
                 "campaignId": "YOUR_CAMPAIGN_ID",
                 "state": "paused", # or "enabled", "archived"
                 "bid": 0.80 # Optional, if updating bid
             }
             # Add more theme objects as needed, up to 100
         ]

         # For a real scenario, you might read this from a file
         # file = open("update_themes.json")
         # data = file.read()
         # file.close()
         # result = Themes().update_themes(body=data)

         result = Themes().update_themes(themes=themes_to_update)
         print(result)

      ### Example JSON (for request body)

      .. code-block:: json

         {
             "themes": [
                 {
                     "themeId": "string",
                     "adGroupId": "string",
                     "campaignId": "string",
                     "state": "enabled|paused|archived",
                     "bid": 0.80
                 }
             ]
         }