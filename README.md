# ArcGIS2PROVO

ArcGIS2PROVO is a tool to convert ArcGIS model builder workflows to a provenance graph according to the PROV-Ontology (https://www.w3.org/TR/prov-o/). After running a model in ArcGIS, an XML model report can be generated. This report is used as input for the tool.

# Structure

ArcGIS2PROVO is written in Python 3. It can be used from the command line:

```bash
# specifiy output name:
arcGIS2ProvO.py <path-to-arcgis-model-report>.xml <destination-of-output>.ttl

# or copy name from input:
arcGIS2ProvO.py <path-to-arcgis-model-report>.xml
```

# Required Packages

- provo: https://github.com/GeoinformationSystems/ProvIt/tree/master
- rdflib: https://rdflib.readthedocs.io/en/stable/
- xml: https://docs.python.org/3/library/xml.html

# License

# Contact
Arne Rümmler ([arne.ruemmler@tu-dresden.de](mailto:arne.ruemmler@tu-dresden.de))
