class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        h = 0
        for n in nums:
            if n-1 not in nums:
                c = n
                s = 1
                while c+1 in nums:
                    c+=1
                    s+=1
                h = max(h,s)
        return h
                