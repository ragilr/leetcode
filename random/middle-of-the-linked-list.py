# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        h=head.next
        while h is not None:
            h=h.next
            if h is not None:
                h=h.next
            t=t.next
            if h is not None:
                print(t.val,h.val)
            else:
                print(t.val)
        return t