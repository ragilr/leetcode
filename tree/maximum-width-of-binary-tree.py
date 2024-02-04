# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q  = deque()
        q.append([root,1])
        m = 0
        while q:
            l = len(q)
            m = max(m,q[-1][1]-q[0][1]+1)
            for i in range(l):
                node,n = q.popleft()
                if node.left:
                    q.append([node.left,2*n])
                if node.right:
                    q.append([node.right,2*n+1])
        return m