# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        
        def mergeHelper(root1,root2):
            if root1 == None and root2 == None:
                return None
            newnode=TreeNode()
            left=None
            right=None
            if root1 and root2:
                newnode.val=root1.val+root2.val
                left=mergeHelper(root1.left,root2.left)
                right=mergeHelper(root1.right,root2.right)
            elif root2:
                newnode.val=root2.val
                left=mergeHelper(None,root2.left)
                right=mergeHelper(None,root2.right)
            else:
                newnode.val=root1.val
                left=mergeHelper(root1.left,None)
                right=mergeHelper(root1.right,None)
            newnode.left=left
            newnode.right=right
            return newnode
        return mergeHelper(root1,root2)
            
                
        