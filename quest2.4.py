from linkedlist import Node, LinkedList


def linkedlistpartition(l1,data):

    beforestart = None
    beforeend = None
    afterstart = None
    afterend = None
    node = l1.first

    while node is not None:
        nextn=node.get_next()
        node.set_next(None)

        if node.get_data() < data:
            if beforestart is None:
                beforestart = node
                beforeend = beforestart
            else:
                beforeend.set_next(node)
                beforeend = node

        else:
            if afterstart is None:
                afterstart = node
                afterend = afterstart
            else:
                afterend.set_next(node)
                afterend = node

        node = nextn

    if beforestart is None:
        return LinkedList(afterstart)
    else:
        beforeend.set_next(afterstart)
        return LinkedList(beforestart)

l2 = LinkedList()
l2.insert(1)
l2.insert(2)
l2.insert(7)
l2.insert(5)
l2.insert(3)
l2.insert(7)

linkedlistpartition(l2,5).printlist()

