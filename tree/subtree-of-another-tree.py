# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def searchSubTree(node):
            if node == None:
                return False
            if node.val==subRoot.val:
                print('here')
                if isSameTree(node,subRoot):
                    return True
            l = searchSubTree(node.left)
            r = searchSubTree(node.right)
            return l or r
            
            
        def isSameTree(p,q):
            if not p and not q:
                return True
            elif not p:
                return False
            elif not q:
                return False
            # print('here1',p.val,q.val)
            if p.val!=q.val:
                return False
            l = isSameTree(p.left,q.left)
            r = isSameTree(p.right,q.right)
            # print("child",l,r)
            return l and r
        
        return searchSubTree(root)