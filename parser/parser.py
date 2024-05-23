from lexer.token import Token

"""
SNOL (Simple Number-Only Language) GRAMMAR:
command: assign | expression | input | print
assign := VARIABLE ASSIGN expression
expression := term { (PLUS | MINUS) term }
term := factor { (MULTIPLY | DIVIDE | MODULO) factor }
factor := INTEGER | FLOAT | LPAREN expression RPAREN | VARIABLE

print := PRINT expression
input := BEG VARIABLE
"""

class Parser:
    """Recursive descent parser for the SNOL language."""
    def __init__(self):
        self.tokens = []

    def parse(self, tokens: Token):
        """Returns an AST for one line of code."""
        self.tokens = tokens
        
