# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.count = float('inf')
        self.small = float('inf')

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        self.count = k
        self.traverse(root)
        return self.small

    def traverse(self,node):
        if node.left!=None:
                self.traverse(node.left)
        self.count = self.count - 1
        if self.count==0:
            self.small = node.val
            return
        if node.right!=None:
            self.traverse(node.right)                