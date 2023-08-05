class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        l = len(index)
        ret = []
        for i in range(l):
            ret.insert(index[i],nums[i])
        return ret
