class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None]*(len(s)+2)
        def dfs(i):
            if i>len(s):
                memo[i] = 0
                return memo[i]
            if i==len(s):
                memo[i] = 1
                return memo[i]
            
            
            if not memo[i]:
                if 1<= int(s[i]) <= 26:
                    memo[i] = dfs(i+1)
                
                if int(s[i])!= 0 and 1<= int(s[i:i+2]) <= 26:
                    memo[i] += dfs(i+2)
                if not memo[i]: memo[i] = 0

            return memo[i]

        
        return dfs(0)