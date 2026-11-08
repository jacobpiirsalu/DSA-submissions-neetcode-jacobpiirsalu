class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minStart = 101
        for i in range(len(prices)):
            minStart = min(prices[i], minStart)
            maxProfit = max(maxProfit, prices[i]-minStart)
        return maxProfit