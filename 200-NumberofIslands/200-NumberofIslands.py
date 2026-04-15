# Last updated: 4/14/2026, 8:47:49 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        output = 0
6
7        def dfs(r, c):
8            if r < 0 or c < 0 or r >= rows or c >= cols:
9                return
10            
11            if grid[r][c] == "1":
12                grid[r][c] = "."
13
14                dfs(r + 1, c)
15                dfs(r - 1, c)
16                dfs(r, c + 1)
17                dfs(r, c - 1)
18            
19            else:
20                return
21
22        for r in range(rows):
23            for c in range(cols):
24                if grid[r][c] == "1":
25                    dfs(r, c)
26                    output += 1
27        
28        return output
29
30
31
32        