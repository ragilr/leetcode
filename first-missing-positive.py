class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)

        i = 0
        while i<l:
            j = nums[i]-1
            if 0<=j<l and nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1
        for i in range(l):
            if nums[i]!=i+1:
                return i+1
        return l+1