from lexer.lexer import Lexer
from parser.parser import Parser

# from evaluator.evaluator import Evaluator


def main():
    lexer = Lexer()
    parser = Parser()
    # evaluator = Evaluator()

    print(
        "The SNOL environment is now active, you may proceed with giving your commands."
    )
    while True:
        try:
            line = input("SNOL> ")
            # if we have time, should add "did you mean" feature
            if line.strip() == "EXIT!":
                break

            tokens = lexer.tokenize(line)
            ast = parser.parse(tokens)
            # result = evaluator.evaluate(ast)

            result = ast

            # print(result)

        except Exception as e:
            print(e)

    print("Evaluator is now terminated...")


if __name__ == "__main__":
    main()
