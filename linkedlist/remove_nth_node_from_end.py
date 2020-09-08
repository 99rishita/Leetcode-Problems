# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenh = 0
        p = head
        while p!=None:
            p = p.next
            lenh += 1
        diff = lenh-n
        if diff == 0:
            head = head.next
            return head
        q = head
        prev = head
        while diff!=0 and q.next!=None:
            prev = q
            q = q.next
            diff -= 1
        prev.next = q.next
        return head