class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,l,h):
            i=l-1
            pivot=nums[h]
            for j in range(l,h):
                if nums[j]<=pivot:
                    i=i+1
                    nums[i],nums[j]=nums[j],nums[i]
            nums[i+1],nums[h]=nums[h],nums[i+1]
            return i+1
        
        def kLarge(nums,l,h,k):
            # print(nums,l,h)
            pi = partition(nums,l,h)
            if len(nums)-k==pi:
                return nums[pi]
            elif len(nums)-k>pi:
                return kLarge(nums,pi+1,h,k)
            else:
                return kLarge(nums,l,pi-1,k)
        
        return kLarge(nums,0,len(nums)-1,k)