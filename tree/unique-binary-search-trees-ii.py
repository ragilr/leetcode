# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def helper(l,h):
            if l>h:
                return [None]
            if (l,h) in dp:
                return dp[(l,h)]
            ret = []
            for val in range(l,h+1):
                left = helper(l,val-1)
                right = helper(val+1,h)
                for i in left:
                    for j in right:
                        root = TreeNode(val,i,j)
                        ret.append(root)
            dp[(l,h)] = ret
            return ret
        return helper(1,n)