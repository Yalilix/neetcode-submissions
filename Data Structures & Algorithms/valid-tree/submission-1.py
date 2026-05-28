class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        node_visited = set()

        def dfs(u, prev):
            if u in visited:
                return False

            if u not in node_visited:
                node_visited.add(u)

            visited.add(u)
            for v in adj[u]:
                if prev == v:
                    continue
                if not dfs(v, u): return False
            visited.remove(u)
            return True
        
        cc_cnt = 0
        for i in range(n):
            if i not in node_visited:
                cc_cnt += 1
            if not dfs(i, -1): return False
        print(cc_cnt)
        if cc_cnt > 1:
            return False

        return True