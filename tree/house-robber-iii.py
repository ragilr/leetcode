# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # solution using dp
        # cache={}
        # def robHelper(node,canRob):
        #     if not node:
        #         return 0
        #     if (node,canRob) in cache:
        #         return cache[(node,canRob)]
        #     leftRob = robHelper(node.left,True)
        #     rightRob = robHelper(node.right,True)
        #     ret = leftRob+rightRob
        #     if canRob:
        #         ret = max(ret, node.val+robHelper(node.left,False)+robHelper(node.right,False))
        #     cache[(node,canRob)]=ret
        #     return ret
        # return robHelper(root,True)

        def dfs(node):
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            withoutNode = max(left)+max(right)
            withNode = node.val+left[0]+right[0]
            return [withoutNode,withNode]
        return max(dfs(root))