# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        odd = head
        even = head.next
        evenhead = even
        
        while even!=None and even.next!=None:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = evenhead
        return head