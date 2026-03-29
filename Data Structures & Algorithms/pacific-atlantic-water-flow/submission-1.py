class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []
        M = len(heights)-1
        N = len(heights[0])-1

        memoPacific = {}
        def dfsPacific(m,n):
            if (m,n) in memoPacific:
                return memoPacific[(m,n)]
            
            # Check if we're at Pacific border
            if (0<=m<=M and n==0) or (m==0 and 0<=n<=N):
                memoPacific[(m,n)] = True
                return True
            
            memoPacific[(m,n)] = False  # Assume False initially
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                new_m, new_n = m + dr, n + dc
                if (0 <= new_m <= M and 0 <= new_n <= N and 
                    heights[m][n] >= heights[new_m][new_n]):
                    if dfsPacific(new_m, new_n):
                        memoPacific[(m,n)] = True
                        return True
            
            return False
        
        memoAtlantic = {}
        def dfsAtlantic(m,n):
            if (m,n) in memoAtlantic:
                return memoAtlantic[(m,n)]
            
            # Check if we're at Atlantic border
            if (0<=m<=M and n==N) or (m==M and 0<=n<=N):
                memoAtlantic[(m,n)] = True
                return True
            
            memoAtlantic[(m,n)] = False  # Assume False initially
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                new_m, new_n = m + dr, n + dc
                if (0 <= new_m <= M and 0 <= new_n <= N and 
                    heights[m][n] >= heights[new_m][new_n]):
                    if dfsAtlantic(new_m, new_n):
                        memoAtlantic[(m,n)] = True
                        return True
            
            return False

        for m in range(M+1):
            for n in range(N+1):
                if dfsPacific(m,n) and dfsAtlantic(m,n):
                    ret.append([m,n])
        
        return ret
