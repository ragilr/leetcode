# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head and head.next == None:
            return True
        t,h = head,head
        prev = None
        while h!=None and h.next!=None:
            h = h.next.next
            prev=t
            t=t.next
        prev=t
        t=t.next
        prev.next=None
        while t!=None:
            t.next,prev,t=prev,t,t.next
        t=head
        while t and prev:
            if t.val!=prev.val:
                return False
            prev=prev.next
            t=t.next
        return True
        
        
        # slow, fast, prev = head, head, None
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        # prev, slow, prev.next = slow, slow.next, None
        # while slow:
        #     slow.next, prev, slow = prev, slow, slow.next
        # fast, slow = head, prev
        # while slow:
        #     if fast.val != slow.val: return False
        #     fast, slow = fast.next, slow.next
        # return True