# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inord = deque()
        s = 0
        def inorder(node):
            nonlocal s
            if not node:
                return
            inorder(node.right)
            s = node.val+s
            node.val = s
            inorder(node.left)
        inorder(root)
        return root