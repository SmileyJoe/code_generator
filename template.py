from constant import *

class Template:

    globalName = "m{varName}"
    
    constantName = "TAG_{varName}"
    
    variable = """    private {varType} {varName};
"""

    getter = """    public {varType} get{funcName}(){{
        return {varName};
    }}

"""

    setter = """    public void set{funcName}({varType} {localVarName}){{
        {varName} = {localVarName};
    }}

"""

    constant = ("    public static final String "
                    "{varName} = \"{varValue}\";" + newline)
                    
    fromApi = """    public static {varType} """ + \
"""fromApi(JSONObject object){{
        {varType} item = new {varType}();
        JsonHelper helper = new JsonHelper(object);

{contents}
        return item;
    }}
"""

    fromJson = """        item.set{funcName}""" + \
"""(helper.get{varTypeClass}({tagName}));
"""

    fromJsonObject = """        item.set{funcName}""" + \
"""({varType}.fromApi(helper.get{varTypeClass}({tagName})));
"""

    toString = """    @Override
    public String toString(){{
        return '{className}{{' 
        {contents}      '}}';
    }}
"""

    toStringItem = """          + '{varName} = ' + {varName}""" + newline