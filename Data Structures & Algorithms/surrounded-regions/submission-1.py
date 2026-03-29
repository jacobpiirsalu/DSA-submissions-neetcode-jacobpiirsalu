class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #if any given O is NOT connected to a border O, then it's considered "surrounded"
        R = len(board)
        C = len(board[0])

        def dfs(r,c):
            # if the neighbor is O, then set the curr value to # and then call dfs on the neighbor
            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            if r>=R or c>=C or r<0 or c<0 or board[r][c] != "O":
                return
            
            board[r][c] = "#"
            for dr, dc in neighbors:
                dfs(r+dr, c+dc)


        for r in range(R):
            for c in range(C):
                if r!=0 and r!=R-1 and c!=0 and c!=C-1:
                    continue
                else: #at one of the border cells
                    dfs(r,c) #changes connected cells to "#"

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

        return

        