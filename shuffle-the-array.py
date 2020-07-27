class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = [None]*2*n
        for i in range(n):
            ret[i*2]=nums[i] #x
            ret[i*2+1]=nums[i+n]
        return ret
            
        
