class Solution:
    cache = {} #n (numSteps) : numOfWays
    def climbStairs(self, n: int) -> int:
        if n<=1: return 1
        
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.cache[n]        