# -*- coding: utf-8 -*-
import json
import os
from function import *
from constant import *
from pprint import pprint

fullFilename = "test.txt"
filename = os.path.splitext(fullFilename)[0]

with open(fullFilename) as dataFile:
    data = json.load(dataFile)

print data["name"]

pprint(data)
className = uppercaseFirst(filename)

contents = "public class " + className + "(){" + newline
variables = ""
getters = ""
setters = ""
constants = ""
fromApiItems = ""

for key, value in data.iteritems():
    varTypeClass = ""
    varTypeArray = ""
    if isinstance(value, int):
        varType = "int"
    elif isinstance(value, list):
        varTypeArray = uppercaseFirst(toCamelCase(key))
        varType = "ArrayList<{varName}>".format(
            varName=varTypeArray)
        varTypeClass = "JsonArray"
    elif isinstance(value, dict):
        varType = uppercaseFirst(toCamelCase(key))
        varTypeClass = "JsonObject"
    elif isinstance(value, float):
        varType = "float"
    else:
        varType = "String"

    if not varTypeArray:
        varTypeArray = varType

    fromApiItems += fromApiItem(varTypeArray, varTypeClass, key)
    constants += tagConstant(key)
    key = toCamelCase(key)
    variables += variable(varType, key)
    setters += setter(varType, key)
    getters += getter(varType, key)

contents += newline + constants + newline + \
variables + newline + \
setters + \
getters + \
fromApi(className, fromApiItems) + "}"

with open(className + ".java", "w+") as f:
    f.write(contents)