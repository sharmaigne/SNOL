import re


class Token:
    """A class to represent a token. A token has a type and a value.

    The type is a string that represents the type of the token, such as 'NUMBER' or 'ADD'.

    The value is the actual value of the token, such as 2 or 'ADD'."""

    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

    def __repr__(self):
        return self.__str__()


class Lexer:
    """A class to represent a lexer.

    A lexer takes a line of code and tokenizes it."""

    def __init__(self):
        self.tokens = []

    def __make_token(self, value):
        """Create a token with the given value."""

        # token types
        # "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LPAREN", "RPAREN", "ASSIGN"
        # "INTEGER", "FLOAT", "VARIABLE"

        # operators
        operators = {
            "+": "PLUS",
            "-": "MINUS",
            "*": "MULTIPLY",
            "/": "DIVIDE",
            "(": "LPAREN",
            ")": "RPAREN",
            "=": "ASSIGN",
        }

        # check if the value is an OPERATOR
        if value in operators:
            return Token(operators[value])

        # check if the value is an INTEGER or a FLOAT
        if re.match(r"^\d+$", value):
            return Token("INTEGER", int(value))
        if re.match(r"^\d+\.(\d*)?$", value):
            return Token("FLOAT", float(value))

        # check if the value is a VARIABLE
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", value):
            return Token("VARIABLE", value)

    def tokenize(self, line):
        # This function will take a line of code and return a list of tokens
        # The tokens will be in the form of a list of tuples (type, value)
        # For example, the code "1+4.5" will return [("INTEGER", 1), ("PLUS", None), ("FLOAT", 4.5)]
        # The token types will be 'ADD', 'NUMBER', 'STRING', 'VARIABLE', 'ASSIGN', 'LPAREN', 'RPAREN', 'COMMA', 'SEMI', 'EOF'
        # The token values will be the actual values of the tokens
        # You will need to use regular expressions

        # split the line into tokens by spaces eg "1 + 4" -> ["1", "+", "4"]
        self.tokens = line.split()

        # TODO: split even further to catch the ones not separated by spaces "BEG1.5+40" -> ["BEG", "1.5", "+", "40"]

        # iterate through the tokens and determine their type
        self.tokens = [self.__make_token(value) for value in self.tokens]

        return self.tokens
