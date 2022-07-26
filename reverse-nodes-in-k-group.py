# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        n=k
        if node == None:
            return node
        while node and k>0:
            node = node.next
            k-=1
        if k==0:
            reveredhead = self.reverseLL(head,n)
            nexthead = self.reverseKGroup(node,n)
            head.next = nexthead
            nexthead=reveredhead
        else:
            nexthead = head
        return nexthead
        
        
            
    
    def reverseLL(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        prev = None
        node = head
        while node and k>0:
            print(node.val)
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            k-=1
        return prev
            
        
        