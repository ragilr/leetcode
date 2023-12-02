class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        l = len(grid[0])
        prefRow1 = grid[0].copy()
        prefRow2 = grid[1].copy()
        
        for i in range(1,l):
            prefRow1[i]=prefRow1[i-1]+grid[0][i]
            prefRow2[i]=prefRow2[i-1]+grid[1][i]

        ret = float('inf')

        for i in range(l):
            top = prefRow1[-1]-prefRow1[i]
            bottom = prefRow2[i-1] if i > 0 else 0
            secondRobot = max(top,bottom)
            ret = min(ret,secondRobot)
            
        return ret
        