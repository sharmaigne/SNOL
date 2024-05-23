class Evaluator:
    def __init__(self):
        self.environment = {}

    def evaluate(self, node):
        method_name = f"evaluate_{type(node).__name__}"
        method = getattr(self, method_name, self.generic_evaluate)
        return method(node)

    def generic_evaluate(self, node):
        raise Exception(f"No evaluation method defined for {type(node).__name__}")

    def evaluate_IntegerNode(self, node):
        return node.value

    def evaluate_FloatNode(self, node):
        return node.value

    def evaluate_VariableAccessNode(self, node):
        if node.variable not in self.environment:
            raise Exception(f"Error: undefined word: {node.variable}")
        return self.environment[node.variable]

    def evaluate_BinaryOpNode(self, node):
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)

        if type(left) != type(right):
            raise Exception("ERROR: Incompatible types")

        return {
            "+": left + right,
            "-": left - right,
            "*": left * right,
            "/": left / right,
            "%": left % right,
        }.get(node.op, Exception(f"Invalid binary operator: {node.op}"))

    def evaluate_UnaryOpNode(self, node):
        number = self.evaluate(node.node)

        if node.op == "-":
            return -number

        raise Exception(f"Invalid unary operator: {node.op}")

    def evaluate_AssignmentNode(self, node):
        value = self.evaluate(node.value)
        self.environment[node.variable] = value
        return value

    def evaluate_InputNode(self, node):
        value = input(node.prompt)
        self.environment[node.variable] = value
        return value

    def evaluate_PrintNode(self, node):
        value = self.evaluate(node.value)
        print(value)
        return value
