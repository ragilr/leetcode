import math

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        clen = len(cost)+1
        minCost = [math.inf]*(clen)
        minCost[0]=minCost[1]=0
        for i in range(2,clen):
            minCost[i]=min((minCost[i-2]+cost[i-2]),(minCost[i-1]+cost[i-1]))
        return minCost[clen-1]