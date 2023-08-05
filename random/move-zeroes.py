class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count=0
        nzp=0
        # print(nums,nums[0],nzp,count)
        while(i<len(nums)):
            if(nums[i]==0):
                count+=1
                # print(nums,nums[i],nzp,count)
                i+=1
                continue
            if(nzp>-1):
                nums[nzp]=nums[i]
            nzp+=1
            # print(nums,nums[i],nzp,count)
            i+=1
        i=len(nums)-1
        while(count>0):
            nums[i]=0
            i-=1
            count-=1
            
            
            