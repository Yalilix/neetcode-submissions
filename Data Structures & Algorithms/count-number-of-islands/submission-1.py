class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        islands = 0
        visited = set()

        def dfs(r, c):
            nonlocal islands
            if (r < 0 or c < 0 or
                r >= n or c >= m):
                return 

            if grid[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return


        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i,j)

        return islands