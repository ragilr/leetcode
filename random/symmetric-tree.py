# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def canContinue(a,b):
            if a and b:
                return True
            elif not a and not b:
                return True
            return False
        
        lq=deque()
        rq=deque()
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False
        if not root.left and not root.right:
            return True
        lq.append(root.left)
        rq.append(root.right)
        while lq and rq:
            lnode = lq.popleft()
            rnode = rq.popleft()
            
            if lnode.val != rnode.val:
                return False
            
            if not canContinue(lnode.left,rnode.right):
                return False
            elif lnode.left:
                lq.append(lnode.left)
                rq.append(rnode.right)
                
            if not canContinue(lnode.right,rnode.left):
                return False
            elif lnode.right:
                lq.append(lnode.right)
                rq.append(rnode.left)
            
            
        if lq:
            return False
        if rq:
            return False
        return True