# 2 islands
# need to get from one island to the next
# how many water bits do we flip to connect the 2 islands
# land is only connected by up,down,left, right (no diagonal connections)
#import collections
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #flip one of the islands to 2s
        startVal = [0,0]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    #print(startVal)
                    startVal = [r,c]

        def bfsFlip(startIdx):
            queue = collections.deque()
            r,c = startIdx
            queue.appendleft([r,c])
            while queue:
                r,c = queue.pop()
                grid[r][c] = 2
                nei = [[r+1,c],[r-1,c],[r,c-1],[r,c+1]]
                nei=list(filter(lambda x: 0<=x[0]<n and 0<=x[1]<n and grid[x[0]][x[1]]==1,nei))
                for nxt in nei:
                    #print(nxt)
                    queue.appendleft(nxt)

        #print(startVal)
        bfsFlip(startVal)
        #print('done bfs flip')

        #lenGrid = [[-1]*n for _ in range(n)]
        minPath = float('inf')
        visited = {}
        def bfsPath(startwPath):
            nonlocal minPath
            nonlocal visited
            startIdx, dist = startwPath
            r,c = startIdx

            queue = collections.deque()
            queue.appendleft([startIdx,dist])
            while queue:
                #print(queue[-1])
                currIdx,currD = queue.pop()
                r,c = currIdx
                if currD >= minPath:
                    continue
                if (r,c) in visited and currD >= visited[(r,c)]:
                    continue

                visited[(r,c)] = currD
                nei = [[r+1,c],[r-1,c],[r,c-1],[r,c+1]]
                finished = list(filter(lambda x: 0<=x[0]<n and 0<=x[1]<n and grid[x[0]][x[1]]==1,nei))
                #print(finished)
                if finished:
                    minPath = min(minPath, currD)

                nei=list(filter(lambda x: 0<=x[0]<n and 0<=x[1]<n and grid[x[0]][x[1]]==0,nei))
                #print(nei)
                for nxt in nei:
                    queue.appendleft([nxt,currD+1])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    #print('bfs path: ' + str([r,c]))
                    bfsPath( [[r,c],0] )
        return minPath