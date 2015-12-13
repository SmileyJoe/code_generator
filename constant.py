# -*- coding: utf-8 -*-


newline = "\n"
tab = "    "
tamplateGlobalName = "m{varName}"
templateConstantName = "TAG_{varName}"
templateVariable = """    private {varType} {varName};
"""
templateGetter = """    public {varType} get{funcName}(){{
        return {varName};
    }}

"""
templateSetter = """    public void set{funcName}({varType} {localVarName}){{
        {varName} = {localVarName};
    }}

"""
templateConstant = ("    public static final String "
                    "{varName} = \"{varValue}\";" + newline)
templateFromApi = """    public static {varType} """ + \
"""fromApi(JSONObject object){{
        {varType} item = new {varType}();
        JsonHelper helper = new JsonHelper(object);

{contents}
        return item;
    }}
"""
templateFromJson = """        item.set{funcName}""" + \
"""(helper.get{varTypeClass}({tagName}));
"""
templateFromJsonObject = """        item.set{funcName}""" + \
"""({varType}.fromApi(helper.get{varTypeClass}({tagName})));
"""