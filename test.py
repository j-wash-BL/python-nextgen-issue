from __future__ import print_function

import time
import geojson
from geojson.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = geojson.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with geojson.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geojson.GeoJsonApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.get_geojson()
        print("The response of GeoJsonApi->get_geojson:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GeoJsonApi->get_geojson: %s\n" % e)
