class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        cc_cnt = 0
        visited = set()
        
        def dfs(u, prev):
            if u in visited:
                return

            visited.add(u)
            for v in adj[u]:
                if v == prev:
                    continue
                dfs(v, u)

        for i in range(n):
            if i not in visited:
                cc_cnt += 1
                dfs(i, -1)
        
        return cc_cnt