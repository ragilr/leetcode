class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        z = 0
        for n in nums:
            if n!=0:
                p *= n
            else:
                z += 1
        if z > 1:
            return [0]*len(nums)
        ret = []
        for n in nums:
            if z==0:
                ret.append(p//n)
            elif n==0:
                ret.append(p)
            else:
                ret.append(0)
        return ret