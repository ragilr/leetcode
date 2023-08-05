# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersect(self,head):
        t,h=head,head
        while h and h.next:
            t=t.next
            h=h.next.next
            if t==h:
                return h
        return None
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        ptr1=head
        ptr2=intersect
        while ptr1!=ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next
        return ptr2
            
            
        