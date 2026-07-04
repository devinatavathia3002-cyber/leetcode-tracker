# Last updated: 7/3/2026, 6:16:32 PM
1class Solution:
2    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
3        ROWS = len(dungeon)
4        COLS = len(dungeon[0])
5
6        dp = [[float("inf")] * COLS for _ in range(ROWS)]
7
8        def findMin(oldCell, r, c):
9            minimum = float('inf')
10            if 0 <= r < ROWS and 0 <= c < COLS:
11                curr = dp[r][c]
12                minimum = max(1, curr - oldCell)
13
14            return minimum
15        
16        for r in range(ROWS - 1, -1, -1):
17            for c in range(COLS - 1, -1, -1):
18                curr = dungeon[r][c]
19
20                right = findMin(curr, r + 1, c)
21                down = findMin(curr, r, c + 1)
22
23                res = min(right, down)
24                if res == float("inf"):
25                    if curr > 0:
26                        res = 1
27                    else:
28                        res = (1 - curr)
29
30                dp[r][c] = res
31
32        return dp[0][0]