class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        mini=-1
        minj=-1
        maxi = len(m)
        maxj = len(m[0])
        i = 0
        j = 0
        t = maxi*maxj
        ret = []
        while(t>0):
            while(j<maxj) and t>0:
                print(m[i][j])
                ret.append(m[i][j])
                t-=1
                j+=1
            j-=1  
            i+=1
            maxj-=1
            
            while i<maxi and t>0:
                print(m[i][j])
                ret.append(m[i][j])
                t-=1
                i+=1
            i-=1
            j-=1
            maxi-=1
            
            while j>minj and t>0:
                print(m[i][j])
                ret.append(m[i][j])
                j-=1
                t-=1
            mini+=1
            j+=1
            i-=1
            
            while i>mini and t>0:
                print(m[i][j])
                ret.append(m[i][j])
                i-=1
                t-=1
            minj+=1
            i+=1
            j+=1
            
        return ret