class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        i=0
        l = len(nums)
        while i<l and j<l:
            nums[i],num = nums[j],nums[j]
            # print(i,j,num)
            j_init = j
            while j+1<l and num==nums[j+1]:
                j+=1
            if i+1<l and j_init!=j:
                i+=1
                nums[i]=num
            j+=1
            i+=1
            # print(nums,i,j)
        return i