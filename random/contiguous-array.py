class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        l = 0
        s = 0
        d[s]=0
        for i in range(len(nums)):
            if nums[i]==0:
                s -= 1
            else:
                s += 1
            if s in d:
                l = max(l,i+1-d[s])
            else:
                d[s]=i+1
        return l
        