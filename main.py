from termcolor import colored
from src.encoder import Encoder
from src.universal_function import universalFunction


def present():
    print(colored('For following instructions:', 'green'))
    print(open('instructions.txt', "r").read())
    print()
    print(colored('We have this LL(1) grammar:', 'green'))
    print(open('grammar.txt', "r").read())
    print()
    print(colored('Parse table of this grammar is:', 'green'))
    print(open('parse-table.txt', "r").read())


if __name__ == "__main__":
    present()
    # filePath = 'data/in/book-example.txt'
    filePath = 'data/in/test.txt'
    fileString = open(filePath, "r").read()
    print(colored('input file:', 'green'))
    encoder = Encoder(fileString)
    instructions = encoder.encodeLines()
    programCode = encoder.calcuateProgramCode()
    inputValues = encoder.getInputVaules()
    input_for_universal_program = inputValues + [programCode]
    universalFunction(input_for_universal_program, instructions)
