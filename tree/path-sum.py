# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,target):
            if not node:
                return False
            target = target - node.val
            if target==0 and node.left == None and node.right == None:
                return True
            return (dfs(node.left,target) or dfs(node.right,target))
        return dfs(root,targetSum) if root else False
