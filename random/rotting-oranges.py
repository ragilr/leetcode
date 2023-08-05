class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        c = 0
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        minutes=0
        while q:
            c=len(q)
            # print(q)
            for k in range(c):
                v=q.popleft()
                i=v[0]
                j=v[1]
                if i+1<m and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    q.append((i+1,j))
                    fresh-=1
                if i-1>=0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    q.append((i-1,j))                    
                    fresh-=1
                if j+1<n and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    q.append((i,j+1))
                    fresh-=1
                if j-1>=0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    q.append((i,j-1))     
                    fresh-=1
            minutes+=1
        if fresh==0 and minutes==0:
            return 0
        elif fresh==0:
            return minutes-1
        return -1