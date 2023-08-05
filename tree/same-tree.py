# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(p,q) -> bool:
            if p == None and q == None:
                return True
            elif p == None:
                return False
            elif q == None:
                return False
            if p.val!=q.val:
                return False
            l = inorder(p.left,q.left)
            r = inorder(p.right,q.right)
            return l and r
        return inorder(p,q)