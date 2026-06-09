# Last updated: 6/9/2026, 12:39:54 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        
4        ROWS = len(board)
5        COLS = len(board[0])
6
7        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
8
9        def dfs(row, col, sub):
10            if "".join(sub) == word:
11                return True
12
13            val = word[len(sub)]
14            for cord in directions:
15                x, y = cord
16                newX = x + row
17                newY = y + col
18
19                if 0 <= newX < ROWS and 0 <= newY < COLS and board[newX][newY] == val and board[newX][newY] != "#":
20                    sub.append(val)
21                    board[newX][newY] = "#"
22                    if dfs(newX, newY, sub):
23                        return True
24                    sub.pop()
25                    board[newX][newY] = val
26
27            return False
28        
29        for r in range(ROWS):
30            for c in range(COLS):
31                if board[r][c] == word[0]:
32                    board[r][c] = "#"
33                    if dfs(r, c, [word[0]]):
34                        return True
35                    board[r][c] = word[0]
36        return False
37
38