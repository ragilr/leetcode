class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def matBin(li,hi,lj,hj,m,target):
            print(li,hi,lj,hj)
            if li>hi or lj>hj:
                return False
            r = len(m)
            c = len(m[0])
            i = (li+hi)//2
            j = (lj+hj)//2
            print(li,hi,lj,hj,i,j,m[i][j])
            if m[i][j]==target:
                return True
            if m[i][0]<=target and target<=m[i][c-1]:
                hi=li=i
                if target<m[i][j]:
                    hj=j-1
                else:
                    lj=j+1
            if m[i][j]>target and m[i][0]>target:
                hi=i-1
                # print("hi=i-1")
            if m[i][j]<target and m[i][c-1]<target:
                li=i+1
                # print("li=i+1")
            return matBin(li,hi,lj,hj,m,target)
        return matBin(0,len(matrix)-1,0,len(matrix[0])-1,matrix,target)

                

