# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getintersect(self, head):
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        intersect = self.getintersect(head)
        if intersect == None:
            return None
        ptr1 = head
        ptr2 = intersect
        while(ptr1!=ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
        