class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        start = 0
        end = 1
        maxProfit = 0

        while end < n:
            if prices[start] < prices[end]:
                profit = prices[end] - prices[start]
                maxProfit = max(maxProfit, profit)
            else:
                start = end # move to after the window.

            end += 1
        return maxProfit