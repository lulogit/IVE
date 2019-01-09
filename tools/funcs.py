function_list = {"remove": (0,True, lambda x: x),
        "replace_tag": (1, True, lambda x: x),
        "replace": (2, True, lambda x,y: x),
        "before": (1, True, lambda x,y: x),
        "simplify": (0, True, lambda x: x)}.keys()

for f in function_list:
    print("""
@export
def %s(**params: [], argument: 'xpath') -> ['node']:
    return []
""" % f)
