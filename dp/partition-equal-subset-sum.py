class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2:
            return False
        tot = tot/2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            nextDp = set(dp)
            for t in dp:
                nextDp.add(t+nums[i])
            dp = nextDp
        return tot in dp