class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(r,c):
            if r>=len(grid) or c>=len(grid[0]): return 0
            if r<0 or c<0: return 0
            if grid[r][c] == 0: return 0
            
            # value is not 0 or out of bounds
            area = 1
            grid[r][c] = 0
            area+=dfs(r+1, c)
            area+=dfs(r-1, c)
            area+=dfs(r, c-1)
            area+=dfs(r,c+1)
            return area



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islandArea = dfs(r,c)
                    if islandArea > maxArea: maxArea = islandArea
        
        return maxArea
        