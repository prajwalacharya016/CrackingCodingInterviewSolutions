from binarytree import Tree, Node
import sys

def checkBST(node, min, max):

    if node is None:
        return

    if node.v <= min or node.v > max:
        return False
    if checkBST(node.l,min,node.v) is False or checkBST(node.r, node.v, max) is False:
        return False

    return True

t=Tree()
t.add(4)
t.add(2)
t.add(6)

t.add(1)
t.add(3)
t.add(5)
t.add(7)

print checkBST(t.root,-sys.maxint-1, sys.maxint)