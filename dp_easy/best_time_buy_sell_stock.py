import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minprice = sys.maxsize
        for i in range(0, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if prices[i] - minprice > max_profit:
                max_profit =  prices[i] - minprice
        return max_profit
        