class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])        
        i = 0
        j = n-1
        while i<m and j>-1:
            # print(i,j,m,n)
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i=i+1
        return False