class Solution:
    def numDecodings(self, s: str) -> int:
        count=0
        def dfs(i):
            nonlocal count
            if i>len(s):
                return
            if i==len(s):
                count+=1
                return
            

            if 1<= int(s[i]) <= 26:
                dfs(i+1)
            
            if int(s[i])!= 0 and 1<= int(s[i:i+2]) <= 26:
                dfs(i+2)

            return

        dfs(0)
        return count