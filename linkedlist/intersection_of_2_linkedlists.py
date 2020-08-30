# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        ptr1 = headA
        ptr2 = headB
        lenA = 0
        lenB = 0
        while ptr1:
            ptr1 = ptr1.next
            lenA += 1
        while ptr2:
            ptr2 = ptr2.next
            lenB += 1
        diff = abs(lenA - lenB)
        p = headA
        q = headB
        if lenA>lenB:
            while diff:
                p = p.next
                diff -= 1
        else:
            while diff:
                q = q.next
                diff -= 1
        while p!=q:
            if p == None or q == None:
                return None
            p = p.next
            q = q.next
        return p
