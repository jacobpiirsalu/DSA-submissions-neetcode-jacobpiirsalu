class TicTacToe:

    def __init__(self, n: int):
        #self.board = [[0]*n for _ in range(n)]
        self.N = n
        self.sumR = [0]*n
        self.sumC = [0]*n
        self.sumDiag, self.sumADiag = 0,0
        

    def move(self, row: int, col: int, player: int) -> int:
        #update move
        incr = 1 if player==1 else -1
        self.sumR[row]+=incr
        self.sumC[col]+=incr
        if row==col: self.sumDiag+=incr
        if row+col==self.N-1: self.sumADiag+=incr

        #win condition
        if (
            abs(self.sumDiag)==self.N or abs(self.sumADiag)==self.N 
            or any(abs(r)==self.N for r in self.sumR) 
            or any(abs(c)==self.N for c in self.sumC)
        ):
            return player
        else: return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
