# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dup = {}
        path = set()
        def dfs(node):
            if not node:
                return
            sleft = dfs(node.left)
            sright = dfs(node.right)
            sleft = "l"+sleft if sleft else "lnone"
            sright = "r"+sright if sright else "rnone"
            s = sleft+str(node.val)+sright
            # print(node.val,s,s in path)
            if s in path:
                dup[s]=node
            path.add(s)
            return s
        dfs(root)
        # print(root)
        ret = []
        # print(dup)
        for k,v in dup.items():
            ret.append(v)
        return ret