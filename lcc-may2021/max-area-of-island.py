class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxY=len(grid[0])
        maxX=(len(grid))
        i=0
        j=0
        maxArea = -1
        for i in range(maxX):
            for j in range(maxY):
                #print(i,j)
                area = self.visitIsland(grid,i,j)
                if area>maxArea:
                    maxArea = area
                # print("Area",i,j,area)
                # j+=1
            # i+=1
        # return self.visitIsland(grid,3,8)
        return maxArea
    
    def visitIsland(self, grid: List[List[int]], x, y) -> None:
        # print('Trying to visit',x,y)
        maxY = len(grid[0])
        maxX = (len(grid))
        if(x<0 or y<0 or x>=maxX or y>=maxY or grid[x][y]==0):
            return 0
        # print('Exploring',x,y)
        grid[x][y] = 0
        a = self.visitIsland(grid,x+1,y)
        b = self.visitIsland(grid,x,y+1)
        c = self.visitIsland(grid,x-1,y)
        d = self.visitIsland(grid,x,y-1)
        # print('Visited',x,y)
        return 1+a+b+c+d