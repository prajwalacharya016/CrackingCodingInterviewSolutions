class IndividualStack:
    def __init__(self):
        self.stack=[None]*5


class StackwithStacks:
    def __init__(self):
        self.stacks = []
        self.stackcount=-1
        self.count=0
        self.st = None

    def push(self, element):
        if self.count%5==0:
            self.stackcount = self.stackcount+1
            self.count=0
            self.st=IndividualStack()
            self.stacks.append(self.st)
            self.st.stack[self.count]=element
            self.count = self.count+1

        else:
            self.st.stack[self.count] = element
            self.count = self.count + 1

    def pop(self):
        if self.count == 1:
            self.count=self.count-1
            returnval= self.stacks[self.stackcount].stack[self.count]
            self.stacks.pop()
            self.stackcount=self.stackcount-1
            self.count=5
            return returnval

        else:
            self.count = self.count - 1
            return self.stacks[self.stackcount].stack[self.count]


st = StackwithStacks()

st.push(1)
st.push(1)
st.push(1)
st.push(1)
st.push(1)
st.push(12)
st.push(13)
st.push(1)
st.push(4)
st.push(7)
st.push(1)
st.push(8)
st.push(1)
st.push(6)


print st.pop()
print st.pop()
print st.pop()
print st.pop()
print st.pop()
print st.pop()
print st.pop()
print st.pop()