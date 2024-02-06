# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node,n):
            n = n*10+node.val
            if not node.left and not node.right:
                return n
            left = right = 0
            if node.left:
                left = helper(node.left,n)
            if node.right:
                right = helper(node.right,n)
            print(left,right)
            return left+right
        return helper(root,0)