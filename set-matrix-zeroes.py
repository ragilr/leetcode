class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = matrix
        m = len(mat)
        n = len(mat[0])
        r = mat[0][0]
        c = mat[0][0]
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0 and i!=0  and j!=0):
                    # print("changed")
                    mat[0][j]=0
                    mat[i][0]=0
                elif (mat[i][j]==0 and i==0):
                    r = 0
                elif (mat[i][j]==0 and j==0):
                    c = 0
                # print(i,j,mat)
        # print (mat,r,c)
        for i in range(1,m):
            if(mat[i][0]==0):
                for j in range(1,n):
                    mat[i][j]=0
        for j in range(1,n):
            if(mat[0][j]==0):
                for i in range(1,m):
                    mat[i][j]=0
            
        if r==0:
            for i in range(n):
                    mat[0][i]=0
        if c == 0:
            for j in range(m):
                    mat[j][0]=0