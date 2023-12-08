class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0
        for j in nums:
            if j == 0:
                return 0
            elif j < 0:
                negative += 1
        if negative & 1:
            return -1
        return 1