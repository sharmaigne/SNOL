"""
SNOL (Simple Number-Only Language) GRAMMAR:
command: assign | expression | input | print
assign := "VARIABLE" "ASSIGN" expression
expression := term { ("PLUS" | "MINUS") term }
term := factor { ("MULTIPLY" | "DIVIDE" | "MODULO") factor }
factor := INTEGER | "FLOAT" | "LPAREN" expression "RPAREN" | "VARIABLE"

print := PRINT expression
input := BEG "VARIABLE"
"""


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
            self.prompt = f"Please enter a value for {variable}:"
        else:
            self.prompt = prompt


class PrintNode:
    def __init__(self, value):
        self.value = value


class Parser:
    def __init__(self):
        self.tokens = []
        self.current_token = None
        self.index = 0

    def __eat(self, token_type):
        # print(f"Current token: {self.current_token}")
        if self.current_token.type == "EOF":
            return

        if self.current_token.type == token_type:
            # print(
            #     f"Eating {self.current_token}, next token is {self.tokens[self.index + 1]}"
            # )
            self.index += 1
            self.current_token = self.tokens[self.index]

        else:
            raise Exception(
                f"Expected token type {token_type}, but got {self.current_token.type}"
            )

    def parse(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index] if self.tokens else None
        return self.command()

    def command(self):
        if self.current_token.type == "VARIABLE":
            return self.assign()
        if self.current_token.type == "KEYWORD":
            if self.current_token.value == "PRINT":
                return self.print_()
            if self.current_token.value == "BEG":
                return self.input()
        else:
            return self.expression()

    def assign(self):
        variable = self.current_token.value
        self.__eat("VARIABLE")
        self.__eat("ASSIGN")
        value = self.expression()
        return AssignmentNode(variable, value)

    def print_(self):
        self.__eat("PRINT")
        value = self.expression()
        return PrintNode(value)

    def input(self):
        self.__eat("BEG")
        variable = self.current_token.value
        self.__eat("VARIABLE")
        return InputNode(variable)

    def expression(self):
        node = self.term()
        while self.current_token.type in ("PLUS", "MINUS"):
            op = self.current_token.value
            self.__eat(self.current_token.type)
            node = BinaryOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in ("MULTIPLY", "DIVIDE"):
            op = self.current_token.value
            self.__eat(self.current_token.type)
            node = BinaryOpNode(node, op, self.factor())
        return node

    def factor(self):
        if self.current_token.type == "INTEGER":
            node = IntegerNode(self.current_token.value)
            self.__eat("INTEGER")
            return node
        if self.current_token.type == "FLOAT":
            node = FloatNode(self.current_token.value)
            self.__eat("FLOAT")
            return node
        if self.current_token.type == "LPAREN":
            self.__eat("LPAREN")
            node = self.expression()
            self.__eat("RPAREN")
            return node
        if self.current_token.type == "MINUS":
            self.__eat("MINUS")
            node = UnaryOpNode("-", self.factor())
            return node
        if self.current_token.type == "VARIABLE":
            node = VariableAccessNode(self.current_token.value)
            self.__eat("VARIABLE")
            return node
        raise Exception(f"Unexpected token type: {self.current_token.type}")
