# ------------------------------------------------------------
#   Compiler project fall 2019 - Phase1 : lexical Analyzer
#
#   Parsa Farin nia, Seyyed Amirali Sajjadi
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.
tokens = (
    'TOKEN_ID',
    'TOKEN_INTEGER',
    ''
)

# Regular expression rules for tokens
t_TOKEN_ID = r'_([A-Za-z0-9]_)*([A-Za-z0-9]{2})*|[A-Za-z]([A-Za-z0-9]{2})*((_[A-Za-z0-9])*|([A-Za-z0-9]_)*)([A-Za-z0-9]{2})*'

# Regular expression rules for trivial tokens
t_TOKEN_CLASS = r'class'
t_TOKEN_REFERENCE = r'reference'
t_TOKEN_STATIC = r'static'
t_TOKEN_INT_TYPE = r'int'
t_TOKEN_REAL_TYPE = r'real'
t_TOKEN_BOOL_TYPE = r'bool'
t_TOKEN_STRING_TYPE = r'string'
t_TOKEN_VOID = r'void'
t_TOKEN_TRUE = r'true'
t_TOKEN_FALSE = r'false'
t_TOKEN_PRINT = r'print'
t_TOKEN_RETURN = r'return'
t_TOKEN_BREAK = r'break'
t_TOKEN_CONTINUE = 'continue'
t_TOKEN_IF = r'if'
t_TOKEN_ELSE = r'else'
t_TOKEN_ELSEIF = r'elseif'
t_TOKEN_WHILE = r'while'
t_TOKEN_FOR = r'for'
t_TOKEN_TO = r'to'
t_TOKEN_IN = r'in'
t_TOKEN_STEPS = r'steps'
t_TOKEN_BITWISE_AND = r'&'
t_TOKEN_AND = r'&&'
# TODO: Part2 trivial regexes come here!

# More complex tokens are defined here
def t_TOKEN_INTEGER(t):
    r'[\+-]?(0(x[1-9A-F]([0-9A-F])*|b1[01]*)?|[1-9]([0-9])*|0x|0b)'

    sign = 1
    string_value = t.value
    if '-' in string_value:
        sign = -1
        string_value = string_value[1:]
    elif '+' in string_value:
        string_value = string_value[1:]
    t.value = sign * int(string_value, 0)
    return t
#TODO: Comment token regex rule function comes here!
# NOTE that it mustn't have any return statement in it.

# TODO: Real_number,String functions definitions come here
# Note that real number function must parse it's raw value (like '12.65') to it's actual value(a real number) (ex: real number token string value = '12.42' and t.value must be set to 12.42)
# Note that string function must parse it's raw value to get its actual value and put it at t.value.
# string parsing examples:
#   string value                 value required to put in t.value
#   '"hello"'         ->                'hello'
#   '"hello\\n \\r"'  ->                'hello\n \r'
#   'this '+' is '+' a '+ ' test!' ->   'this is a test!'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (White spaces except for new line (new line is dealt with above))
t_ignore = ' \t\r'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
        _A_mirali 0b1101
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
