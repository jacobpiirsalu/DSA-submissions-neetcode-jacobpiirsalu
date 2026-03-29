class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        ret = []
        
        # Use exclusive bounds: left, right, top, bottom
        left, right = 0, n
        top, bottom = 0, m
        
        while left < right and top < bottom:
            # Traverse right
            for i in range(left, right):
                ret.append(matrix[top][i])
            top += 1
            
            # Traverse down
            for i in range(top, bottom):
                ret.append(matrix[i][right - 1])
            right -= 1
            
            # Check if we're done (for single row/column cases)
            if not (left < right and top < bottom):
                break
                
            # Traverse left
            for i in range(right - 1, left - 1, -1):
                ret.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # Traverse up
            for i in range(bottom - 1, top - 1, -1):
                ret.append(matrix[i][left])
            left += 1
        
        return ret

        