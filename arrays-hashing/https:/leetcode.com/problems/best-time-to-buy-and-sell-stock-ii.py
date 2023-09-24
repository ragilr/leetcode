class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        sold = set()
        for i in range(1,len(prices)):
            price = prices[i]
            if price < prices[i-1]:
                if prices[i-1]-buy > 0:
                    profit += (prices[i-1]-buy)
                    sold.add(i)
                buy = price
        if len(prices)-1 not in sold and buy<prices[-1]:
            profit = profit+prices[-1]-buy
        return profit