import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = pow(2,len(nums))
        ret = [[]]
        for i in range(1,n):
            arr = self.genArray(i)
            r = []
            for a in arr:
                r.append(nums[a])
            ret.append(r)
        return ret
    
    
    def genArray(self,i:int) -> List[int]:
        j=1
        c=0
        ret = []
        while j<i+1:
            # print(j,i,j&i)
            if j&i==j:
                ret.append(c)
            c+=1
            j=j*2
        print(i,ret)
        return ret
        