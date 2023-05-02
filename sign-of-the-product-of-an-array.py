class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zero = False
        negative = 0
        for j in nums:
            if j == 0:
                zero = True
            elif j < 0:
                negative = negative ^ 1
        # print("negative",negative)
        if zero:
            return 0
        if not negative:
            return 1
        return -1