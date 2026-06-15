# Last updated: 6/14/2026, 5:11:53 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        
4        # dfs traversal 
5        ROWS = len(grid)
6        COLS = len(grid[0])
7
8        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
9        output = 0
10
11        def dfs(r, c):
12            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
13                grid[r][c] = "0"
14                for cord in directions:
15                    x, y = cord
16                    newR = x + r
17                    newC = y + c
18                    dfs(newR, newC)
19
20        for r in range(ROWS):
21            for c in range(COLS):
22                if grid[r][c] == "1":
23                    dfs(r, c)
24                    output += 1
25
26        return output