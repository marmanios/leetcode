class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                p = max(price-lowest,p)
        return p