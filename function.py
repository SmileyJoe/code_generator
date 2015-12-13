# -*- coding: utf-8 -*-
from constant import *


def variable(varType, name):
    varName = globalName(name)
    return templateVariable.format(varType=varType, varName=varName)


def constantName(varName):
    varName = varName.upper()
    return templateConstantName.format(varName=varName)


def tagConstant(jsonKey):
    varName = constantName(jsonKey)
    return templateConstant.format(varName=varName, varValue=jsonKey)


def setter(varType, name):
    funcName = uppercaseFirst(name)
    varName = globalName(name)
    localVarName = name
    return templateSetter.format(
        varType=varType, varName=varName, funcName=funcName,
        localVarName=localVarName)


def getter(varType, name):
    funcName = uppercaseFirst(name)
    varName = globalName(name)
    return templateGetter.format(
        varType=varType, varName=varName, funcName=funcName)


def fromApi(varType, contents):
    return templateFromApi.format(varType=varType, contents=contents)


def globalName(name):
    varName = uppercaseFirst(name)
    return tamplateGlobalName.format(varName=varName)


def fromApiItem(varType, varTypeClass, jsonKey):
    funcName = uppercaseFirst(toCamelCase(jsonKey))
    tagName = constantName(jsonKey)
    varTypeClass = uppercaseFirst(varTypeClass)

    if varTypeClass:
        return templateFromJsonObject.format(
            varType=varType, funcName=funcName, tagName=tagName,
            varTypeClass=varTypeClass)
    else:
        varTypeClass = uppercaseFirst(varType)
        return templateFromJson.format(
            varTypeClass=varTypeClass, funcName=funcName, tagName=tagName)


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