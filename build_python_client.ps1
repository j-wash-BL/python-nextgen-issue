remove-item -recurse .\geojson-client\*

docker run --rm -v "${PWD}/:/output" -v "${PWD}:/input" openapitools/openapi-generator-cli:latest generate `
   -g python-nextgen `
   -i /input/geojson_spec.v1.yml `
   -o /output/geojson-client `
   --additional-properties=packageName=geojson `
   --additional-properties=packageVersion=2.4.5