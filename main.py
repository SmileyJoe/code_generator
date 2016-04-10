# -*- coding: utf-8 -*-
import json
import os
import template
from function import *
from constant import *
from pprint import pprint
from class_builder import ClassBuilder
import sys

jsonDir = "json"
javaDir = "java"
acceptedExtension = "json"
builder = ClassBuilder()
arguments = sys.argv

i = 0

while i < len(arguments):
    argument = arguments[i]
    
    if argument == "-i":
        i = i + 1
        jsonDir = arguments[i]
    elif argument == "-o":
        i = i + 1
        javaDir = arguments[i]
    
    i = i + 1 

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