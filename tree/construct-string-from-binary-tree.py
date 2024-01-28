# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ret = ""
        def preOrder(node):
            nonlocal ret
            # print(node)
            if node == None:
                return
            ret = ret+str(node.val)
            # print(node.val,ret)
            if node.left:
                ret+="("
                # print(node.val,ret)
            preOrder(node.left)
            if node.left:
                ret+=")"
                # print(node.val,ret)
            if not node.left and node.right:
                ret+="()"
            if node.right:
                ret+="("
                # print(node.val,ret)
            preOrder(node.right)
            if node.right:
                ret+=")"
                # print(node.val,ret)
            # print(node.val,ret)
        preOrder(root)
        return ret        