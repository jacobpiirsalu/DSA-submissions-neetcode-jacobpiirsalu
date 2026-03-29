class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)+1
        C = len(matrix[0])+1
        self.prefixMatrix = [[0]*C for i in range(R)]
        for r in range(1,R):
            summ=0
            for c in range(1,C):
                summ+=matrix[r-1][c-1]
                self.prefixMatrix[r][c] = summ
        
        for r in range(1,R):
            for c in range(1,C):
                self.prefixMatrix[r][c]+=self.prefixMatrix[r-1][c]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print(self.prefixMatrix)
        return self.prefixMatrix[row2+1][col2+1] - self.prefixMatrix[row1][col2+1] - self.prefixMatrix[row2+1][col1] + self.prefixMatrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)