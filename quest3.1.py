class Stack:
    def __init__(self, sizeofeachstack):
        self.sizeofeachstack=sizeofeachstack
        self.stackindex=[-1,sizeofeachstack-1,(2*sizeofeachstack)-1]
        self.stack=[None]*sizeofeachstack*3

    def push(self, element, number):
        if self.stackindex[number-1]<(number * self.sizeofeachstack)-1:
            self.stackindex[number-1] = self.stackindex[number-1] + 1
            self.stack[self.stackindex[number-1]]=element
        else:
            print "stack {0} full".format(number)

    def pop(self, number):
        if self.stackindex[number-1]>((number-1) * self.sizeofeachstack)-1:
            pop = self.stack[self.stackindex[number-1]]
            self.stack[self.stackindex[number - 1]] = None
            self.stackindex[number-1]=self.stackindex[number-1]-1
            return pop
        else:
            print "stack {0} empty".format(number-1)


st = Stack(5)
st.push(1,1)
st.push(2,1)
st.push(2,1)
st.push(2,1)
st.push(2,1)
st.push(2,1)
st.push(2,1)
st.push(3,3)
st.push(2,2)
st.push(1,2)


print st.stack
