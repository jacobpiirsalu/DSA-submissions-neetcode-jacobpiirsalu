import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        islands=0
        
        visited = set() #(r,c) coords


        def bfs(r,c):
            q = collections.deque()
            q.appendleft([r,c])
            while q:
                r,c = q.pop()
                nei = [[-1,0],[1,0],[0,1],[0,-1]]
                nei = map(lambda x: [x[0]+r, x[1]+c],nei)
                nei = list(filter(lambda x: 0<=x[0]<ROWS and 0<=x[1]<COLS and (x[0],x[1]) not in visited and grid[x[0]][x[1]]=='1',nei))
                for ni in nei:
                    q.appendleft(ni)
                    visited.add((ni[0],ni[1]))
     

        for r in range(len(grid)): #r,c the coords in the grid, NOT str
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c) #side effect:add any neighboring 1's to the visited set
                    islands+=1
        return islands

        