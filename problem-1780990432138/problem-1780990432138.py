# Last updated: 6/9/2026, 12:33:52 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        
4        ROWS = len(board)
5        COLS = len(board[0])
6
7        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
8        visited = set()
9
10        def dfs(row, col, sub):
11            if "".join(sub) == word:
12                return True
13
14            val = word[len(sub)]
15            for cord in directions:
16                x, y = cord
17                newX = x + row
18                newY = y + col
19
20                if 0 <= newX < ROWS and 0 <= newY < COLS and board[newX][newY] == val and (newX, newY) not in visited:
21                    sub.append(val)
22                    visited.add((newX, newY))
23                    if dfs(newX, newY, sub):
24                        return True
25                    sub.pop()
26                    visited.remove((newX, newY))
27            
28            return False
29        
30        for r in range(ROWS):
31            for c in range(COLS):
32                if board[r][c] == word[0]:
33                    visited.add((r, c))
34                    if dfs(r, c, [word[0]]):
35                        return True
36                    visited.remove((r, c))
37        return False
38
39