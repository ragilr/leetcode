"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self.recurr(root,[])
        
    def recurr(self, root: 'Node',ret:List[int])->List[int]:
        if root==None:
            return
        ret.append(root.val)
        for c in root.children:
            ret = self.recurr(c,ret)
        # print(ret)
        return ret
        
        
        