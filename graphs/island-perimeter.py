class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # print(grid[0],len(grid[0]))
        def getStartPoint():
            for i in range(row):
                for j in range(col):
                    # print(i,j)
                    if grid[i][j]==1:
                        return i,j
        x,y = getStartPoint()
        q = deque()
        visited = set()
        visited.add((x,y))
        q.append((x,y))
        c = 0
        while q:
            x,y = q.popleft()
            if x-1>=0 and grid[x-1][y]==1 and (x-1,y) not in visited:
                q.append((x-1,y))
                visited.add((x-1,y))
            elif x-1<0 or grid[x-1][y]==0:
                c+=1
            if x+1<row and grid[x+1][y]==1 and (x+1,y) not in visited:
                q.append((x+1,y))
                visited.add((x+1,y))
            elif x+1>=row or grid[x+1][y]==0:
                c+=1
            if y+1<col and grid[x][y+1]==1 and (x,y+1) not in visited:
                q.append((x,y+1))
                visited.add((x,y+1))
            elif y+1>=col or grid[x][y+1]==0:
                c+=1
            if y-1>=0 and grid[x][y-1]==1 and (x,y-1) not in visited:
                q.append((x,y-1))
                visited.add((x,y-1))
            elif y-1<0 or grid[x][y-1]==0:
                c+=1
        return c