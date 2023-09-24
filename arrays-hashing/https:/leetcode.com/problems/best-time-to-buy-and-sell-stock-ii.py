class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy = prices[0]
    #     profit = 0
    #     prices.append(-1)
    #     for i in range(1,len(prices)):
    #         price = prices[i]
    #         if price < prices[i-1]:
    #             if prices[i-1]-buy > 0:
    #                 profit += (prices[i-1]-buy)
    #             buy = price
    #     return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                    profit += (prices[i]-prices[i-1])
        return profit