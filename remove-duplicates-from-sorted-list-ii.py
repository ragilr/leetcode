# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        newHead = None
        if not head:
            return None
        while node:
            if node.next and node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node=node.next
                node=node.next
                if prev:
                    prev.next=node
                else:
                    newHead=node
                if node and not node.next:
                    prev=node
                elif node and node.next and node.next.val!=node.val:
                    prev=node
            elif prev:
                prev=node
                node=node.next
            else:
                newHead=node
                prev=node
                node=node.next
        return newHead
            
        