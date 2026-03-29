class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for to,fromm in prerequisites:
            adj[fromm].append(to)
            
        visited = set()
        def dfs(fromm):
            if fromm in visited:
                return False
            if adj[fromm] == []:
                return True
            visited.add(fromm)
            for node in adj[fromm]:
                if not dfs(node):
                    return False
            visited.remove(fromm)
            adj[fromm] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


