class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i+1, buying) #if we do nothing this day
            if buying:
                buy = dfs(i+1, not buying) - prices[i] #if we buy this day, we must either sell or do nothing the next day
                return max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i] #if we hold this day, we can either sell and incurr cooldown of 1 day or do nothing 
                return max(sell, cooldown)
            
        return dfs(0, True)