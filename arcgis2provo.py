import xml.etree.ElementTree as ET
from datetime import datetime
from provit import ProvGraph, Activity, Entity, Agent


def serializeArcGISReport(inPath, outPath):
    g = ProvGraph(namespace='https://provBasicExample.org/')

    tree = ET.parse(inPath)
    root = tree.getroot()

    model = root.find('MdModel')

    processes = model.findall('Processes/MdProcess')
    input_identifiers = ['Input raster or feature source data', 'Input raster', 'Input raster or feature region data', 'Input cost raster', 'Clip Features', 'Feature Class Location', 'Erase Features', 'Network Data Source', 'Input Network Analysis Layer',
                         'Input Locations', 'Input Layer', 'Input Package', 'Target Dataset',  'Input Features']
    output_identifiers = ['Output distance raster', 'Output cell size', 'Output raster', 'Output rasters', 'Output feature class', 'Output feature class of neighboring connections', 'Output Feature Class',
                          'Feature Class Name', 'Output Spatial Grid', 'Updated Target Dataset', 'Network Analyst Layer', 'Updated Input Network Analysis Layer', 'Output File', 'Tool Succeeded']

    for process in processes:
        processId = Activity(g, process.find('Name').text.replace(" ", ""))
        processId.label(process.find('Name').text.replace(" ", ""))
        variables = process.findall('Parameters/MdParameter')
        for parameter in variables:
            display_name_of_parameter = parameter.find('DisplayName').text
            if display_name_of_parameter in input_identifiers:
                input_data = Entity(g, parameter.find(
                    'ValueAsText').text.replace(" ", "").split("\\")[-1])
                input_data.label(parameter.find(
                    'ValueAsText').text.replace(" ", "").split("\\")[-1])
                processId.used(input_data)
            if display_name_of_parameter == 'Input rasters':
                param = parameter.findtext('ValueAsText').split(';')
                inputs = []
                dicty = {}
                for input in param:
                    if '\\' in input or ' ' in input:
                        dicty[input.split('\\')[-1].split(' ')
                              [0]] = input.split(' ')[-1]
                    for i in dicty:
                        input_data = Entity(g, i)
                        input_data.label(i)
                        input_data.description("The value of " + i + " for the Activity " + process.find(
                            'Name').text.replace(" ", "") + " is " + dicty[i])
                        processId.used(input_data)

            if display_name_of_parameter == 'Input Datasets':
                param = parameter.findtext('ValueAsText').split(';')
                inputs = []
                for input in param:
                    if '\\' in input:
                        input_data = input.split('\\')[-1]
                        inputs.append(input_data)
                for inp in param:
                    if '\\' not in inp:
                        inps = inp.replace("'", "").replace(" ", "")
                        inputs.append(inps)
                        for i in inputs:
                            input_data = Entity(g, i)
                            input_data.label(i)
                            processId.used(input_data)

            if display_name_of_parameter in output_identifiers:
                output_data = Entity(g, parameter.find(
                    'ValueAsText').text.replace(" ", "").split("\\")[-1])
                output_data.label(parameter.find(
                    'ValueAsText').text.replace(" ", "").split("\\")[-1])
                output_data.wasGeneratedBy(processId)

            if display_name_of_parameter == 'Solve Succeeded':
                out_data = Entity(g, parameter.findtext(
                    'DisplayName').replace(" ", ""))
                out_data.wasGeneratedBy(processId)

    g.serialize(format='ttl', destination=outPath)


# serializeArcGISReport(inPath='./neuerWorkflow-Report.xml',
#                       outPath='./Flow.ttl')

serializeArcGISReport(
    inPath='./SuitabilityCorridorModel-Report.xml', outPath='./SuitabilityCorridorModel-Prov.ttl')

# serializeArcGISReport(inPath='./GasLeaksModel-Report.xml', outPath='./GasLeaks.ttl')

# serializeArcGISReport(inPath='./ParisTransport-Report.xml', outPath='./ParisTransport.ttl')
