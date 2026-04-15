# Last updated: 4/14/2026, 11:33:50 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        output = 0
6        fresh = 0
7        q = deque()
8
9        for r in range(rows):
10            for c in range(cols):
11                if grid[r][c] == 2:
12                    q.append((r, c))
13                if grid[r][c] == 1:
14                    fresh += 1
15                    
16        while q and fresh > 0:
17            for val in range(len(q)):
18                row, col = q.popleft()
19                if row > 0:
20                    if grid[row - 1][col] == 1:
21                        fresh -= 1
22                        grid[row - 1][col] = 2
23                        q.append((row - 1, col))
24                if row < rows - 1:
25                    if grid[row + 1][col] == 1:
26                        fresh -= 1
27                        grid[row + 1][col] = 2
28                        q.append((row + 1, col))
29                if col > 0:
30                    if grid[row][col - 1] == 1:
31                        fresh -= 1
32                        grid[row][col - 1] = 2
33                        q.append((row, col - 1))
34                if col < cols - 1:
35                    if grid[row][col + 1] == 1:
36                        fresh -= 1
37                        grid[row][col + 1] = 2
38                        q.append((row, col + 1))
39            output += 1
40                    
41        return output if fresh == 0 else -1
42
43