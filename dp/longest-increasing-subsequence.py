class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = {}
        # def dfs(prev,i,curr_len):
        #     if i == len(nums):
        #         return curr_len
        #     # if (prev,i,curr_len) in dp:
        #         # return dp[(prev,i,curr_len)]
        #     n = float('inf') if prev == -1 else nums[prev]
        #     ret = dfs(prev,i+1,curr_len)
        #     if nums[i]>n:
        #         ret = max(ret, dfs(i,i+1,curr_len+1))
        #     else:
        #         ret = max(ret, dfs(i,i+1,1))     
        #     # dp[(prev,i,curr_len)] = ret      
        #     return ret            
        # return dfs(-1,0,1)

        dp = [1]*len(nums)
        print(nums)
        for i in range(len(nums)-1,-1,-1):
            m = 1
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    m = max(m,dp[j]+1)
            dp[i] = m
        return max(dp)

        