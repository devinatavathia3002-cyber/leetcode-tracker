# Last updated: 4/15/2026, 10:58:32 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        rows = len(board)
4        cols = len(board[0])
5        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
6
7        def dfs(r, c):
8            if (r < 0 or c < 0 or r >= rows 
9                or c >= cols or board[r][c] == 'X'
10                or board[r][c] == 'S'):
11
12                return
13            
14            board[r][c] = 'S'
15
16            for num in directions:
17                x, y = num
18                dfs(r + x, c + y)
19        
20
21        for r in range(rows):
22            if board[r][0] == 'O':
23                dfs(r, 0)
24            if board[r][cols - 1] == 'O':
25                dfs(r, cols - 1)
26        
27        for c in range(cols):
28            if board[0][c] == 'O':
29                dfs(0, c)
30            if board[rows - 1][c] == 'O':
31                dfs(rows - 1, c)
32        
33        for r in range(rows):
34            for c in range(cols):
35                if board[r][c] == 'S':
36                    board[r][c] = 'O'
37                elif board[r][c] == 'O':
38                    board[r][c] = 'X'
39                else:
40                    continue