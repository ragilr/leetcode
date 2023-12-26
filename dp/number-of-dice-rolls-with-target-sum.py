class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {(0,0):1}
        mod = 1000000007
        def dfs(n,k,t):
            if (n,t) in dp:
                return dp[(n,t)]
            if n==0 or t<=0:
                return 0
            if n*k < t:
                dp[(n,t)] = 0
                return 0
            
            x = 0
            for i in range(1,k+1):
                x = ((dfs(n-1,k,t-i))%mod+x)%mod
            dp[(n,t)] = x
            return x
        return dfs(n,k,target)
