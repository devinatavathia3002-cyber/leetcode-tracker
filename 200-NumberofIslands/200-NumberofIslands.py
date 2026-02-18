# Last updated: 2/17/2026, 11:27:16 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        
4        islands = 0
5        # visited = set()
6
7        rows, cols = len(grid), len(grid[0])
8        
9        def checkVal(r, c, q):
10            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
11                print((r, c))
12                q.append([r, c])
13                grid[r][c] = "0"
14        
15        def bfs(r, c):
16            q = deque()
17            q.append([r, c])
18
19            while q: 
20                for i in range(len(q)):
21                    r, c = q.popleft()
22
23                    checkVal(r + 1, c, q)
24                    checkVal(r - 1, c, q)
25                    checkVal(r, c + 1, q)
26                    checkVal(r, c - 1, q)
27
28        for r in range(rows):
29            for c in range(cols):
30                if grid[r][c] == "1":
31                    bfs(r, c)
32                    islands += 1
33
34
35        return islands