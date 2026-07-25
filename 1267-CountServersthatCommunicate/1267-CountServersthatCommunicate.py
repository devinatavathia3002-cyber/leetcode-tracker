# Last updated: 7/25/2026, 11:23:01 AM
1class Solution:
2    def countServers(self, grid: List[List[int]]) -> int:
3        ROWS, COLS = len(grid), len(grid[0])
4        row_cnt = [0] * ROWS
5        col_cnt = [0] * COLS
6
7        for r in range(ROWS):
8            for c in range(COLS):
9                if grid[r][c] == 1:
10                    row_cnt[r] += 1
11                    col_cnt[c] += 1
12
13        res = 0
14        for r in range(ROWS):
15            for c in range(COLS):
16                if grid[r][c] and max(row_cnt[r], col_cnt[c]) > 1:
17                    res += 1
18
19        return res