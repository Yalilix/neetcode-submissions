class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(u, prev):
            if u in visited:
                return False

            visited.add(u)
            for v in adj[u]:
                if prev == v:
                    continue
                if not dfs(v, u): return False
            return True
        
        return dfs(0, -1) and n == len(visited)