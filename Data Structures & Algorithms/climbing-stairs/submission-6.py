# bottom up dynamic programming solution
class Solution:
    cache = {} #n (numSteps) : numOfWays
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        #cS(n) = cS(n-1) + cS(n-2)
        #cS(0) = 1
        #cS(1) = 1
        dp = [1,1] 

        incr = 1
        while incr<n:
            tmp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = tmp
            incr+=1
        return dp[1]
