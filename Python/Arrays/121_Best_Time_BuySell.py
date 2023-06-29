class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1  # buy:left, sell:right
        maxProfit = 0       # contains maxProfit
        # sliding window problem
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)   # update maxProfit value
            else:
                left = right
            right += 1
        return maxProfit                
