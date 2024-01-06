class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i],endTime[i],profit[i]))
        jobs.sort(key=lambda x:x[0])
        dp = {}
        # def findJ(target,l,h):
        #     while l<h:
        #         mid = (l+h)//2
        #         if jobs[mid][0]==target:
        #             return mid
        #         elif jobs[mid][0]>target:
        #             h=mid-1
        #         else:
        #             l=mid+1
        #     return h
                    
        def dfs(i):
            if i == len(jobs):
                return 0
            if i in dp:
                return dp[i]
            a=dfs(i+1)
            curr_endtime = jobs[i][1]
            j = bisect.bisect(jobs,(curr_endtime,-1,-1))
            b = dfs(j)+jobs[i][2]
            dp[i]=max(a,b)
            return dp[i]
    
        ret = dfs(0)
        return ret