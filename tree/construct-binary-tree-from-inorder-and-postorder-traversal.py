# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i,n in enumerate(inorder):
            index[n]=i
        
        def makeTree(l,r):
            if l>r:
                return None
            val = postorder.pop()
            idx = index[val]
            right = makeTree(idx+1,r)
            left = makeTree(l,idx-1)
            return TreeNode(val,left,right)
        return makeTree(0,len(inorder)-1)