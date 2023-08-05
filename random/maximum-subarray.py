class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = curr_max = nums[0]
        for i in range(1,len(nums)):
            curr_max = max(curr_max+nums[i],nums[i])
            m = max(curr_max,m)
        return m
        
        