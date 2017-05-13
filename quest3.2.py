import sys
def peek(list):
    return list[-1]


class stackwithmin:
    def __init__(self):
        self.stack = []
        self.minstack = [sys.maxint]

    def push(self, data):
        if data<peek(self.minstack):
            self.minstack.append(data)

        self.stack.append(data)

    def pop(self):
        data = self.stack.pop()
        if data == peek(self.minstack):
            self.minstack.pop()
        return data

    def min(self):
        return peek(self.minstack)

s=stackwithmin()
s.push(1)
s.push(2)
s.push(1)
s.push(1)
s.push(32)
s.push(-1)
s.push(3)

print s.min()