class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for to,fromm in prerequisites:
            adj[fromm].append(to)
            
        
        memo = {}
        def dfs(fromm, visited):
            if fromm in visited:
                memo[fromm] = False
                return False
            if fromm in memo:
                return memo[fromm]
            visited.add(fromm)
            for node in adj[fromm]:
                if not dfs(node, visited):
                    memo[fromm] = False
                    visited.remove(fromm)
                    return False
            visited.remove(fromm)
            memo[fromm] = True
            return True

        for i in range(numCourses):
            visited = set()
            if not dfs(i, visited):
                return False
        return True


