# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {1:[TreeNode(0)]}
        def dfs(n):
            if n in cache:
                return cache[n]
            ret = []
            for i in range(1,n,2):
                left = dfs(i)
                right = dfs(n-i-1)
                for l in left:
                    for r in right:
                        ret.append(TreeNode(0,l,r))
            cache[n]=ret
            return ret
        return dfs(n)        