class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getroot(self):
        return self.root

    def addvalue(self, val, node):
        if val < node.v:
            if node.l is not None:
                self.addvalue(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self.addvalue(val, node.r)
            else:
                node.r = Node(val)

    def add(self, val):
        if self.root is None:
            self.root =Node(val)
        else:
            self.addvalue(val, self.root)