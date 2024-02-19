"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(n,r,c):
            val = grid[r][c]
            leaf = True
            for i in range(r,r+n):
                for j in range(c,c+n):
                    if grid[i][j]!=val:
                        leaf=False
                        break
            if leaf:
                return Node(val,True,None,None,None,None)
            n=n//2
            topLeft = helper(n,r,c)
            topRight = helper(n,r,c+n)
            bottomLeft = helper(n,r+n,c)
            bottomRight = helper(n,r+n,c+n)
            return Node(val,False,topLeft,topRight,bottomLeft,bottomRight)
        return helper(len(grid),0,0)