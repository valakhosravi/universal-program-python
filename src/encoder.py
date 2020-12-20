from .compiler import Compiler
from .generate_prime_numbers import generatePrimeNumbers
from termcolor import colored


class Encoder(object):
    fileString = ''
    lines = []
    compiler = {}

    def __init__(self, input):
        self.fileString = input
        self.lines = input.splitlines()
        self.compiler = Compiler()

    def encode(self, line):
        code = self.compiler.parse(line)
        return code

    def encodeLines(self):
        codeList = []
        for line in self.lines:
            code = self.encode(line)
            _code = (code[0], (code[1], code[2]))
            codeList.append(_code)
        return codeList

    def fStar(self, x, y):
        return 2 ** x * (2 * y + 1) - 1

    def calcuateProgramCode(self):
        codeList = self.encodeLines()
        number_of_instructions = len(codeList)
        primeNumbersList = generatePrimeNumbers(number_of_instructions)
        instructionCodeList = []
        index = 1
        for code in codeList:
            bc = self.fStar(code[1][0], code[1][1])
            abc = self.fStar(code[0], bc)
            instructionCodeList.append(abc)
            print("I" + str(index) + ": " + self.lines[index - 1] + "\t" + str(codeList[index - 1]) + "\t" + str(abc))
            index = index + 1
        print()
        res = 1
        
        print(colored("Program code is: ","green"))
        print("P = [", end="")
        for i in range(0, len(primeNumbersList)):
            print(str(primeNumbersList[i]) + "^" + str(instructionCodeList[i]), end=", ")
            res = res * (primeNumbersList[i] ** instructionCodeList[i])
        print("]")
        print("#(P) = ", res)
        print()
        return res - 1

    def getInputVaules(self):
        values = self.compiler.getInputValues(self.fileString)
        return values
