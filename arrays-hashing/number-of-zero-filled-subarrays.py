class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # l = len(nums)
        ret = count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                count = 0
            ret += count
        return ret
            