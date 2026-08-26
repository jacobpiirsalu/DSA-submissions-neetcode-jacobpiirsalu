class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return 0
        L,R = 0,1
        max_profit = 0

        while L < len(prices): #could be split into recursion, maybe DP to save on computation, but prices length is small
            while R<len(prices):
                max_profit=max(max_profit, prices[R]-prices[L])
                R+=1
            L+=1
            R=L+1
        return max_profit

