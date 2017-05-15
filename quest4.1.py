from binarytree import Tree
def checkheight(root):
    
    if (root is None):
        return 0

    leftheight = checkheight(root.l)

    if leftheight == -1:
        return -1
    rightheight = checkheight(root.r)

    if rightheight == -1:
        return -1

    heightdiff = leftheight - rightheight
    if abs(heightdiff)>1:
        return -1
    else:
        return max(leftheight, rightheight) + 1

t=Tree()
t.add(4)
t.add(2)
t.add(6)

t.add(1)
t.add(3)
t.add(5)
t.add(7)

print checkheight(t.root)