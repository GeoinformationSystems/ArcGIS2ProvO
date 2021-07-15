__--- work in progress ---__

# ArcGIS2PROVO

ArcGIS2PROVO is a software to convert ArcGIS model builder workflows to a provenance graph according to the PROV-Ontology (https://www.w3.org/TR/prov-o/). After running a model in ArcGIS, an XML model report can be generated. This report is used as input for the software.

# Structure

ArcGIS2PROVO is written in Python. It can be used from the command line:

 ```~ arcgis2provo.py modelReport.xml```

# Used Packages

- provo: https://github.com/GeoinformationSystems/ProvIt/tree/master
- rdflib: https://rdflib.readthedocs.io/en/stable/
- datetime: https://docs.python.org/3/library/datetime.html
- xml: https://docs.python.org/3/library/xml.html

# License
