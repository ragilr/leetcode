# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node,mx):
            if node == None:
                return 0
            ret = 0
            if node.val>=mx:
                ret+=1
                mx = node.val
            left = traverse(node.left,mx)
            right = traverse(node.right,mx)
            return left+right+ret
        return traverse(root,float('-inf'))