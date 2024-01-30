# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = []
        def helper(root,l):
            if not root:
                return
            if l==len(level):
                level.append([])
            level[l]=root.val
            helper(root.left,l+1)
            helper(root.right,l+1)
        
        helper(root,0)
        return level
            
        