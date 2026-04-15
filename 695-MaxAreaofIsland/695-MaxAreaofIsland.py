# Last updated: 4/14/2026, 9:07:55 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        
4        rows = len(grid)
5        cols = len(grid[0])
6        output = 0
7
8        def dfs(r, c):
9            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
10                return 0
11            
12            grid[r][c] = 0
13            return (dfs(r + 1, c) +
14                    dfs(r - 1, c) +
15                    dfs(r, c + 1) +
16                    dfs(r, c - 1) + 1)
17            
18
19        for r in range(rows):
20            for c in range(cols):
21                if grid[r][c] == 1:
22                    area = dfs(r, c)
23                    output = max(output, area)
24
25        return output