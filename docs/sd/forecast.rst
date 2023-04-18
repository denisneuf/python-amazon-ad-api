Forecasts
=========


.. autoclass:: ad_api.api.sd.Forecast

    Endpoints available

    .. csv-table::
        :widths: 10, 35, 50
        :header: "Method", "Endpoint", "Description"

        "POST", "/sd/forecasts", "Return forecasts for an ad group that may or may not exist."


    .. autofunction:: ad_api.api.sd.Forecast.list_forecasts(self, **kwargs) -> ApiResponse:

