# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        ptr = result
        carry = 0
        x = 0
        y = 0
        sumtotal = 0
        while l1 or l2 or carry:
            if l1 != None:
                x = l1.val
            elif l1 == None or l2 == None:
                x = 0
            if l2 != None:
                y = l2.val
            elif l1 == None or l2 == None:
                y = 0
            sumtotal = x + y + carry
            carry = (sumtotal) // 10
            out = (sumtotal)%10
            ptr.next = ListNode(out)
            ptr = ptr.next
            if l2 != None:
                l2 = l2.next
            if l1 != None:
                l1 = l1.next
        return result.next