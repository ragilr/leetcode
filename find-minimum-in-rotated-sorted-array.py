class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findMinBin(l,h,nums):
            print(nums)
            print(l,h,nums[l],nums[h])
            m = (l+h)//2
            if nums[m]>nums[(m+1)%len(nums)]:
                return nums[(m+1)%len(nums)]
            if nums[m-1]>nums[m]:
                return nums[m]
            if nums[l]>nums[m]:
                return findMinBin(l,m-1,nums)
            else:
                return findMinBin(m+1,h,nums)
        if len(nums)==1:
            return nums[0]
        return findMinBin(0,len(nums)-1,nums)

        