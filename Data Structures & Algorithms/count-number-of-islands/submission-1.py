class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()

        def bfs(r,c):
            queue = collections.deque()
            
            queue.append((r,c))
            while queue:
                r,c = queue.popleft()
                drc = [(r+1, c), (r-1,c), (r,c-1), (r,c+1)]
                for d in drc:
                    if 0<=d[0]<len(grid) and 0<=d[1]<len(grid[0]) and grid[d[0]][d[1]] == '1' and d not in visited:
                        visited.add(d)
                        queue.append(d)
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    numIslands+=1
                    visited.add((r,c))
                    bfs(r,c) #incr islands + update visited
        return numIslands


