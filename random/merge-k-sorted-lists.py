# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # remove all empty from lists
        ll = []
        for i in range(len(lists)):
            if lists[i] != None:
                ll.append(lists[i])
        lists = ll
        if len(lists)==0:
            return None
        pNode = None
        newList = None
        while len(lists) > 0:
            s = float('inf')
            index = -1
            for i in range(len(lists)):
                if lists[i].val < s:
                    s = lists[i].val
                    index = i
            lists[index] = lists[index].next
            if lists[index] == None:
                del lists[index]
            if pNode == None:
                newList = ListNode(s)
                pNode = newList
            else:
                pNode.next = ListNode(s)
                pNode = pNode.next
                        
        return newList