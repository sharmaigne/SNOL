from lexer.lexer import Lexer
# from parser.parser import Parser
# from interpreter.interpreter import Interpreter


def main():
    lexer = Lexer()
    # parser = Parser()
    # interpreter = Interpreter()

    print(
        "The SNOL environment is now active, you may proceed with giving your commands."
    )
    while True:
        try:
            line = input("SNOL> ")
            # if we have time, should add "did you mean" feature
            if line.strip() == "EXIT!":
                break

            # tokens = lexer.tokenize(line)
            # ast = parser.parse(tokens)
            # result = interpreter.interpret(ast)

            result = lexer.tokenize(line)

            print(result)
        except Exception as e:
            print(e)
    print("Interpreter is now terminated...")


if __name__ == "__main__":
    main()
