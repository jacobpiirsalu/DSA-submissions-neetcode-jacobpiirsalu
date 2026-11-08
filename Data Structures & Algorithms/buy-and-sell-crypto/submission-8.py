class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxP = 0, 1, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = max(prices[r]-prices[l], maxP)
                r+=1
            else:
                l+=1
                r=l+1
        return maxP