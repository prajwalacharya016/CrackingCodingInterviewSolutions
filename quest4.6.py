from binarytree import Tree
class state:
    def __init__(self):
        self.trueVal=False
        self.endVal=False

def printInorder(root,data, st):
    if st.endVal==True:
        return
    if root:
        # First recur on left child
        printInorder(root.l,data, st)

        # then print the data of node

        if st.trueVal == True:
            print root.v
            st.endVal=True

        if root.v == data:
          st.trueVal = True

        # now recur on right child
        printInorder(root.r,data, st)

st= state()
t=Tree()
t.add(4)
t.add(2)
t.add(1)
t.add(5)
t.add(7)
t.add(6)
printInorder(t.root, 2, st)

