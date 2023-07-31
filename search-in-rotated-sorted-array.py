class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        if(nums[0]>nums[-1]):
            pivot = self.findPivot(0,len(nums)-1,nums)
        print(pivot)
        # pivot = 4
        a = self.binSearch(pivot,0,len(nums)-1,nums,target)
        if a != -1:
            return self.adjustPivot(a,pivot,len(nums))
        return -1
    
    def binSearch(self, pivot:int, l:int,h:int,nums: List[int], target: int) -> int:
        if(l>h):
            return -1
        mid = int((l+h)/2)
        number = nums[self.adjustPivot(mid,pivot,len(nums))]
        if(number==target):
            return mid
        elif(number>target):
            return self.binSearch(pivot,l,mid-1,nums,target)
        else:
            return self.binSearch(pivot,mid+1,h,nums,target)
    
    def adjustPivot(self,i:int,p:int,l:int) -> int:
        return (int((i+p)%l))
    
    def findPivot(self, l:int, h:int, nums: List[int]) -> int:
        # if(l<=h):
        #     print(nums[l:h+1])
        if(l>=h or nums[l]<nums[h]):
            return
        if(h-l==1 and nums[l]>nums[h]):
            return h
        mid = int((l+h)/2)
        left = self.findPivot(l,mid,nums)
        if(left!=None):
            return left
        return self.findPivot(mid,h,nums)
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        print(nums)
        while l <= h:
            mid = (l+h)//2
            print(l,h,mid)
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<= target and target<=nums[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if target<=nums[h] and nums[mid]<=target:
                    l=mid+1
                else:
                    h=mid-1
        return -1

        
        
        
        