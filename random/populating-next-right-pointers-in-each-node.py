"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        q=deque()
        q.append((root,0))
        level=[]
        while q:
            item=q.popleft()
            if item[1]==len(level):
                level.append([])
            level[item[1]].append(item[0])
            if item[0].left:
                q.append((item[0].left,item[1]+1))
                q.append((item[0].right,item[1]+1))
        for l in level:
            i=0
            for i in range(len(l)-1):
                l[i].next=l[i+1]
            l[i]=None
        return root
        