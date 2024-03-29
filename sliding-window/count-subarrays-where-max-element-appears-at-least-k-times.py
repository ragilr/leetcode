class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ret = 0
        r= 0
        f=0
        for l in range(len(nums)):             
            if l>0 and nums[l-1]==m:
                f-=1
            while f<k and r<len(nums):
                f += 1 if nums[r]==m else 0
                r+=1
            if f>=k:
                ret+=len(nums)-r+1
        return ret