  

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        # print(n)
        # print(len(grid))
        j=0
        rowLen=len(grid[0])
        i=len(grid)-1
        c=0
        while(i>-1):
            while(j<rowLen and grid[i][j]>-1):
                j=j+1
                # print(j)
            # print(j)
            # print(rowLen-j)      
            i=i-1
            c=c+rowLen-j
        return c
        