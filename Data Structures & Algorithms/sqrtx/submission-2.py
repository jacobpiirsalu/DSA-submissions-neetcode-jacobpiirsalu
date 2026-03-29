class Solution:
    def mySqrt(self, x: int) -> int:
        if 0 <= x <= 1:
            return x//1
        dp = [0,1]
        for i in range(2,x+1):
            if dp[0]*dp[0] <= x < dp[1]*dp[1]:
                return dp[0]
            dp[0] = dp[1]
            dp[1] = i