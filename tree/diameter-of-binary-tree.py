# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # hcached = dict()
        def height(node):
            if node == None:
                return 0
            # if node in hcached:
            #     return hcached[node]
            l =  height(node.left)
            r =  height(node.right)             
            self.result = max(self.result,l+r)
            h = 1+max(l,r)
            # hcached[node]=h
            return h
        height(root)
        return self.result


    def __init__(self):
            self.result = float('-inf')