class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0]*n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        #move will be valid
        #just have to check if there is a winner, and who?

        #update the matrix
        self.board[row][col] = player
        
        #DFS from their current move, do DFS for THIS player, if length is n then THIS PLAYER is winner
        dirs = [[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,-1),(1,1)],[(-1,1),(1,-1)]]

        def dfs(srow: int, scol:int, d: (int,int), visited: set((int,int))) -> int:
            x,y = d
            nei = (x+srow, y+scol)
            if nei not in visited and 0<=nei[0]<self.n and 0<=nei[1]<self.n and self.board[nei[0]][nei[1]] == player:
                visited.add(nei)
                return 1+dfs(nei[0],nei[1],d, visited)
            return 0

        for d in dirs:
            d1,d2 = d
            if dfs(row,col,d1, set((row,col))) + dfs(row,col,d2, set((row,col))) + 1 == self.n:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
