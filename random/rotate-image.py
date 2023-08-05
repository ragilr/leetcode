class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        self.transpose(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)
    def transpose(self,mat:List[List[int]]) -> None:
        n = len(mat)
        for i in range(n):
            for j in range(i,n):
                mat[j][i],mat[i][j]=mat[i][j],mat[j][i]
        