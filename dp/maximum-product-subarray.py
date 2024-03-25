class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mn,mx = 1,1
        for n in nums:
            temp = n*mx
            mx = max(n*mn,n*mx,n)
            mn = min(n,temp,n*mn)
            res = max(res,mx)
        return res