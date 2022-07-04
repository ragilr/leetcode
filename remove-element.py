class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for n in nums:
            if n == val:
                c+=1
        l = len(nums)-1
        i=0
        while i<len(nums)-c:
            if nums[i]==val:
                while l>-1 and l>i and nums[l]==val:
                    l-=1
                nums[l],nums[i]=nums[i],nums[l]
            i+=1
        return len(nums)-c
            
            
                
    
                
