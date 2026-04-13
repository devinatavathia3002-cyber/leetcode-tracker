# Last updated: 4/13/2026, 12:35:46 AM
1class Solution:
2    def islandPerimeter(self, grid: List[List[int]]) -> int:
3        
4        rows = len(grid)
5        cols = len(grid[0])
6        visited = set()
7
8        def dfs(r, c):
9            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
10                return 1
11
12            if (r, c) in visited:
13                return 0
14            
15            visited.add((r, c))
16            total = (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
17            return total
18
19        for r in range(rows):
20            for c in range(cols):
21                if grid[r][c] == 1:
22                    return dfs(r, c)
23        return 0
24