class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        iterations = len(prices) - 1

        i = 0
        while i <= iterations:
            slice_prices = prices[i:]
            print(prices)
            buy = slice_prices[0]
            print(buy)
            sell = max(slice_prices)
            max_price = max(max_price, sell - buy)
            print(max_price)
            i += 1
        return max_price
