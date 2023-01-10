# python-nextgen-issue
A project that recreates a bug on  OpenAPITools/openapi-generator 

Requires python 3.9 and openapitools/openapi-generator-cli:latest in docker (as of 1/10/23)

To reproduce the issue, run `.\build_python_client.ps1` in powershell, install the client by running `pip install -e geojson-client`, then run `python test.py`

The following stacktrace should be returned:
```
Traceback (most recent call last):
  File "[*project root*]\test.py", line 4, in <module>
    import geojson
  File "[*project root*]\geojson-client\geojson\__init__.py", line 21, in <module>
    from geojson.api.geo_json_api import GeoJsonApi
  File "[*project root*]\geojson-client\geojson\api\__init__.py", line 6, in <module>
    from geojson.api.geo_json_api import GeoJsonApi
  File "[*project root*]\geojson-client\geojson\api\geo_json_api.py", line 23, in <module>
    from geojson.models.geo_json_geometry import GeoJsonGeometry
  File "[*project root*]\geojson-client\geojson\models\__init__.py", line 18, in <module>
    from geojson.models.geo_json_geometry import GeoJsonGeometry
  File "[*project root*]\geojson-client\geojson\models\geo_json_geometry.py", line 22, in <module>
    from geojson.models.geometry_collection import GeometryCollection
  File "[*project root*]\geojson-client\geojson\models\geometry_collection.py", line 23, in <module>
    from geojson.models.geo_json_geometry import GeoJsonGeometry
ImportError: cannot import name 'GeoJsonGeometry' from partially initialized module 'geojson.models.geo_json_geometry' (most likely due to a circular import) ([*project root*]\geojson-client\geojson\models\geo_json_geometry.py)
```
