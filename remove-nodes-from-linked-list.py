# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove(node,prev)->int:
            if node.next == None:
                return node
            rightHighNode = remove(node.next,node)
            if node.val<rightHighNode.val:
                # print("removing",node.val)
                if prev!=None:
                    prev.next=node.next
                return rightHighNode
            return node
        return remove(head,None)
        # return head
        
