class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)-1
        N = len(heights[0])-1


        validPacific = set()
        def pacific(m,n):
            if (m,n) in validPacific:
                return

            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            validPacific.add((m,n))
            for dm,dn in directions:
                if 0<=m+dm<=M and 0<=n+dn<=N and heights[m+dm][n+dn] - heights[m][n] >= 0:
                    pacific(m+dm, n+dn)
                elif (0<=m+dm<=M and n+dn==0) or (m+dm==0 and 0<=n+dn<=N):
                    pacific(m+dm, n+dn)
        pacific(0,0)

        validAtlantic = set()
        def atlantic(m,n):
            if (m,n) in validAtlantic:
                return

            directions=[(1,0),(0,1),(-1,0),(0,-1)]
            validAtlantic.add((m,n))
            for dm,dn in directions:
                if 0<=m+dm<=M and 0<=n+dn<=N and heights[m+dm][n+dn] - heights[m][n] >= 0:
                    atlantic(m+dm, n+dn)
                elif (0<=m+dm<=M and n+dn==N) or (m+dm==M and 0<=n+dn<=N):
                    atlantic(m+dm, n+dn)
        atlantic(M,N)

        return list(validPacific.intersection(validAtlantic))
        

            
            
            
            

