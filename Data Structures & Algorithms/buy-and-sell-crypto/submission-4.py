class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1: return 0
        L,R,maxP=0,0,0
        while R<len(prices)-1:
            R+=1
            maxP = max(maxP, prices[R]-prices[L])
            if prices[R] < prices[L]:
                L=R
        return maxP
