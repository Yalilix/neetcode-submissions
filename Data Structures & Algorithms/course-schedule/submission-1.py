class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for u, v in prerequisites:
            adj_list[u].append(v)

        visited = set()

        def dfs(u):
            if not adj_list[u]:
                return True

            if u in visited:
                return False

            visited.add(u)
            for v in adj_list[u]:
                if not dfs(v): return False
            visited.remove(u)
            adj_list[u] = []

            return True
        
        for u in range(numCourses):
            if not dfs(u): return False

        return True

