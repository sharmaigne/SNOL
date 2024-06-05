"""
SNOL (Simple Number-Only Language) GRAMMAR:
command: (assign | expression | input | print) END
assign := VARIABLE ASSIGN expression
expression := term { (PLUS | MINUS) term }
term := factor { (MULTIPLY | DIVIDE | MODULO) factor }
factor := INTEGER | FLOAT | LPAREN expression RPAREN | VARIABLE

print := PRINT (expression)
input := BEG VARIABLE
"""

from lexer.token import Token

### NODES ###


class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value
        self.type = type(value)


class VariableAccessNode:
    def __init__(self, variable):
        self.variable = variable


class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class UnaryOpNode:
    def __init__(self, op, node):
        self.op = op
        self.node = node


class IntegerNode:
    def __init__(self, value):
        self.value = value


class FloatNode:
    def __init__(self, value):
        self.value = value


class InputNode:
    def __init__(self, variable, prompt=None):
        self.variable = variable
        if prompt is None:
            self.prompt = f"SNOL :> Please enter a value for [{variable}]\nInput: "
        else:
            self.prompt = prompt


class PrintNode:
    def __init__(self, value, variable=None):
        self.variable = variable
        self.value = value


### ----------------- ###


class Parser:
    """Recursive descent parser"""

    def __init__(self):
        self.tokens = []
        self.current_token: Token = Token("", "")
        self.index = 0

    def __eat(self, token_type):    
        if self.current_token.type == "EOF":
            return
        
        if self.current_token.type == token_type:
            self.index += 1
            self.current_token = self.tokens[self.index]

        else:
            raise Exception(
                f"Expected token type {token_type}, but got {self.current_token.type}"
            )

    def parse(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index] if self.tokens else Token("EOF", "")
        return self.command()

    def command(self):
        line_ast = None
        if self.tokens[self.index + 1].type == "ASSIGN":  # example: x = 43.4 + 2
            line_ast = self.assign()

        elif self.current_token.type == "KEYWORD":
            if self.current_token.value == "INPUT":
                line_ast = self.input()
            elif self.current_token.value == "PRINT":
                line_ast = self.print_()

        else:
            line_ast = (
                self.expression()
            )  # catches both variable and number first eg x + 4. 4 + 2

        if self.current_token.type == "EOF":
            return line_ast

        raise Exception(
            "Unknown command! Does not match any valid command on this language."
        )

    def assign(self):
        variable = self.current_token.value
        self.__eat("VARIABLE")
        self.__eat("ASSIGN")
        value = self.expression()
        return AssignmentNode(variable, value)

    def input(self):
        self.__eat("KEYWORD")
        variable = self.current_token.value
        self.__eat("VARIABLE")

        return InputNode(variable)

    def print_(self):
        self.__eat("KEYWORD")
        value = self.expression()

        return PrintNode(value)

    def expression(self):
        node = self.term()
        while self.current_token.type in ("PLUS", "MINUS"):
            op = self.current_token.value
            self.__eat(self.current_token.type)
            node = BinaryOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in ("MULTIPLY", "DIVIDE", "MODULO"):
            op = self.current_token.value
            self.__eat(self.current_token.type)
            node = BinaryOpNode(node, op, self.factor())
        return node

    def factor(self):
        node = None

        if self.current_token.type == "INTEGER":
            node = IntegerNode(self.current_token.value)
            self.__eat("INTEGER")
        elif self.current_token.type == "FLOAT":
            node = FloatNode(self.current_token.value)
            self.__eat("FLOAT")
        elif self.current_token.type == "LPAREN":
            self.__eat("LPAREN")
            node = self.expression()
            self.__eat("RPAREN")
        elif self.current_token.type == "MINUS":
            self.__eat("MINUS")
            node = UnaryOpNode("-", self.factor())
        elif self.current_token.type == "VARIABLE":
            node = VariableAccessNode(self.current_token.value)
            self.__eat("VARIABLE")
        if node:
            return node
