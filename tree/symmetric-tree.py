# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(lnode,rnode):
            if lnode==None and rnode==None:
                return True
            elif lnode and rnode==None:
                return False
            elif rnode and lnode==None:
                return False
            
            if lnode.val!=rnode.val:
                return False
            
            return dfs(lnode.left,rnode.right) and dfs(lnode.right,rnode.left)
        return dfs(root.left,root.right)