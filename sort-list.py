# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        a = []
        while node:
            a.append(node.val)
            node=node.next
        a.sort()
        head=prev=None
        for i in a:
            print(i)
            node=ListNode(i)
            if prev:
                prev.next=node
            else:
                head=node
            prev=node
        return head
            