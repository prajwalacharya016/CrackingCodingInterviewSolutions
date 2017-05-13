from linkedlist import LinkedList, Node


def ispalindrome(l1):
    slow=l1.first
    fast=l1.first
    stack=[]
    while True:
        if fast is None or fast.get_next() is  None:
            break
        else:
            stack.append(slow)
            slow=slow.get_next()
            fast=fast.get_next().get_next()

    if fast is not None:
            slow=slow.get_next()

    while True:
        if slow is None:
            break

        if stack.pop().get_data() == slow.get_data():
            slow=slow.get_next()

        else:
            return False

    return True

l1=LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(2)
l1.insert(1)

print ispalindrome(l1)