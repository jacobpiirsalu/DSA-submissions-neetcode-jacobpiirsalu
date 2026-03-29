class Solution:
    memo = {}
    def tribonacci(self, n: int) -> int:
        if n==1:
            return 1
        if n<=0:
            return 0
        if n-3 not in self.memo:
            self.memo[n-3] = self.tribonacci(n-3)
        if n-2 not in self.memo:
            self.memo[n-2] = self.tribonacci(n-2)
        if n-1 not in self.memo:
            self.memo[n-1] = self.tribonacci(n-1)
        return self.memo[n-3] + self.memo[n-2] + self.memo[n-1]