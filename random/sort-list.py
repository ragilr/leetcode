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


#Actual solution using merge sort
class Solution:
       
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def divideLL(head: Optional[ListNode]):
            if head is None or head.next is None:
                return head, None
            h = head.next
            t = head
            while h and h.next:
                h=h.next.next
                t=t.next
            # print(head,t,sep="\n")
            ret=t.next
            t.next=None
            return head, ret

        def mergeSort(head:Optional[ListNode]):
            # print("Mergesort")
            # printLL(head)
            if head is None or head.next is None:
                return head
            l,r = divideLL(head)
            lnode = mergeSort(l)
            rnode = mergeSort(r)
            # print("Merging")
            # print(lnode,rnode,sep="  --- ")
            prev = None
            newhead = None
            while lnode and rnode:
                node = ListNode()
                if newhead is None:
                    newhead = node
                if lnode.val>=rnode.val:
                    node.val = rnode.val
                    rnode = rnode.next
                else:
                    node.val = lnode.val
                    lnode = lnode.next
                if prev:
                    prev.next = node
                prev = node
                # print(newhead)
            while lnode:
                node = ListNode(lnode.val)
                if newhead is None:
                    newhead = node
                if prev:
                    prev.next = node
                prev = node
                lnode = lnode.next
                # print(newhead)
            while rnode:
                node = ListNode(rnode.val)
                if newhead is None:
                    newhead = node
                if prev:
                    prev.next = node
                prev = node
                rnode = rnode.next
                # print(newhead)
            # print("Mergesorted")
            # printLL(newhead)
            return newhead
    
        def printLL(node):
            while(node):
                print(node.val,"->",end="",sep="")
                node=node.next
            print()
        return mergeSort(head)
                
            
            