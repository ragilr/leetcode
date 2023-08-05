# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        w=dict()
    
        def width(root: Optional[TreeNode], level:int, num:int) -> None:
            if root==None:
                return
            if level in w:
                if num < w[level][0]:
                    w[level][0]=num
                if num > w[level][1]:
                    w[level][1]=num
            else:
                w[level]=[num,num]
            width(root.left,level+1,num*2+1)
            width(root.right,level+1,num*2+2)
        
        
        width(root,0,0)
        # print(w)
        m=-1
        for k,v in w.items():
            m=max(m,abs(v[0]-v[1])+1)
            # print(k,v,abs(v[0]-v[1]+1))
        return m
        
        
        