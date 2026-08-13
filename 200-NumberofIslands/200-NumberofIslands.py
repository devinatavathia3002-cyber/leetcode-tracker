# Last updated: 8/13/2026, 3:21:40 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        # can solve with dfs or bfs
4        ROWS = len(grid)
5        COLS = len(grid[0])
6
7        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
8        ct = 0
9
10        def dfs(r, c):
11            if grid[r][c] == '0':
12                return
13            else:
14                grid[r][c] = '0'
15                for dir in directions:
16                    x, y = dir
17                    newR, newC = x + r, c + y
18                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == '1':
19                        dfs(newR, newC)
20
21        for r in range(ROWS):
22            for c in range(COLS):
23                if grid[r][c] == '1':
24                    dfs(r, c)
25                    ct += 1
26        return ct
27
28