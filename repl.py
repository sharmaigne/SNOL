from lexer.lexer import Lexer
from parser.parser import Parser
from evaluator.evaluator import Evaluator

# readline is a library that allows us to use the arrow keys to navigate through the command history
# if readline is not available (non unix systems), we create a dummy class to avoid errors
try:
    import readline

except ImportError:
    print(
        "Note: Readline is not available on this system, command history will not be available."
    )

    class Readline:
        @staticmethod
        def set_completer(*args, **kwargs):
            pass

        @staticmethod
        def parse_and_bind(*args, **kwargs):
            pass
    readline = Readline()

def main():
    lexer = Lexer()
    parser = Parser()
    evaluator = Evaluator()

    print(
        "The SNOL environment is now active, you may proceed with giving your commands."
    )
    while True:
        try:
            line = input("\nCommand: ")
            # if we have time, should add "did you mean" feature
            if line.strip() == "EXIT!":
                break
            if line.strip() == "":
                continue

            tokens = lexer.tokenize(line)
            ast = parser.parse(tokens)
            result = evaluator.evaluate(ast)

            # uncomment out to make a REPL
            # print(f"SNOL :> {result}")

        except Exception as e:
            print(f"SNOL :> {e}")

    print("Evaluator is now terminated...")


if __name__ == "__main__":
    main()
