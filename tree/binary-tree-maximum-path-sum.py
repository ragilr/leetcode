# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = root.val
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            nonlocal ret
            ret = max(ret,node.val+left+right)
            return node.val + max(left,right)
        dfs(root)
        return ret
    # try to fix https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1178599337/