class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = price if price < min_price else min_price
            profit = price - min_price
            max_profit = profit if profit > max_profit else max_profit
        
        return max_profit
            
        return max_profit