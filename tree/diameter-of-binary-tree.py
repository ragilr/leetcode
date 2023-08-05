# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hcached = dict()
        def height(node):
            if node == None:
                return 0
            if node in hcached:
                return hcached[node]
            h = 1+max(height(node.left),helight(node.right))
            hcached[node]=h
            return h
        m = float('-inf')
        
        def inorder(node):
            if node==None:
                return 
            inorder(node.left)
            inorder(node.right)
            m = max(hl+hr,m)
            return m            