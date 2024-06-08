import re


class Evaluator:
    """Evaluates the abstract syntax tree generated by the parser."""

    def __init__(self):
        self.environment = {}  # stores variables

    def evaluate(self, node):
        method_name = f"evaluate_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_evaluate)
        return method(node)

    def generic_evaluate(self, node):
        raise Exception(f"No evaluation method defined for {type(node).__name__}")

    ### EVALUATE DATA TYPES ###
    def evaluate_IntegerNode(self, node):
        return node.value

    def evaluate_FloatNode(self, node):
        return node.value

    ### VARIABLES ###
    def evaluate_VariableAccessNode(self, node):
        if node.variable not in self.environment:
            raise Exception(f"Error! [{node.variable}] is not defined!")
        return self.environment[node.variable]

    def evaluate_AssignmentNode(self, node):
        value = self.evaluate(node.value)
        self.environment[node.variable] = value
        return value

    ### OPERATIONS ###
    def evaluate_BinaryOpNode(self, node):
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)

        true = type(left)(1)
        false = type(left)(0)

        if type(left) != type(right):
            raise Exception(
                "Error! Operands must be of the same type in an arithmetic operation!"
            )

        # ALGEBRAIC OPERATORS

        match node.op:
            case "+":
              return left + right
            case "-":
                return left - right
            case "*":
                return left * right
            case "/":
                # integer division since python defaults to float division
                if type(left) == int and type(right) == int:
                    return left // right
                return left / right
            case "%":
                return left % right
            case "**":
                return left**right
            case "==":
                return true if left == right else false
            case "!=":
                return true if left != right else false
            case "<=":
                return true if left <= right else false
            case ">=":
                return true if left >= right else false
            case "<":
                return true if left < right else false
            case ">":
                return true if left > right else false
            case "&&":
                return true if left and right else false
            case "||":
                return true if left or right else false
            case _:
                raise Exception(f"Invalid binary operator: {node.op}")

        # //, **, <, >, <=, >=, ==, !=, ||, &&

    def evaluate_UnaryOpNode(self, node):
        number = self.evaluate(node.node)

        match node.op:
            case "-":
                return -number
            case "!":
                return type(number)(1) if number == 0 else type(number)(0)
            case _:
                raise Exception(f"Invalid unary operator: {node.op}")

    ### INPUT/OUTPUT ###
    def evaluate_InputNode(self, node):
        value = input(node.prompt)

        if re.match(r"^-?\d+$", value):
            value = int(value)
        elif re.match(r"^-?\d+\.(\d*)?$", value):
            value = float(value)
        else:
            raise Exception(f"ERROR: Invalid input {value}")

        self.environment[node.variable] = value
        return value

    def evaluate_PrintNode(self, node):
        value = self.evaluate(node.value)
        if node.variable:
            print(f"SNOL :> [{node.variable}] = {value}")
        else:
            print(f"SNOL :> {value}")
        return value