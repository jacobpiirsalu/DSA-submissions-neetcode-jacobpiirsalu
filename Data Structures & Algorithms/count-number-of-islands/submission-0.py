class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()

        def dfs(r: int, c:int):
            if r<0 or c<0:
                return
            if r>=ROWS or c>=COLS:
                return
            if grid[r][c] == "0":
                return

            kv = (r,c)    
            # value must be 1:
            if kv not in visited:
                visited.add((r,c))
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    
                    islands +=1
                    dfs(r,c) 
                    #expand from all directions connected to this point
                    #adding the connected 1's to visited
        return islands


        