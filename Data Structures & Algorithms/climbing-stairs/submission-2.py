class Solution:
    def climbStairs(self, n: int) -> int:
        #base case
        # if n<=1:
        #     return 1
        if n==1 or n==2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

        