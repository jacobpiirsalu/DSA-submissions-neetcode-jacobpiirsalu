class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #strategy: binary search, first to find which row it's in
        # then normal bin search for within that row

        L=0
        R=len(matrix)-1
        M=(L+R)//2

        while L<=R:
            print(f'L: {L}, R: {R}, M: {M}')
            if target<matrix[M][0]:
                R=M-1
            elif target>matrix[M][-1]:
                L=M+1
            elif matrix[M][0] <=target<= matrix[M][-1]:
                break
            M=(L+R)//2
        if L>R: return False

        l=0
        r=len(matrix[M])-1
        m=(l+r)//2

        while l<=r:
            if target<matrix[M][m]:
                r=m-1
            elif target>matrix[M][m]:
                l=m+1
            else:
                return True
            m=(l+r)//2
        return False
        