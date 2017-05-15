from linkedlist import LinkedList, Node
from binarytree import Tree

llist=[None]*4
def linkedlistimplementation(node,level):
    if node is None:
        return

    if llist[level] is None:
        llist[level]= LinkedList()
        llist[level].insert(node)
    else:
        llist[level].insert(node)

    linkedlistimplementation(node.l,level+1)
    linkedlistimplementation(node.r, level+1)

t=Tree()
t.add(4)
t.add(2)
t.add(1)
t.add(5)
t.add(7)
t.add(6)

linkedlistimplementation(t.root,0)
counter=0
for l in llist:
    print "new list"+str(counter)
    current = l.first
    while True:
        if current is None:
            break
        if current.get_next() is None:
            print current.get_data().v
            break
        else:
            print current.get_data().v
            current = current.get_next()
    counter += 1
