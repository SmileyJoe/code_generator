from constant import *
from template import Template
from function import *

class ClassBuilder:

    __items = ""
    __className = ""
    
    
    def setClassName(self, className):
        self.__className = className


    def getClassName(self):
        return self.__className

    
    def setItems(self, items):
        self.__items = items
    

    def variable(self, varType, name):
        varName = self.globalName(name)
        return Template.variable.format(varType=varType, varName=varName)


    def constantName(self, varName):
        varName = varName.upper()
        return Template.constantName.format(varName=varName)


    def tagConstant(self, jsonKey):
        varName = self.constantName(jsonKey)
        return Template.constant.format(varName=varName, varValue=jsonKey)


    def setter(self, varType, name):
        funcName = uppercaseFirst(name)
        varName = self.globalName(name)
        localVarName = name
        return Template.setter.format(
            varType=varType, varName=varName, funcName=funcName,
            localVarName=localVarName)


    def getter(self, varType, name):
        funcName = uppercaseFirst(name)
        varName = self.globalName(name)
        return Template.getter.format(
            varType=varType, varName=varName, funcName=funcName)
            
    def fromApi(self, varType, contents):
        return Template.fromApi.format(varType=varType, contents=contents)


    def toString(self, className, contents):
        return Template.toString.format(className=className, contents=contents)


    def globalName(self, name):
        varName = uppercaseFirst(name)
        return Template.globalName.format(varName=varName)


    def fromApiItem(self, varType, varTypeClass, jsonKey):
        funcName = uppercaseFirst(toCamelCase(jsonKey))
        tagName = self.constantName(jsonKey)
        varTypeClass = uppercaseFirst(varTypeClass)

        if varTypeClass:
            return Template.fromJsonObject.format(
                varType=varType, funcName=funcName, tagName=tagName,
                varTypeClass=varTypeClass)
        else:
            varTypeClass = uppercaseFirst(varType)
            return Template.fromJson.format(
                varTypeClass=varTypeClass, funcName=funcName, tagName=tagName)
                
    def toStringItem(self, name):
        varName = self.globalName(name)
        return Template.toStringItem.format(varName=varName)
        
      
    def build(self):
        contents = "public class " + self.__className + "(){" + newline
        variables = ""
        getters = ""
        setters = ""
        constants = ""
        fromApiItems = ""
        toStringItems = ""

        for key, value in self.__items.iteritems():
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

            fromApiItems += self.fromApiItem(varTypeArray, varTypeClass, key)
            toStringItems += self.toStringItem(key)
            constants += self.tagConstant(key)
            key = toCamelCase(key)
            variables += self.variable(varType, key)
            setters += self.setter(varType, key)
            getters += self.getter(varType, key)

        contents += newline + constants + newline + \
        variables + newline + \
        setters + \
        getters + \
        self.toString(self.__className, toStringItems) + "}"
        #fromApi(className, fromApiItems) + "}"
        
        return contents