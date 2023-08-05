class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSearch(0,len(nums)-1,nums,target)
        
        
    def binSearch(self, l:int,h:int,nums: List[int], target: int) -> int:
        if(l>h):
            return l
        mid = int((l+h)/2)
        number = nums[mid]
        if(number==target):
            return mid
        elif(number>target):
            return self.binSearch(l,mid-1,nums,target)
        else:
            return self.binSearch(mid+1,h,nums,target)
        