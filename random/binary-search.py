class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin(nums, 0, len(nums)-1, target)
    
    def bin(self,nums: List[int], start: int, end: int, target: int):
        # print(start,str(int((start+end)/2)),end)
        if(start>end):
            return -1
        mid = int((start+end)/2)
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            return self.bin(nums,start,mid-1,target)
        else:
            return self.bin(nums,mid+1,end,target)