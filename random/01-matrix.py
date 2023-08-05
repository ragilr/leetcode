class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mem=[]
        visited=[]
        for i in range(m):
            mem.append([float('inf')]*n)
            visited.append([False]*n)
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    mem[i][j]=0
                    visited[i][j]=True
                    q.append((i,j))
        while q:
            v = q.popleft()
            i=v[0]
            j=v[1]
            if i+1<m and not visited[i+1][j] and mem[i+1][j] > mem[i][j]+1:
                mem[i+1][j]=mem[i][j]+1
                visited[i+1][j]=True
                q.append((i+1,j))
            if i-1>=0 and not visited[i-1][j] and mem[i-1][j] > mem[i][j]+1:
                mem[i-1][j]=mem[i][j]+1
                visited[i-1][j]=True
                q.append((i-1,j))                    
            if j+1<n and not visited[i][j+1] and mem[i][j+1] > mem[i][j]+1:
                mem[i][j+1]=mem[i][j]+1
                visited[i][j+1]=True
                q.append((i,j+1))
            if j-1>=0 and not visited[i][j-1] and mem[i][j-1] > mem[i][j]+1:
                mem[i][j-1]=mem[i][j]+1
                visited[i][j-1]=True
                q.append((i,j-1))                    
        return mem
        