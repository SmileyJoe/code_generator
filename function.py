# -*- coding: utf-8 -*-
from constant import *
from os import listdir
from os.path import isfile, join
from pprint import pprint
import os


def uppercaseFirst(name):
    uppercase = ""
    first = True
    for letter in name:
        if first:
            uppercase += letter.capitalize()
            first = False
        else:
            uppercase += letter
    return uppercase


def toCamelCase(name):
    camelName = ""
    first = True
    data = name.split('_')
    for item in data:
        if first:
            camelName += item
            first = False
        else:
            camelName += uppercaseFirst(item)
    return camelName
    
def getFiles(dir, extension):
    items = listdir(dir)
    files = []
    
    for item in items:
        print item
        if isfile(dir + "/" + item):
            tempExtension = os.path.splitext(item)[1][1:]
            if tempExtension == extension:
                files.append(item)
                
    return files