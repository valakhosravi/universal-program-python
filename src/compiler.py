from termcolor import colored
import sys
from src.parse_stack import ParseStack


class Compiler(object):
    labelList = ['A1', 'B1', 'C1', 'D1', 'E1', 'A2', 'B2',
                 'C2', 'D2', 'E2', 'A3', 'B3', 'C3', 'D3', 'E3', ]
    variableList = ['Y', 'X1', 'Z1', 'X2', 'Z2', 'X3', 'Z3',
                    'X4', 'Z4', 'X5', 'Z5', 'X6', 'Z6', 'X7', 'Z7', ]
    numberList = ['0', '1']
    grammarList = [
        {'left': 'P', 'right': 'STS'},
        {'left': 'STS', 'right': 'ST STS'},
        {'left': 'STS', 'right': ''},
        {'left': 'ST', 'right': 'A B'},
        {'left': 'A', 'right': '[ label ]'},
        {'left': 'A', 'right': ''},
        {'left': 'B', 'right': 'id <- id M'},
        {'left': 'B', 'right': 'if ~ ( id = 0 ) GoTo label'},
        {'left': 'M', 'right': '+ 1'},
        {'left': 'M', 'right': '- 1'},
        {'left': 'M', 'right': ''},
    ]
    nonTermialList = ['P', 'STS', 'ST', 'A', 'B', 'M']
    terminalList = ['$', '[', 'label', ']', 'id', '<-',
                    'if', '~', '(',	'=', '0', ')', 'GoTo', '+',	'1', '-']
    parseTable = [
        [1,  1, 0, 0,  1,  0,  1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3,  2, 0, 0,  2,  0,  2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0,  4, 0, 0,  4,  0,  4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0,  5, 0, 0,  6,  0,  5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0,  7,  0,  8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [11, 11, 0, 0, 11,  0, 11, 0, 0, 0, 0, 0, 0, 9, 0, 10],
    ]
    inputList = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']

    def __init__(self):
        pass

    def scan(self, word):
        type = None
        if self.isInList(word, self.terminalList):
            type = 'specialToken'
        if self.isInList(word, self.labelList):
            type = 'label'
        if self.isInList(word, self.variableList):
            type = 'id'
        if self.isInList(word, self.numberList):
            type = 'number'
        if type:
            return {
                'value': word,
                'type': type,
            }
        else:
            return False

    def parse(self, command):
        char = ''
        tokenList = []
        for i in range(0, len(command)):
            if command[i] != ' ':
                char = char + command[i]
            token = self.scan(char)
            if token:
                tokenList.append(token)
                char = ''
        tokenList.append({
            'value': '$',
            'type': 'specialToken'
        })
        parseStack = ParseStack()
        parseStack.push('$')
        parseStack.push('P')

        index = 0
        counter = 0
        labelIndex = 0
        commandIndex = -1
        variableIndex = -1
        while parseStack.size() != 0:
            top = parseStack.top()
            # a = input()
            head = tokenList[index]
            if head['type'] == 'label':
                labelIndex = self.findIndexInList(
                    head['value'], self.labelList) + 1
            if head['type'] == 'id':
                variableIndex = self.findIndexInList(
                    head['value'], self.variableList)
            # print('parse stack', parseStack.getAsArray())
            # print('top', top)
            # print('head', head)
            if self.isInList(top, self.nonTermialList):
                v = self.findIndexInList(top, self.nonTermialList)
                if self.isInList(head['value'], self.terminalList):
                    t = self.findIndexInList(head['value'], self.terminalList)
                else:
                    t = self.findIndexInList(head['type'], self.terminalList)
                grammarIndex = self.parseTable[v][t]
                # print('grammar index', grammarIndex)
                if grammarIndex > 0:
                    # print('right', self.grammarList[grammarIndex - 1]['right'])
                    if grammarIndex == 8:
                        lIndex = self.findIndexInList(
                            tokenList[-2]['value'], self.labelList)
                        commandIndex = lIndex + 2
                    if grammarIndex == 9:
                        commandIndex = 1
                    if grammarIndex == 10:
                        commandIndex = 2
                    if grammarIndex == 11:
                        commandIndex = 0
                    parseStack.pop()
                    g = self.grammarList[grammarIndex - 1]['right'].split()
                    for i in range(len(g), 0, -1):
                        parseStack.push(g[i - 1])
            if self.isInList(top, self.terminalList):
                if head['type'] == 'specialToken' or head['type'] == 'number':
                    if head['value'] == top:
                        index = index + 1
                        parseStack.pop()
                    else:
                        print('Wrong input')
                        return
                else:
                    if head['type'] == top:
                        index = index + 1
                        parseStack.pop()
                    else:
                        print('Wrong input')
                        return
            counter = counter + 1
        return (labelIndex, commandIndex, variableIndex,)

    def isInList(self, input, List):
        for element in List:
            if input == element:
                return True
        return False

    def findIndexInList(self, input, List):
        for index in range(0, len(List)):
            if input == List[index]:
                return index
        return -1

    def getInputValues(self, fileString):
        values = []
        lines = fileString.splitlines()
        print(colored("Enter the value of the following inputs: ","green"))
        for line in lines:
            for i in range(0, len(self.inputList)):
                if self.inputList[i] in line:
                    values.append(int(input('X' + str(i + 1) + ': ')))
        print()
        return values

        # get index of inputs , min and max
