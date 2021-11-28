class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums)==0):
            return [-1,-1]
        left = self.binSearch(0,len(nums)-1,nums,target,-1)
        if(left==-1):
            return[-1,-1]
        right = self.binSearch(0,len(nums)-1,nums,target,1)
        return [left,right]
        
        
        
    
    def binSearch(self,l:int,h:int,nums: List[int], target: int, side:int) -> int:
        # print(l,h,side)
        if(l>h or l<0 or h>=len(nums)):
            return -1
        mid = int((l+h)/2)
        number = nums[mid]
        
        if(number==target):
            find = mid
            if(side > 0 and mid<len(nums)-1 and nums[mid+1]==target):
                find = max(mid,self.binSearch(mid+1,h,nums,target,side))
            elif(side < 0 and mid>0 and nums[mid-1]==target):
                find = min(mid,self.binSearch(l,mid-1,nums,target,side))
            if(side<0 and find==-1):
                find = mid
            return find
        elif(number>target):
            return self.binSearch(l,mid-1,nums,target,side)
        else:
            return self.binSearch(mid+1,h,nums,target,side)
        