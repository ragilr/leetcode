class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        res = []
        p = 0
        for i in range(len(nums)-k+1):
            if i == 0:
                for j in range(k-1):
                    d[nums[j]]=d.get(nums[j],0)+1
                d[p]=1
            d[p]-=1
            if d[p]==0:
                del d[p]
            p = nums[i]
            d[nums[i+k-1]] = d.get(nums[i+k-1],0)+1
            res.append(len(d))
        return res