class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        s=0
        mx = 0
        for r in range(len(nums)):
            s+=nums[r]
            while l<len(nums) and nums[r]*(r-l+1)>s+k:
                s=s-nums[l]
                l=l+1
            mx=max(mx,r-l+1)
        return mx