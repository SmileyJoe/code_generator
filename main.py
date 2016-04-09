# -*- coding: utf-8 -*-
import json
import os
import template
from function import *
from constant import *
from pprint import pprint
from class_builder import ClassBuilder

jsonDir = "json"
javaDir = "java"
acceptedExtension = "json"
builder = ClassBuilder()

files = getFiles(jsonDir, acceptedExtension)

for file in files:
    filename = os.path.splitext(file)[0]

    with open(jsonDir + "/" + file) as dataFile:
        data = json.load(dataFile)

    pprint(data)

    builder.setClassName(uppercaseFirst(filename))
    builder.setItems(data)

    with open(javaDir + "/" + builder.getClassName() + ".java", "w+") as f:
        f.write(builder.build())