# dfs(r,c) = dfs(r+1,c) + dfs(r, c+1)
# dyn programming solution -> bottom up
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        r,c = m-1, n-1
        for r in range(m-1, -1, -1):
            #print(f'r:{r}')
            for c in range(n-1, -1, -1):
                #print(f'c:{c}')
                pt = (r,c)
                down = cache.get((r+1,c),0)
                right = cache.get((r,c+1),0)
                if pt == (m-1,n-1): cache[pt] = 1
                else: cache[pt] = right + down

                
        
        print(cache)
        return cache[(0,0)]

            
                


        