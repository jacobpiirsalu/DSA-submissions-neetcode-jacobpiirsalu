from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #bfs, use a queue to queue in valid neighbor nodes, then pop each layer and add their children
        if not grid or not grid[0] or grid[0][0]==1:
            return -1
        n=len(grid)

        q = deque()
        #visited = set()

        q.append((0,0,1))
        grid[0][0] = 1
        #visited.add((0,0))
        
        while q:
            lenQ = len(q)
            for i in range(lenQ):

                vertex = q.popleft()
                
                if vertex[0] == n-1 and vertex[1] == n-1: 
                    return vertex[2]

                nebrs = [[1,0],[-1,0],[0,1],[1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
                for dr,dc in nebrs:
                    r = vertex[0] + dr
                    c = vertex[1] + dc
                    l = vertex[2]
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        # add this node to the queue, it's valid
                        q.append((r,c,l+1))
                        # we've visited this node, so make its value 1
                        grid[r][c] = 1
        return -1

        