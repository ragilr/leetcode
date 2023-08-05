# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t=head
        if head:
            h=head.next
        else:
            h=head
        while t and h:
            if t==h:
                return True
            t=t.next
            if h.next:
                h=h.next.next
            else:
                h=None
        return False
                
        