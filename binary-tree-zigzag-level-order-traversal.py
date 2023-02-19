# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs():
            level = 0
            visited = set()
            q = deque()
            q.append((root, level))
            visited.add(root)
            ret = []
            while q:
                l = []
                size = len(q)
                for i in range(size):
                    s = q.popleft()
                    node = s[0]
                    l.append(node.val)
                    if s[1] == 0:
                        if node.left != None:
                            q.append((node.left, 1))
                            visited.add(node.left)
                        if node.right != None:
                            q.append((node.right, 1))
                            visited.add(node.right)
                    else:
                        if node.right != None:
                            q.append((node.right, 0))
                            visited.add(node.right)
                        if node.right != None:
                            q.append((node.left, 0))
                            visited.add(node.right)
                ret.append(l)
            return ret
        return bfs()
