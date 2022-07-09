class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        m=float('-inf')
        i=0
        d=dict()
        s=0
        j=0
        # while i<len(nums):
        #     while j < len(nums) and nums[j] not in d:
        #         d[nums[j]]=j
        #         s+=nums[j]
        #         j+=1
        #     m=max(s,m)
        #     if j==len(nums):
        #         break
        #     while i<=j and nums[j] in d:
        #         s-=nums[i]
        #         del d[nums[i]]
        #         i+=1
        #     # for k in list(d.keys()):
        #     #     if d[k]<=p:
        #     #         del d[k]
        #     #         s-=k
        #     i=j
        
        while i<len(nums) and j<len(nums):
            if nums[j] not in d:
                s+=nums[j]
                d[nums[j]]=j
                j+=1
            else:
                del d[nums[i]]
                s-=nums[i]
                i+=1
            m=max(s,m)

        return m
                
                
            
        