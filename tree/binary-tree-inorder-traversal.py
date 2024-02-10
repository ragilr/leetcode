# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ret = []
        # def inorder(node):
        #     if node==None:
        #         return
        #     inorder(node.left)
        #     ret.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return ret
        stack = deque()
        node = root
        ret = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ret.append(node.val)
            node = node.right
        return ret
        