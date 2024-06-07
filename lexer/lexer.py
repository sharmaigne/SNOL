import re
from lexer.token import Token


class Lexer:
    """A class to represent a lexer.

    A lexer takes a line of code and tokenizes it."""

    def __init__(self):
        self.tokens = []

    def __make_token(self, value):
        """Create a token with the given value."""

        # token types
        # "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN", "ASSIGN"
        # //, **, <, >, <=, >=, ==, !=, ||, &&, and !
        # "INTEGER", "FLOAT", "VARIABLE"
        # "INPUT", "OUTPUT"
        
        operators = {
            "**": "PRED_7",
            "*": "PRED_6",
            "/": "PRED_6",
            "%": "PRED_6",
            "+": "PRED_5",
            "-": "PRED_5",
            "==": "PRED_4",
            "!=": "PRED_4",
            "<=": "PRED_4",
            ">=": "PRED_4",
            "<": "PRED_4",
            ">": "PRED_4",
            "!": "PRED_3",
            "&&": "PRED_2",
            "||": "PRED_1",
            "(": "LPAREN",
            ")": "RPAREN",
            "=": "ASSIGN",
        }

        # reserved words
        reservedWords = {
            "BEG": "INPUT",
            "PRINT": "PRINT",
        }

        # check if the value is an OPERATOR
        if value in operators:
            return Token(operators[value], value)

        # check if the value is a RESERVED WORD
        if value in reservedWords:
            return Token("KEYWORD", reservedWords[value])

        # check if the value is an INTEGER or a FLOAT
        # follows the EBNF rules:
        # INTEGER = [-]digit{digit}
        # FLOAT = [-]digit{digit}.{digit}
        if re.match(r"^-?\d+$", value):
            return Token("INTEGER", int(value))
        if re.match(r"^-?\d+\.(\d*)?$", value):
            return Token("FLOAT", float(value))

        # check if the value is a VARIABLE
        # follows the EBNF rule VARIABLE = letter{(letter|digit)}
        if re.match(r"^[A-Za-z][A-Za-z0-9]*$", value):
            return Token("VARIABLE", value)

        # TODO: test that this works
        # if the value is not any of the above, raise an exception
        raise Exception(f"ERROR: Unrecognized token {value}")

    def tokenize(self, line):
        # This function will take a line of code and return a list of tokens
        # The tokens will be in the form of a list of tuples (type, value)
        # For example, the code "1+4.5" will return [("INTEGER", 1), ("PLUS", None), ("FLOAT", 4.5)]
        # The token types will be 'ADD', 'NUMBER', 'STRING', 'VARIABLE', 'ASSIGN', 'LPAREN', 'RPAREN', 'COMMA', 'SEMI', 'EOF'
        # The token values will be the actual values of the tokens

        # split the line into tokens by spaces eg "SUM=1.45+4" -> ["SUM", "=", "1.45", "+", "4"]
        # \d+\.?\d* matches all numbers
        # [^_\W]+ matches words, does not count words starting with numbers
        # \|\||&&|\/|\*\*|<=?|>=?|==|!= matches double sign operators
        # [+\-*/%() =!><] matches single sign operators
        # \S+? matches all items, used to catch unrecognized tokens
        self.tokens = re.findall(r"\d+\.?\d*|[^_\W]+|\|\||&&|\/|\*\*|<=?|>=?|==|!=|[+\-*/%()=!><]|\S+?", line)
        print(self.tokens)
        
        # iterate through the tokens and determine their type
        self.tokens = [self.__make_token(value) for value in self.tokens] + [
            Token("EOF")
        ]

        return self.tokens
