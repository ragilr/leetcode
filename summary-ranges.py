class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret=[]
        i = 0
        while i < len(nums):
            a=nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            b=nums[i]
            if(a!=b):
                ret.append(str(a)+"->"+str(b))
            else:
                ret.append(str(a))
            i+=1
        return ret
