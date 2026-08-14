# Last updated: 8/14/2026, 1:40:57 PM
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
14        mins = 0
15        while q:
16            mins += 1
17            length = len(q)
18            for i in range(length):
19                row, col = q.popleft()
20                for dir in directions:
21                    x, y = dir
22                    newR = x + row
23                    newC = y + col
24                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 1:
25                        q.append((newR, newC))
26                        grid[newR][newC] = 2
27
28        for r in range(ROWS):
29            for c in range(COLS):
30                if grid[r][c] == 1:
31                    return -1
32        
33        return mins - 1 if mins > 0 else 0