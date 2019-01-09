import re

index = {}

def export(f):
	index[f.__name__] = f.__annotations__
	return f

@export
def domain(argument: re.compile) -> bool:
	return False

@export
def exists(argument: "xpath") -> bool:
	return False

def check_name(condition):
    'Checks if a certain condition name is valid'
    return condition in index
