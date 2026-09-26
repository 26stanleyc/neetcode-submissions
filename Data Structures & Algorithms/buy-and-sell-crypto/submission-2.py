class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            profit = max(profit, prices[i] - mini)
        if(profit < 0):
            return 0
        else:
            return profit