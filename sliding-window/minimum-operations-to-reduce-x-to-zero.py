class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = 0
        target = sum(nums)-x
        ret = -1
        l=0
        for r,n in enumerate(nums):
            s+=n
            while l<=r and s>target:
                s-=nums[l]
                l+=1
            if s==target:
                ret = max(ret,r-l+1)
        return len(nums)-ret if ret != -1 else -1