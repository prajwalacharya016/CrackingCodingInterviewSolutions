class Node(object):

    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node=new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head=head
        self.first=head

    def insert(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            self.first = new_node
        else:
            self.head.set_next(new_node)
            self.head=new_node

    def printlist(self):
        current = self.first
        while True:
            if current.get_next() is None:
                print current.get_data()
                break
            else:
                print current.get_data()
                current = current.get_next()
