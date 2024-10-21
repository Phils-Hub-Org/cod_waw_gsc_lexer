myDict = {
    "/": {
        "/": "SL_COMMENT",
        "*": "ML_COMMENT",
        "#": "DEV_COMMENT",
    },
    "\n": "NEWLINE",
    "#": {
        "include": "INCLUDE_DIRECTIVE",
        "animtree": "ANIMTREE_DIRECTIVE",
        "using_animtree": "USING_ANIMTREE_DIRECTIVE",
    },
    "\\": "ESCAPE_CHAR",
}

"""
"/": {
    "/": "SL_COMMENT",
    "*": "ML_COMMENT",
    "#": "DEV_COMMENT",
    "DIV": None,
},
"""

def getTokenDict():
    return {}

def getPosition():
    return 0

def incrementPosition():
    pass

def tokenize(code: str, tokenDict: dict=getTokenDict()) -> list:
    tokens = []
    for char in code:
        # /
        result = tokenDict.get(char, None)
        # {
        #     "/": "SL_COMMENT",
        #     "*": "ML_COMMENT",
        #     "#": "DEV_COMMENT",
        #     "DIV": "DIV",
        # }
        if result is not None:
            # true
            if isinstance(result, dict):
                # true
                subDict = result
                # true
                incrementPosition()
                # /
                result = subDict.get(code[getPosition() + 1], None)
                # SL_COMMENT
                if result is not None:
                    tokens.append(('SL_COMMENT', result))
                    # true
                    incrementPosition()
                else: