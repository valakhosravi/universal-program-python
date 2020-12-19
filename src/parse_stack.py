class ParseStack(object):
    stack = []

    def top(self):
        return self.stack[len(self.stack) - 1]

    def push(self, input):
        self.stack.append(input)

    def pop(self):
        return self.stack.pop()
    
    def getAsArray(self):
        return self.stack

    def size(self):
        return len(self.stack)