import sys
from lex import tokens



# helpers
def halt(error_msg, line=None, code=1):
    if line:
        print("[at line %d]" % line, error_msg) #, file=sys.stderr)
    else:
        print(error_msg) #, file=sys.stderr)
    print("Aborting ...")
    sys.exit(code)

# supported conditions
conditions = {
        "exists": (0,True, lambda x: False),
        "domain": (0,True, lambda x: False)
}

# supported functions
functions = {
        "remove": (0,True, lambda x: x),
        "replace_tag": (1, True, lambda x: x),
        "replace": (2, True, lambda x,y: x),
        "before": (1, True, lambda x,y: x),
        "simplify": (0, True, lambda x: x)} 

# handle memory
variables = {}
properties = {p: None for p in "title,body,cover".split(',')}

def p_template0(t):
	'''template	: blocks'''
	print("template_0")


def p_blocks1(t):
	'''blocks		: blocks block
		| block'''
	print("blocks_1")


def p_block2(t):
	'''block		: conditions statements'''
	print("block_2")


def p_conditions3(t):
	'''conditions	: conditions condition
	   	| empty'''
	print("conditions_3")


def p_statements4(t):
	'''statements 	: statements statement
	  	| statement'''
	print("statements_4")


def p_empty5(t):
	'''empty 		: '''
	print("empty_5")


def p_condition6(t):
	'''condition 	: QUERY ID COLON XPATH
	 	| QUERY ID COLON STRING
		| QUERY ID'''
	print("condition_6")


def p_condition7(t):
	'''condition 	: BANG ID COLON XPATH
	 	| BANG ID COLON STRING
		| BANG ID'''
	print("condition_7")


def p_statement8(t):
	'''statement 	: assign_var
	   	| assign_prop
		| func_call
		| tag_replace'''
	print("statement_8")


def p_assign_var9(t):
	'''assign_var	: DOLLAR ID BANG BANG COLON expr
	   	| DOLLAR ID BANG COLON expr
	   	| DOLLAR ID COLON expr
		| DOLLAR ID BANG BANG
	   	| DOLLAR ID BANG
		| DOLLAR ID'''
	print("assign_var_9")


def p_assign_prop10(t):
	'''assign_prop	: ID BANG BANG COLON expr
                | ID BANG COLON expr
                | ID COLON expr
				| ID BANG BANG
                | ID BANG
                | ID'''
	print("assign_prop_10")


def p_func_call11(t):
	'''func_call	: AT ID LPAR params RPAR COLON expr
	 	| AT ID LPAR params RPAR
		| AT ID COLON expr
		| AT ID'''
	print("func_call_11")


def p_params12(t):
	'''params		: param COMMA param
		| param param
		| param'''
	print("params_12")


def p_param13(t):
	'''param		: TAG
		| STRING'''
	print("param_13")


def p_tag_replace14(t):
	'''tag_replace	: TAG COLON expr'''
	print("tag_replace_14")


def p_xpath15(t):
	'''xpath 		: variable XPATH
       		| XPATH'''
	print("xpath_15")


def p_expr16(t):
	'''expr	: xpath
		| variable
   		| STRING
		| NULL'''
	print("expr_16")


def p_variable17(t):
	'''variable 	: DOLLAR DOLLAR
    		| DOLLAR AT
    		| DOLLAR ID'''
	print("variable_17")

def p_error(t):
    halt("Invalid syntax", line=t.lexer.lineno)

import ply.yacc as yacc
parser = yacc.yacc(start="template")
