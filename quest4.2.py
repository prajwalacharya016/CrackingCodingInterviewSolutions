class Node:
    def __init__(self,str):
        self.next=[]
        self.visited = False
        self.name = str

def search(node):
    if node.visited == True:
        return
    else:
        node.visited=True
    for n in node.next:
        search(n)

def depthfirstsearch(nlist):
    for node in nlist:
        search(node)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.next.extend([B,C])
B.next.extend([A,D,E])
C.next.extend([F])
D.next.extend([B])
E.next.extend([B,F])
F.next.extend([C])
start=C
end=A
nlist=[start]
depthfirstsearch(nlist)
print end.visited




