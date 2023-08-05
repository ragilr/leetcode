# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        self.reverse(head)
        head.next = None
        return self.head
    
    def reverse(self, node:Optional[ListNode]):
        if node.next == None:
            self.head = node
            return node
        prev = self.reverse(node.next)
        prev.next = node
        return node

    #iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev