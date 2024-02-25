class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        visited = set()
        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0 or grid2[i][j]==0 or (i,j) in visited:
                return True
            res = grid1[i][j]==1
            visited.add((i,j))
            res = dfs(i+1,j) and res
            res = dfs(i,j+1) and res
            res = dfs(i-1,j) and res
            res = dfs(i,j-1) and res
            return res

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in visited:
                    if dfs(i,j):
                        # print("adding",i,j)
                        ret+=1
                        # print(visited)
        return ret