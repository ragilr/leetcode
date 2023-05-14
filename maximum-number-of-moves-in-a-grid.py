class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dist = []
        def isvalid(i,j):
            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False
            # print("isvalid true",i,j)
            return True
            
        def fillDist(i,j):
            # print(i,j)
            d = dist[i][j]
            if d!=-1:
                return d
            tot=0
            if isvalid(i-1,j+1) and grid[i][j]<grid[i-1][j+1]:
                tot=max(fillDist(i-1,j+1)+1,tot)
            if isvalid(i,j+1) and grid[i][j]<grid[i][j+1]:
                tot=max(fillDist(i,j+1)+1,tot)
            if isvalid(i+1,j+1) and grid[i][j]<grid[i+1][j+1]:
                tot=max(fillDist(i+1,j+1)+1,tot)
            dist[i][j]=tot
            # print("dist",i,j,tot)
            return tot
        for i in range(m):
            dist.append([-1]*n)
        for i in range(m):
            fillDist(i,0)
        mx = 0
        # print(dist)
        for i in range(m):
            # print(dist[i][0])
            mx=max(dist[i][0],mx)
        return mx