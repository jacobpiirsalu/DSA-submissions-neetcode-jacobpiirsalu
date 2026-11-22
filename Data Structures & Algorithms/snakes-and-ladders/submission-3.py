import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)

        sq2coord = {}
        for row in range(len(board)):
            for col in range(len(board)):
                if (n-row) % 2 != 0:
                      sq = (n - (row + 1)) * n + (col + 1)
                else:
                    sq = (n - (row + 1)) * n + (n - col)
                sq2coord[sq] = [row,col]

        #print(sq2coord)
        def replaceWSnkOrLddr(sq: int):
            row,col = sq2coord[sq]
            if board[row][col] != -1:
                return board[row][col]
            else: return sq

        #minPath = float('inf')
        visited = set()

        #BFS
        queue = collections.deque()
        queue.appendleft([1,0]) #start

        while queue:
            print(queue)
            currPnt, cost = queue.pop()
            nei = [currPnt+x for x in range(1,7)]
            #print(nei)
            nei = filter(lambda x: x <= n*n ,nei)
            nei = list(map(replaceWSnkOrLddr, nei))
            print(nei)
            nei = list(filter(lambda x: x != currPnt and x not in visited, nei))
            for ni in nei:
                if ni == n*n:
                    return cost+1

                #print([ni,cost+1])
                visited.add(ni)
                queue.appendleft([ni,cost+1])


        return -1