class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_val:
                min_val = price
            profit = price - min_val
            max_profit = max(max_profit,profit)

        return max_profit