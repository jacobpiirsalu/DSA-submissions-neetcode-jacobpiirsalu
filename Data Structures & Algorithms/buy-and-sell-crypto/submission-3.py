class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bc buy is always before sell, we can always set L = R
        # if R<L bc it should us another buy day we should test
        if len(prices) <=1: return 0
        
        L = 0
        R = 0
        max_profit = 0
        while R<len(prices)-1:
            R+=1
            max_profit = max(max_profit, prices[R]-prices[L])
            if prices[R]<prices[L]:
                L = R
        return max_profit
