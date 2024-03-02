class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    treasure.append((i,j))
        
        def bfs(i,j):
            visited = set()
            q = deque()
            q.append((i,j,0))
            visited.add((i,j))
            while(q):
                for _ in range(len(q)):
                    i,j,prev = q.popleft()
                    if i<0 or j<0 or i>=row or j>=col or grid[i][j]==-1:
                        continue
                    grid[i][j] = min(grid[i][j],prev+1)
                    neigh = [[0,-1],[0,1],[1,0],[-1,0]]
                    for dr,dc in neigh:
                        r,c = i+dr,j+dc
                        if (r,c) not in visited:
                            visited.add((r,c))
                            q.append((r,c,grid[i][j]))

        for t in treasure:
            i,j = t
            bfs(i,j)
        