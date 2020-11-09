import xml.etree.ElementTree as ET
from datetime import datetime
import os

# test
tree = ET.parse('SuitabilityCorridorModel-Report.xml')
root = tree.getroot()


model = root.find('MdModel')
# model = root.findall('MdModel')[0] -> get first element from list

processes = model.findall('Processes/MdProcess')
activities = {}
for process in processes:
  processName = process.find('Name').text
  # find according toolbox from the path of the tool that was used
  pathName = process.findtext('Tool/PathName').split(os.sep)
  while pathName:
    if pathName[0] == r'ArcToolbox':
      break
    else:
      pathName.pop(0)
  # Note the *s instead of just s in os.path.join(*s). Using the asterisk will trigger 
  # the unpacking of the list, which means that each list argument will be supplied 
  # to the function as a separate argument.
  pathName = os.path.join(*pathName)
  print(pathName)


  parameters = process.findall('Parameters/MdParameter')
  # ParameterType tag in XML -> 0: mandatory; 1: optional

  params = []
  for parameter in parameters:
    param = {}
    param['name'] = parameter.find('DisplayName').text
    param['direction'] = parameter.find('ParameterDirection').text
    if int(parameter.find('ParameterType').text) == 0:
      param['mandatory'] = True
    else:
      param['mandatory'] = False
    # no value maps to 'None'
    param['value'] = parameter.find('ValueAsText').text
    if param['value'] != None:
      params.append(param)
  # print(params)
    


    

#   for inp in parameter:
#     currentInp = inp.findtext('DisplayName')

#     if 'Input ' in currentInp:
#       inps = inp.findtext('ValueAsText').replace(" ", "").split("\\")[-1]
#       inputs.append(inps)
#       if inp.findtext('ValueAsText') == '':
#         inputs.remove('')
#       #print(inputs)

#   values.append(inputs)

#   for out in parameter:
#     currentOut = out.findtext('DisplayName')

#     if 'Output ' in currentOut:
#       outs = out.findtext('ValueAsText').replace(" ", "").split("\\")[-1]
#       outputs.append(outs)
#       if out.findtext('ValueAsText') == '':
#         outputs.remove('')

#       #print(outputs)
  
#   values.append(outputs)

#   for entity in parameter:
#     currentEnt = entity.findtext('ValueAsText')
    
#     if 'VALUE ' in currentEnt:
#       inp_weighted = entity.findtext('ValueAsText').split("\\")
#       #print(inp_weighted)
#       inputs_weightedSum = []
#       values_weightedSum = []
#       for i in inp_weighted:
#         if "VALUE " in i:
#           #print(i)
#           inputs_weighted = i.replace(" VALUE 0,1;D:", "").replace(" VALUE 1;D:", "").replace(" VALUE 0,4;D:", "").replace(" VALUE 1", "")
#           #print(inputs_weighted)
#           values_weighted = i.replace("Ruggedness_Reclassified ", "").replace("Distance_to_Roads_Reclassified ", "").replace("Land_Cover_Reclassified ", "").replace("Protected_Status_Reclassified ", "").replace(";D:", "")
#           #print(values_weighted)

#           inputs_weightedSum.append(inputs_weighted)
#           values_weightedSum.append(values_weighted)

#     if process.findtext('Name') == 'Weighted Sum':
#       key = process.findtext('Name').replace(" ", "")
#       values = [process.find('Tool/PathName').text[38:], inputs_weightedSum, outputs, values_weightedSum]
              
  
#   activities[key] = values

# print(activities)

     
    
#Start- und Endzeit, hier muss der Prozess noch dazu

#startingTime = model.findall(".//GPMessage[MessageType='2']")
#print(startingTime)


# for i in startingTime:
#   starting = i.findtext('MessageDescription').replace("Start Time: ", "")
#   for i in startingTime:
#     start = datetime.strptime(starting, "%A, %d. %B %Y %H:%M:%S") #Fehlermeldung verstehe ich nicht 

# print(start)

# startTime = {}

# for start in startingTime:
#   key = start.findtext('Name')
#   value = [start.findtext('MessageType'), start.findtext('MessageDescription').replace("Start Time: ", "")]
#   startTime[key] = value

#   print(startTime)


# endingTime = model.findall(".//GPMessage[MessageType='3']")
# print(endingTime)

#datetime-Format s.o., wenn oben funktioniert 

# endTime = {}

# for end in endingTime:
#   key = end.findtext('Name')
# for end in endingTime:
#   value = [end.findtext('MessageType'), end.findtext('MessageDescription').replace("Succeeded at ", "").replace("(Elapsed Time: ", "").replace("seconds)", "").replace(" 10,39 ", "").replace(" 5,74 ", "").replace(" 2,21 ", "").replace(" 1,67 ", "").replace(" 2,07 ", "").replace(" 1,73 ", "").replace(" 3,07 ", "").replace(" 29,84 ", "")] #wie geht das, wenn man das zusammenfassen möchte?
#   endTime[key] = value

#   print(endTime)



# #Übertragung ins PROV-O
# from provit import ProvGraph, Activity, Entity, Agent

# # setup the graph object (subclass of an rdflib-graph)
# g = ProvGraph(namespace='https://provBasicExample.org/')
# # elements = []


# for key, val in activity.items():
#   # {key: [path, [inputs], [outputs]]}
#   for index, v in range(val):
    
#       pathName = v[0]
    
#       inputEntities = []
#       for inputEnt in v[1]:
#         inputEntities.append(Entity(g, inputEnt))

#       for descrip in v[3]:        #kann man das so programnmieren?
#         inputEntities.append(inputEnt.description(descrip))
      
#       outputEntities = []
#       for outputEnt in v[2]:
#         outputEntities.append(Entity(g, outputEnt))

#   activity = Activity(g, key)
#   activity.description(pathName)
#   g.link(
#     inputs=inputEntities,
#     process=activity,
#     outputs=outputEntities
#   )

# path = './examples/out/provBasicExample_n3.rdf'
# g.serialize(format = 'n3', destination = path)


