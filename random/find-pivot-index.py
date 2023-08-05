class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=[0]*len(nums)
        l[0]=nums[0]
        r=[0]*len(nums)
        r[len(nums)-1]=nums[-1]
        for i in range(1,len(nums)):
            # print(i,nums[i],l)
            l[i]=l[i-1]+nums[i]
        for i in range(len(nums)-2,-1,-1):
            r[i]=r[i+1]+nums[i]
        for i in range(len(nums)):
            if(l[i]-nums[i]==r[i]-nums[i]):
                return i
        return -1
            
        