class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for c in nums:
            count[c]+=1
        i=0
        n=count[0]
        while n>0:
            nums[i]=0
            n-=1
            i+=1
        n=count[1]
        while n>0:
            nums[i]=1
            n-=1
            i+=1
        n=count[2]
        while n>0:
            nums[i]=2
            n-=1
            i+=1
        
        
        