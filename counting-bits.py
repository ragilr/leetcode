class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[]
        for i in range(n+1):
            c = 0
            while i:
                i=i&(i-1)
                c+=1
            ret.append(c)
        return ret
        