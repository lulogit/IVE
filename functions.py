import re

_index = {}
def export(f):
	_index[f.__name__] = f.__annotations__
	return f

@export
def remove(*params: [], argument: 'xpath') -> ['node']:
    return []

@export
def replace_tag(*params: ["TAG"], argument: 'xpath') -> ['node']:
    return []

@export
def replace(*params: ["regexp", "STRING"], argument: 'xpath') -> ['node']:
    return []

@export
def before(*params: ["TAG"], argument: 'xpath') -> ['node']:
    return []

@export
def simplify(*params: [], argument: 'xpath') -> ['node']:
    return []

def check_name(condition):
    'Checks if a certain function name is valid'
    return condition in _index

