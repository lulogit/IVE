template	: blocks;
blocks		: blocks block
		| block;
block		: conditions statements;
conditions	: conditions condition
	   	| empty;
statements 	: statements statement
	  	| statement;
empty 		: ;
condition 	: QUERY ID COLON XPATH
	 	| QUERY ID COLON STRING
		| QUERY ID;
condition 	: BANG ID COLON XPATH
	 	| BANG ID COLON STRING
		| BANG ID;
statement 	: assign_var
	   	| assign_prop
		| func_call
		| tag_replace;
assign_var	: DOLLAR ID BANG BANG COLON expr
	   	| DOLLAR ID BANG COLON expr
	   	| DOLLAR ID COLON expr
		| DOLLAR ID BANG BANG
	   	| DOLLAR ID BANG
		| DOLLAR ID;
assign_prop	: ID BANG BANG COLON expr
                | ID BANG COLON expr
                | ID COLON expr
				| ID BANG BANG
                | ID BANG
                | ID;
func_call	: AT ID LPAR params RPAR COLON expr
	 	| AT ID LPAR params RPAR
		| AT ID COLON expr
		| AT ID;
params		: param COMMA param
		| param param
		| param;
param		: TAG
		| STRING;
tag_replace	: TAG COLON expr;
xpath 		: variable XPATH
       		| XPATH;
expr	: xpath
		| variable
   		| STRING
		| NULL;
variable 	: DOLLAR DOLLAR
    		| DOLLAR AT
    		| DOLLAR ID;
