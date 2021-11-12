Environment Variables
=====================

******************************
Use with environment variables
******************************

=====================    =========================================================================================================
ENVIRONMENT VARIABLE     DESCRIPTION
=====================    =========================================================================================================
AD_API_REFRESH_TOKEN     The refresh token used obtained via authorization
AD_API_CLIENT_ID         Your login with amazon app id
AD_API_CLIENT_SECRET     Your login with amazon client secret
AD_API_PROFILE_ID        Your profile id as Amazon Ad
=====================    =========================================================================================================

To set environment variables in your python script, use

..  code-block:: python

    import os

    os.environ.setdefault('AD_API_REFRESH_TOKEN', 'Your-Token-Here')
    os.environ.setdefault('AD_API_CLIENT_ID', 'Your-Client_Id-Here')
    os.environ.setdefault('AD_API_CLIENT_SECRET', 'Your-Client_Secret-Here')
    os.environ.setdefault('AD_API_PROFILE_ID', 'Your-Profile_Id-Here')


**************************
Note
**************************

You still need create the .env file or by default the mode configuration will be sandbox for testing

..  code-block:: bash

    # environment variables defined inside a .env file
    # AWS_ENV=SANDBOX
    AWS_ENV=PRODUCTION