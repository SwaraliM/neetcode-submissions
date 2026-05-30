class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyDay, sellDay = 0, 1
        res = 0
        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                profit = prices[sellDay] - prices[buyDay]
                res = max(res, profit)
            else: 
                buyDay = sellDay
            
            sellDay += 1
        
        return res
