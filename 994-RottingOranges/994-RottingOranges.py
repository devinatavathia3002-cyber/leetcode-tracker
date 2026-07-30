# Last updated: 7/29/2026, 6:26:36 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        q = deque()
4        directions = [(0, 1), (1,0), (-1, 0), (0, -1)]
5
6        ROWS = len(grid)
7        COLS = len(grid[0])
8
9        for r in range(ROWS):
10            for c in range(COLS):
11                if grid[r][c] == 2:
12                    q.append((r, c))
13        
14
15        mins = 0
16        while q:
17            mins += 1
18            length = len(q)
19            for i in range(length):
20                row, col = q.popleft()
21                for dir in directions:
22                    x, y = dir
23                    newR = x + row
24                    newC = y + col
25                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 1:
26                        q.append((newR, newC))
27                        grid[newR][newC] = 2
28
29        for r in range(ROWS):
30            for c in range(COLS):
31                if grid[r][c] == 1:
32                    return -1
33        
34        return mins - 1 if mins > 0 else 0