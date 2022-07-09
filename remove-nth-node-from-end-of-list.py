# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        prev=None
        while n>0:
            n-=1
            prev=node
            node=node.next
        if node is None:
            head = head.next
            return head
        rem = head
        while node:
            print(rem.val,node.val)
            prev=rem
            rem=rem.next
            node=node.next
        if prev:
            prev.next=rem.next
        else:
            head=prev
        return head
        