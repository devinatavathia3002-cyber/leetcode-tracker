# Last updated: 2/17/2026, 10:42:26 PM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        rows, cols = len(rooms), len(rooms[0])
4        visited = set()
5        q = deque()
6
7        for r in range(rows):
8            for c in range(cols):
9                if rooms[r][c] == 0:
10                    visited.add((r, c))
11                    q.append([r, c])
12        
13        def addCell(r, c):
14            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and rooms[r][c] != -1:
15                visited.add((r, c))
16                q.append([r, c])
17            else:
18                return
19        
20        steps = 0
21        while q:
22            for i in range(len(q)):
23                row, col = q.popleft()
24                rooms[row][col] = steps
25
26                addCell(row + 1, col)
27                addCell(row - 1, col)
28                addCell(row, col + 1)
29                addCell(row, col - 1)
30
31            steps += 1
32
33
34