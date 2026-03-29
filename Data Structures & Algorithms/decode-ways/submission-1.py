class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i>len(s):
                return 0
            if i==len(s):
                return 1
            
            res = 0 
            if 1<= int(s[i]) <= 26:
                res = dfs(i+1)
            
            if int(s[i])!= 0 and 1<= int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            return res

        
        return dfs(0)