class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefSum = 0
        prefMod = {0:-1}
        for i,n in enumerate(nums):
            prefSum+=n
            mod = prefSum%k
            if mod not in prefMod:
                prefMod[mod] = i
            elif i-prefMod[mod]>=2:
                return True
        return False
