class Queue:
    def __init__(self):
        self.stackfirst=[]
        self.stacksecond=[]

    def enqueue(self,data):
        self.stackfirst.append(data)

    def dequeue(self):
        if not self.stacksecond:
            while True:
                if self.stackfirst:
                    self.stacksecond.append(self.stackfirst.pop())
                else:
                    break
        return self.stacksecond.pop()


s1=Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)
s1.enqueue(4)
s1.enqueue(5)
print s1.dequeue()
s1.enqueue(9)
print s1.dequeue()
print s1.dequeue()
print s1.dequeue()
s1.enqueue(7)
print s1.dequeue()
print s1.dequeue()
print s1.dequeue()


