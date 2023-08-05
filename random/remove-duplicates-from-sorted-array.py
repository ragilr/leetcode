class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        if len(nums)<=1:
            return len(nums)
        while j<len(nums):
            while j<len(nums) and nums[i]==nums[j]:
                j+=1
            i+=1
            if j<len(nums) and i<len(nums):
                nums[i]=nums[j]
        return i
        