#Based on LeetCode solution.
#Test cases according to LeetCode not done in here create a Listnode object
#LLinkedList Soltion
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        carry = 0
        firstVal = True
        l3 = None
        while True:
            sum = l1.val + l2.val + carry
            carry = sum / 10
            sum = sum % 10

            if (firstVal == True):
                l3 = ListNode(sum)
                firstNode = l3
                firstVal = False

            else:
                l3.next = ListNode(sum)
                l3 = l3.next

            if l1.next is None and l2.next is not None:
                l1.next = ListNode(0)

            if l2.next is None and l1.next is not None:
                l2.next = ListNode(0)

            if l1.next == None and l2.next == None:
                if carry > 0:
                    l3.next = ListNode(carry)
                break

            l1 = l1.next
            l2 = l2.next

        l3 = firstNode
        return l3