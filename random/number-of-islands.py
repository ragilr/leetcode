class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(i,j) -> bool:
            return (i>-1 and i<len(grid) and j>-1 and j<len(grid[0]))
        def count(i,j):
            grid[i][j]="0"
            # print("hey",i,j)
            if isValid(i+1,j) and grid[i+1][j]=="1":
                count(i+1,j)
            if isValid(i-1,j) and grid[i-1][j]=="1":
                count(i-1,j)
            if isValid(i,j+1) and grid[i][j+1]=="1":
                count(i,j+1)
            if isValid(i,j-1) and grid[i][j-1]=="1":                
                count(i,j-1)
            return 1
        c=0
        print("limits",len(grid),len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(grid)
                if grid[i][j]=="1":
                    c+=1
                    count(i,j)
                    # print("herer",i,j,c)
        return c
                
                