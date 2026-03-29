# dfs(r,c) = dfs(r+1,c) + dfs(r, c+1)
# memoization (top down dyn programming) solution
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {} # (r,c):numPaths
        def dfs(r,c) -> int:
            if r==m-1 and c==n-1:
                return 1 #there's one combination of paths from the end to the end (0!=1)
            if 0<=r<m and 0<=c<n: #in bounds
                pt = (r,c)
                if pt not in cache:
                    cache[pt] = dfs(r+1, c) + dfs(r,c+1)
                return cache[pt]
            
            return 0

        return dfs(0,0)


        