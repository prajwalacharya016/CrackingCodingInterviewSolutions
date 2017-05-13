from linkedlist import Node


def returnbeginning(n1):

    fast = n1
    slow = n1
    while fast.get_next() is not None and slow.get_next() is not None:
        fast=fast.get_next().get_next()
        slow=slow.get_next()

        if fast is slow:
            break

    fast = n1

    while True:
        if fast is slow:
            return slow
        else:
            fast = fast.get_next()
            slow = slow.get_next()


n8 = Node(8)
n7 = Node(7,n8)
n6 = Node(6,n7)
n5 = Node(5,n6)
n4 = Node(4,n5)
n3 = Node(3,n4)
n8.set_next(n3)
n2 = Node(2,n3)
n1 = Node(1,n2)
print returnbeginning(n1).get_data()