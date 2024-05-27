#m*n
#unique paths to reach from 0,0 to m-1,n-1
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0


def uniquePaths(mat):
    m = len(mat)
    n = len(mat[0])
    cache = {}
    def dfs(i,j):
        if i>=m or j>=n:
            return 0
        if i==m-1 and j==n-1:
            return 1
        if (i,j) in cache:
            return cache[(i,j)]
        moves = dfs(i+1,j) + dfs(i,j+1)
        cache[(i,j)] = moves
        return moves
    return dfs(0,0)


# 6 3 1 0
# 3 2 1 0   
# 1 1 1 0
def uniquePathsImp(mat):
    m = len(mat)
    n = len(mat[0])
    path = [1]*(n+1)
    path[n] = 0
    for i in range(m-1):
        for j in range(n-1,-1,-1):
            path[j]=path[j+1]+path[j]
    return path[0]



# mat = [[0,0],[0,0]]
# mat = [[0,0,0],[0,0,0],[0,0,0]]
mat = [[0,0,0,0],[0,0,0,0]]
# mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

print(uniquePaths(mat))
print(uniquePathsImp(mat))



