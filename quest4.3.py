from binarytree import Tree, Node
t=Tree()
def createminimalBST(list,start,end):
    if end<start:
        return
    mid=(start+end)/2
    print list[mid]
    t.add(Node(list[mid]))
    createminimalBST(list,start,mid-1)
    createminimalBST(list,mid+1,end)

array =[1,2,3,4,5,6,7,8]
createminimalBST(array,0,len(array)-1)

