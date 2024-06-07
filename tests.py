import unittest
from unittest import mock
from lexer.lexer import Lexer
from lexer.token import Token
from parser.parser import Parser
from parser.parser import AssignmentNode, BinaryOpNode, IntegerNode, FloatNode, VariableAccessNode, InputNode, PrintNode
from evaluator.evaluator import Evaluator

class TestLexer(unittest.TestCase):

    def test_expressions(self):
        lexer = Lexer()
        code = '3 + 4 * 10'
        tokens = lexer.tokenize(code)
        expected_tokens = [
            Token('INTEGER', 3),
            Token('PRED_5', '+'),
            Token('INTEGER', 4),
            Token('PRED_6', '*'),
            Token('INTEGER', 10),
            Token('EOF', None)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_space_separation(self):
        lexer = Lexer()
        code = '   42    +    23   '
        tokens = lexer.tokenize(code)
        expected_tokens = [
            Token('INTEGER', 42),
            Token('PRED_5', '+'),
            Token('INTEGER', 23),
            Token('EOF', None)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_variables(self):
        lexer = Lexer()
        code = 'x = 5'
        tokens = lexer.tokenize(code)
        expected_tokens = [
            Token('VARIABLE', 'x'),
            Token('ASSIGN', '='),
            Token('INTEGER', 5),
            Token('EOF', None)
        ]
        self.assertEqual(tokens, expected_tokens)

    def test_parentheses(self):
        lexer = Lexer()
        code = '(a + b) * c'
        tokens = lexer.tokenize(code)
        expected_tokens = [
            Token('LPAREN', '('),
            Token('VARIABLE', 'a'),
            Token('PRED_5', '+'),
            Token('VARIABLE', 'b'),
            Token('RPAREN', ')'),
            Token('PRED_6', '*'),
            Token('VARIABLE', 'c'),
            Token('EOF', None)
        ]
        self.assertEqual(tokens, expected_tokens)

class TestParser(unittest.TestCase):

    def test_assign(self):
        parser = Parser()
        tokens = [
            Token('VARIABLE', 'x'),
            Token('ASSIGN', '='),
            Token('INTEGER', 5),
            Token('EOF', None)
        ]
        ast = parser.parse(tokens)
        expected_ast = AssignmentNode('x', IntegerNode(5))
        self.assertEqual(ast.variable, expected_ast.variable)
        self.assertEqual(ast.value.value, expected_ast.value.value)

    def test_expression(self):
        parser = Parser()
        tokens = [
            Token('INTEGER', 3),
            Token('PRED_5', '+'),
            Token('INTEGER', 4),
            Token('PRED_6', '*'),
            Token('INTEGER', 10),
            Token('EOF', None)
        ]
        ast = parser.parse(tokens)
        expected_ast = BinaryOpNode(IntegerNode(3), '+', BinaryOpNode(IntegerNode(4), '*', IntegerNode(10)))
        self.assertEqual(ast.left.value, expected_ast.left.value)
        self.assertEqual(ast.op, expected_ast.op)
        self.assertEqual(ast.right.left.value, expected_ast.right.left.value)
        self.assertEqual(ast.right.op, expected_ast.right.op)
        self.assertEqual(ast.right.right.value, expected_ast.right.right.value)

    def test_float_expression(self):
        parser = Parser()
        tokens = [
            Token('FLOAT', 3.5),
            Token('PRED_5', '+'),
            Token('FLOAT', 4.2),
            Token('EOF', None)
        ]
        ast = parser.parse(tokens)
        expected_ast = BinaryOpNode(FloatNode(3.5), '+', FloatNode(4.2))
        self.assertEqual(ast.left.value, expected_ast.left.value)
        self.assertEqual(ast.op, expected_ast.op)
        self.assertEqual(ast.right.value, expected_ast.right.value)

class TestEvaluator(unittest.TestCase):

    def test_evaluate_assignment(self):
        evaluator = Evaluator()
        node = AssignmentNode('x', IntegerNode(42))
        self.assertEqual(evaluator.evaluate(node), 42)

    def test_evaluate_variable_access(self):
        evaluator = Evaluator()
        evaluator.environment['x'] = 42
        node = VariableAccessNode('x')
        self.assertEqual(evaluator.evaluate(node), 42)

    def test_evaluate_input(self):
        evaluator = Evaluator()
        node = InputNode('x', 'Enter a number: ')
        with mock.patch('builtins.input', return_value='42'):
            self.assertEqual(evaluator.evaluate(node), 42)

    def test_evaluate_print(self):
        evaluator = Evaluator()
        node = PrintNode(IntegerNode(42))
        with mock.patch('builtins.print') as mocked_print:
            evaluator.evaluate(node)
            mocked_print.assert_called_with('SNOL :> 42')

class TestIntegration(unittest.TestCase):

    def test_lexer_parser_evaluator(self):
        lexer = Lexer()
        parser = Parser()
        evaluator = Evaluator()

        code = 'x = 5 + 3 * 2'
        tokens = lexer.tokenize(code)
        ast = parser.parse(tokens)
        result = evaluator.evaluate(ast)
        self.assertEqual(result, 11)
        self.assertEqual(evaluator.environment['x'], 11)

    def test_lexer_parser_evaluator_with_floats(self):
        lexer = Lexer()
        parser = Parser()
        evaluator = Evaluator()

        code = 'y = 3.5 + 4.2'
        tokens = lexer.tokenize(code)
        ast = parser.parse(tokens)
        result = evaluator.evaluate(ast)
        self.assertEqual(result, 7.7)
        self.assertEqual(evaluator.environment['y'], 7.7)

if __name__ == "__main__":
    unittest.main()
