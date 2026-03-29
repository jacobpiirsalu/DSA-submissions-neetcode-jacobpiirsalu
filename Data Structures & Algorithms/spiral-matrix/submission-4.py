class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        
        ret = []
        def recurse(xBound, yBound):
            print(xBound, yBound)
            if len(ret) >= m*n: return
            if xBound[0]-xBound[1]==0 and yBound[0]-yBound[1]==0:
                ret.append(matrix[yBound[0]][xBound[0]])
            
            
            #right
            for x in range(xBound[0], xBound[1]+1):
                if len(ret) >= m*n: return
                ret.append(matrix[yBound[0]][x])

            
            #down
            for y in range(yBound[0]+1,yBound[1]+1):
                if len(ret) >= m*n: return
                ret.append(matrix[y][xBound[1]])

            
            #left
            for x in range(xBound[1]-1, xBound[0]-1, -1):
                if len(ret) >= m*n: return
                ret.append(matrix[yBound[1]][x])

            if len(ret) >= m*n: return
            #up
            for y in range(yBound[1]-1, yBound[0], -1):
                if len(ret) >= m*n: return
                ret.append(matrix[y][xBound[0]])

            #recurse
            if len(ret) >= m*n: return            
            recurse((xBound[0]+1, xBound[1]-1),
            (yBound[0]+1, yBound[1]-1)
            )

            

        recurse(
            (0,n-1),
            (0,m-1)
        )
        return ret

        