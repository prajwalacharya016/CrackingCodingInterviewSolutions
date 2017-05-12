from linkedlist import LinkedList, Node

def deleteNode(l2,data):
    head=l2.first
    n=None
    while head:
        if head.data == data:
            n = head
            break
        else:
            head=head.get_next()

    if n is None or n.get_next() is None:
        return False

    nextd = n.get_next()
    n.data = nextd.get_data()
    n.set_next(nextd.get_next())
    return True

l2 = LinkedList()
l2.insert(1)
l2.insert(2)
l2.insert(3)
l2.insert(5)
l2.insert(7)

deleteNode(l2,7)
l2.printlist()