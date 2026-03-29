from collections import deque
class Solution:
    # find the idxs of the rotten fruits. Each layer of the BFS will be 1 minute
    # at each layer, add the rotten fruit to the queue, pop each one for that minute
    # and add their children

    #if there are still fresh fruit at the end, return -1, otherwise return the number of minutes (layers) of bfs




    # def addNeighborsToQueue(self, node: (int, int), q, grid: List[List[int]]):
    #     neighbors = [[-1,0], [1,0], [0,1], [0,-1]]
    #     for dx,dy in neighbors:
    #         r = node[0] + dx
    #         c = node[1] + dy

    #         if 0 <= r < len(grid) and 0 <= c < len(grid) and grid[r][c] == 1:
    #             grid[r][c] == 2
    #             q.append((r,c))





    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if it's not a 2d matrix or empty, return:
        if not grid or not grid[0]:
            return -1
        
    
        #left is front of queue, right is back
        q = deque()
        #add rotten fruits to the queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        
        mins = 0
        while q:
            print(mins)
            print(q)
            
            mins+=1
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                print(node)
                #rottenFruits = self.addNeighborsToQueue(node, q, grid)
                neighbors = [[-1,0], [1,0], [0,1], [0,-1]]
                for dx,dy in neighbors:
                    r = node[0] + dx
                    c = node[1] + dy

                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
            if not q: mins-=1
        
        #if there are still fresh fruit, return -1
        for row in grid:
            if 1 in row:
                return -1
        return mins # there's aways 1 extra minute in the loop for the final check at the end

        
        










        