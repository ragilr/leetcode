# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        prev = None
        node = head
        while node!=None and node.next!=None:
            temp1 = node
            temp2 = node.next
            temp3 = temp2.next
            if prev!=None:
                prev.next = temp2
            else:
                head=temp2
            temp2.next=temp1
            temp1.next=temp3
            node=temp3
            prev=temp1
        return head
            
    