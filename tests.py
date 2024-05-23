from lexer.lexer import Lexer
from lexer.token import Token


def test_lexer():
    """
    Unit tests for the lexer.

    Each test calls lexer.tokenize()
    input: a string
    output: a list of tokens
    """
    lexer = Lexer()

    # test expressions

    # test space separation

    # test variables

    # test ...


def test_parser():
    """
    Unit tests for the parser.

    Each test calls parser.parse()
    input: a list of tokens
    output: an AST
    """
    pass


def test_evaluator():
    """
    Unit tests for the evaluator.

    Each test calls evaluator.evaluate()
    input: an AST
    output: a value
    """
    pass


def test_integration():
    """
    Integration tests for the lexer, parser, and evaluator.

    Each test calls lexer.tokenize(), parser.parse(), and evaluator.evaluate()
    input: a string
    output: a value
    """
    pass


if __name__ == "__main__":
    test_lexer()
    test_parser()
    test_evaluator()
    test_integration()
