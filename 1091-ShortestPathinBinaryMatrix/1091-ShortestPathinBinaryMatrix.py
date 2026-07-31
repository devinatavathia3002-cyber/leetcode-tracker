# Last updated: 7/30/2026, 6:09:46 PM
1class Solution:
2    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
3        ROWS = len(grid)
4        COLS = len(grid[0])
5
6        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
7
8        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
9            return -1
10
11        q = deque()
12        q.append((0, 0))
13        grid[0][0] = 1
14        count = 1
15
16        while q:
17            length = len(q)
18            for i in range(length):
19                row, col = q.popleft()
20                if row == ROWS - 1 and col == COLS - 1:
21                    return count
22                else:
23                    for dir in directions:
24                        x, y = dir
25                        newR, newC = row + x, col + y
26                        if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 0:
27                            q.append((newR, newC))
28                            grid[newR][newC] = 1
29            count += 1
30
31        return -1