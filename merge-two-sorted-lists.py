# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=list1
        b=list2
        prev = None
        head = None
        while a and b:
            node = None
            if a.val<b.val:
                node=a
                a=a.next
            else:
                node=b
                b=b.next
            if prev:
                prev.next = node
            else:
                head = node
            prev=node
        
        while a:
            if prev:
                prev.next = a
            else:
                head = a
            prev=a
            a=a.next
        while b:
            if prev:
                prev.next=b
            else:
                head=b
            prev=b
            b=b.next
        return head
            
        