class Solution:
    #brute force: DFS
    #time complexity is O(2^(m+n))
    #space complexity (max depth of recursive call)
    #is equal to the max path length, O(m+n)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        def dfs(r,c) -> int:
            if 0<=r<m and 0<=c<n: #in bounds  
                if obstacleGrid[r][c] == 1:
                    return 0
                if r==m-1 and c==n-1: return 1
                
                if dp[r][c] == 0: #not yet visited
                    dp[r][c] = dfs(r+1, c) + dfs(r, c+1)
                return dp[r][c]

            #out of bounds
            return 0
        
        return dfs(0,0)