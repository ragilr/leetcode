# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        preorder=deque(preorder)
        for i,n in enumerate(inorder):
            index[n]=i
        def helper(l,r):
            if l>r:
                return None
            val = preorder.popleft()
            idx = index[val]
            left = helper(l,idx-1)
            right = helper(idx+1,r)
            return TreeNode(val,left,right)
        return helper(0,len(inorder)-1)

        