class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_total = 0
        for sell in prices:
            max_total = max(max_total, sell - min_buy)
            min_buy = min(min_buy, sell)
        return max_total

            

