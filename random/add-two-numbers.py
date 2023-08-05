# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        head = None
        c=0
        n1,n2=l1,l2
        while n1 and n2:
            s=n1.val+n2.val+c
            c=s//10
            node=ListNode(s%10)
            if prev:
                prev.next=node
            else:
                head=node
            prev=node
            n1=n1.next
            n2=n2.next
        while n1:
            s=n1.val+c
            c=s//10
            node=ListNode(s%10)
            if prev:
                prev.next=node
            else:
                head=node
            prev=node
            n1=n1.next
        while n2:
            s=n2.val+c
            c=s//10
            node=ListNode(s%10)
            if prev:
                prev.next=node
            else:
                head=node
            prev=node
            n2=n2.next
        if c>0:
            node=ListNode(c)
            prev.next=node
        return head
        
            
                
            

