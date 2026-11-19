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
        dirs = [[(-1,0),(1,0)],[(0,-1),(0,1)]]

        def dfs(srow: int, scol:int, d: (int,int)) -> int:
            x,y = d
            nei = (x+srow, y+scol)
            if 0<=nei[0]<self.n and 0<=nei[1]<self.n and self.board[nei[0]][nei[1]] == player:
                return 1+dfs(nei[0],nei[1],d)
            return 0

        if row+col == self.n-1 or row==col:
            dirs+=[[(-1,-1),(1,1)],[(-1,1),(1,-1)]]
            print(dirs)
        for d in dirs:
            d1,d2 = d
            if dfs(row,col,d1) + dfs(row,col,d2) + 1 == self.n:
                return player
        return 0
        # inefficient bc you only need to check the diagonal IF the move is on one of the main diagonals of the board (another square will never be long enough to reach)


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
