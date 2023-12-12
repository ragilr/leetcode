class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = []
        row,col = len(matrix),len(matrix[0])
        self.pre = [[0]*(col+1) for r in range(row+1)]
        for i in range(row):
            prefix = 0
            for j in range(col):
                prefix += matrix[i][j]
                above = self.pre[i][j+1]
                self.pre[i+1][j+1]=prefix+above

        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.pre[r2][c2]
        above = self.pre[r1-1][c2]
        left = self.pre[r2][c1-1]
        topLeft = self.pre[r1-1][c1-1]
        return bottomRight-above-left+topLeft

            

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)