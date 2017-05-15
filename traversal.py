from binarytree import Tree

def printInorder(root):

    if root:
        # First recur on left child
        printInorder(root.l)

        # then print the data of node
        print(root.v),

        # now recur on right child
        printInorder(root.r)


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.l)

        # the recur on right child
        printPostorder(root.r)

        # now print the data of node
        print(root.v),


def printPreorder(root):

    if root:
        # First print the data of node
        print(root.v),

        # Then recur on left child
        printPreorder(root.l)

        # Finally recur on right child
        printPreorder(root.r)

t=Tree()
t.add(1)
t.add(3)
t.add(4)
t.add(6)
t.add(2)
t.add(3)

printPostorder(t.root)
