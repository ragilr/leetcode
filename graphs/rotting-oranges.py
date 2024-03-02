class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = set()
        def visitNeigh(i,j,q,visited):
            if i-1>=0 and (i-1,j) not in visited and grid[i-1][j]==1:
                q.append((i-1,j))
                visited.add((i-1,j))
            if i+1<row and (i+1,j) not in visited and grid[i+1][j]==1:
                q.append((i+1,j))
                visited.add((i+1,j))
            if j-1>=0 and (i,j-1) not in visited and grid[i][j-1]==1:
                q.append((i,j-1))
                visited.add((i,j-1))
            if j+1<col and (i,j+1) not in visited and  grid[i][j+1]==1:
                q.append((i,j+1))
                visited.add((i,j+1))

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    visitNeigh(i,j,q,visited)
        time = 0
        # print(q)
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                grid[i][j]=2
                visitNeigh(i,j,q,visited)
            time+=1
            # print(q)

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1
        return time