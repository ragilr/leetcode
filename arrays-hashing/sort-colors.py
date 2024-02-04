class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        j = 0
        for i in range(3):
            n = count[i]
            while n:
                nums[j]=i
                n=n-1
                j+=1
        return nums
