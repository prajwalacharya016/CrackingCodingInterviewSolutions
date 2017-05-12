from linkedlist import Node, LinkedList

def removedups(l1):
    data=l1.first
    previous=None
    dic={}

    while data is not None:
        if data.get_data() in dic:
            previous.set_next(data.get_next())
        else:
            dic[data.get_data()]=Node(data)
            previous=data
        data=data.get_next()

l1 = LinkedList()

l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(1)
l1.insert(2)
l1.insert(7)
l1.printlist()
removedups(l1)
print "After no dups"
l1.printlist()

