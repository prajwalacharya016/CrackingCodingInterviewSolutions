class Tower:
    def __init__(self, index):
        self.stack = []
        self.index = index

    def get_index(self):
        return self.index

    def add(self, d):
        self.stack.append(d)

    def moveTopTo(self,t):
        top=self.stack.pop()
        t.add(top)
        print "Move disks {0} from {1} to {2}".format(top,self.index,t.get_index())

    def moveDisks(self, n, destination, buffer):
        if n>0:
            self.moveDisks(n-1, buffer, destination)
            self.moveTopTo(destination)
            buffer.moveDisks(n-1, destination, self)

n = 3

towers = []

for i in range(0,3):
    towers.append(Tower(i))

for i in range (n-1,-1,-1):
    towers[0].add(i)

towers[0].moveDisks(n, towers[2], towers[1])
