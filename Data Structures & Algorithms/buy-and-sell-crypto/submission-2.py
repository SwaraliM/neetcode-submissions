class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        minBuyPrice = prices[0]

        for sellPrice in prices:
            res = max(res, sellPrice - minBuyPrice)
            minBuyPrice = min(minBuyPrice, sellPrice)
        
        return res
