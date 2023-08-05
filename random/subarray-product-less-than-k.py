class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # n=0
        # for i in range(len(nums)):
        #     p=1
        #     for j in range(i,len(nums)):
        #         p*=nums[j]
        #         if p>=k:
        #             break
        #         n+=1
        p=1
        sub=0
        i,j=0,0
        # if k==0:
        #      return 0
        # while i < len(nums) and j<len(nums):
        #     n=0
        #     while p<k and j<len(nums):
        #         print("stuck here1",i,j,p,nums[i:j])
        #         p*=nums[j]
        #         n+=1
        #         j+=1
        #     sub+=(n*(n+1))//2
        #     while p>=k and i<j:
        #         p/=nums[i]
        #         i+=1
        #         print("stuck here2",i,j,p,nums[i:j])
        #     print("stuck here3",i,j,p,nums[i:j])
        while j<len(nums):
            p=p*nums[j]
            while i<=j and p>=k:
                p/=nums[i]
                i+=1
            sub+=j-i+1
            j+=1
        return sub
        