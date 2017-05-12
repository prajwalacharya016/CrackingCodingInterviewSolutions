from linkedlist import LinkedList, Node


def ktolast(llist, k):
    if k<=0:
        return None

    p1=llist.first
    p2=llist.first
    for i in range(0,k-1):
        if p1 is None:
            return None
        p1=p1.get_next()

    if p1 is None :
        return None

    while p1.get_next() is not None:
        p1=p1.get_next()
        p2=p2.get_next()

    return p2

l2 = LinkedList()
l2.insert(1)
l2.insert(2)
l2.insert(3)
l2.insert(5)
l2.insert(7)

LinkedList(ktolast(l2,5)).printlist()

