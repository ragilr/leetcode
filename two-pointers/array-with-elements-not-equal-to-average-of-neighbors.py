class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        ret = [-1]*l
        i = 0
        j = 0
        while j<l:
            ret[j]=nums[i]
            j+=2
            i+=1
        j=1
        while j<l and i<l:
            ret[j]=nums[i]
            j+=2
            i+=1
        return ret
