class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.ksum(nums,target,4)
    
    
    def ksum(self,nums:List[int], target:int, k:int) -> List[List[int]]:
        res = []
        if not nums:
            return res
        
        avg = target // k
        
        if avg < nums[0] or nums[-1] < avg:
            return res
        
        if k == 2:
            return self.twoSum(nums,target)
        
        for i in range(len(nums)):
            if i==0 or nums[i-1] != nums[i]:
                for subset in self.ksum(nums[i+1:],target-nums[i],k-1):
                    res.append([nums[i]]+subset)
        return res
    
    def twoSum(self, nums:List[int], target: int) -> List[List[int]]:
        l=0
        h=len(nums)-1
        res = []
        while l<h:
            s = nums[l]+nums[h]
            if (l>0 and nums[l-1]==nums[l]) or s < target:
                l+=1
            elif s > target or (h < len(nums)-1 and nums[h] ==nums[h+1]):
                h-=1
            else:
                res.append([nums[l],nums[h]])
                l+=1
                h-=1
        return res
            