reserved = {
        "null": "NULL"}

tokens = [
    'AT','QUERY','BANG','DOLLAR',
    'LPAR','RPAR','COLON','COMMA', 
    'ID',
    'STRING','XPATH','TAG'
    ]

tokens = tokens + list(reserved.values())

# Tokens
t_ignore_COMMENT = r'\#[^\n]*'

t_AT = r'\@'
t_QUERY = r'\?'
t_BANG = r'\!'
t_COMMA = r'\,'
t_DOLLAR = r'\$'
t_LPAR = r'\('
t_RPAR = r'\)'
t_COLON = r'\:'
t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'

def t_TAG(t):
    r'\<(p|img|b|br|article)\>'
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_XPATH(t):
    r'\/[\/\[\]\(\)a-zA-Z0-9\.\@\=\"\-\'\:\*\;\, \_]+'
    try:
        # validate XPATH or throw error
        pass
    except ValueError:
        print("Invalid XPATH: %s", t.value)
        sys.exit(1)
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()
