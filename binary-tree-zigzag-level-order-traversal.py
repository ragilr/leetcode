# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = set()
        q = deque()
        ret = []
        def bfs():
            if root == None:
                return ret
            q.append(root)
            zigzag = False
            while q:
                l = []
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    tempq = []
                    l.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if zigzag:
                    l.reverse()
                ret.append(l)
                zigzag = not zigzag
            return ret
        return bfs()