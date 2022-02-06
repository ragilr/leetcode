class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=2
        i=2
        while i<len(nums):
            if nums[i-1]==nums[i] and nums[i-1]==nums[i-2]:
                while i<len(nums) and nums[i]==nums[i-1]:
                    i=i+1
                if nums[j-1]<=nums[j] and not (nums[j]==nums[j-1] and nums[j-1]==nums[j-2]):
                    j+=1
            if i<len(nums) and j<len(nums):
                nums[j]=nums[i]
                j+=1
            print(i,j,nums)
            # j+=1
            i+=1
        return j