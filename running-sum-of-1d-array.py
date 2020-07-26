class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run = [None]*len(nums)
        # print run
        prev = 0
        length = len(nums)
        for i in range(length):
            run[i]=prev+nums[i]
            prev=run[i]
        return run
