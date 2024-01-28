# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # not using BST properties
        # if root == None or root == p or root == q:
        #     return root
        # left = self.lowestCommonAncestor(root.left,p,q)
        # right = self.lowestCommonAncestor(root.right,p,q)
        # if not left:
        #     return right
        # if not right:
        #     return left
        # return root
        curr = root
        while curr:
            if curr.val > p.val and curr.val>q.val:
                curr = curr.left
            elif curr.val<p.val and curr.val<q.val:
                curr = curr.right
            else:
                return curr