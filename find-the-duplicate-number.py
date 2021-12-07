class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = t = nums[0]
        l=len(nums)
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        t= nums[0]
        while(h!=t):
            t = nums[t]
            h = nums[h]
        return h