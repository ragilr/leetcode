# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node == None or self.result==False:
                return 0
            l = height(node.left)
            r = height(node.right)
            if abs(l-r)>1:
                self.result = False
            return 1+max(l,r)
        height(root)
        return self.result 

        