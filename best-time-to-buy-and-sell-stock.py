class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     low=[0]*len(prices)
    #     high=[0]*len(prices)
    #     l=prices[0]
    #     for i in range(len(prices)):
    #         if prices[i]<l:
    #             l=prices[i]
    #         low[i]=l
    #     h=prices[-1]
    #     for i in range(len(prices)-1,-1,-1):
    #         if prices[i]>h:
    #             h=prices[i]
    #         high[i]=h
    #     m=0
    #     for i in range(len(prices)):
    #         if m < high[i]-low[i]:
    #             m=high[i]-low[i]    
    #     return m
    
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        m = 0
        for p in prices:
            if p < l:
                l=p
            if p-l >m:
                m=p-l
        return m
