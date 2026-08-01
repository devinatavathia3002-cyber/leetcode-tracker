# Last updated: 8/1/2026, 12:18:19 PM
1class Solution:
2    def gameOfLife(self, board: List[List[int]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        # if converting from 0 -> 1, put a -1
7        # if converting from 1 -> 0, put a 2
8        # in the end, every cell org 1 is now 1 or more, for 0 it's 0 or less
9
10        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
11        ROWS = len(board)
12        COLS = len(board[0])
13
14        # first loop, change every cell
15        for r in range(ROWS):
16            for c in range(COLS):
17                alive = 0
18                curr = board[r][c]
19                for dir in directions:
20                    x, y = dir
21                    newR, newC = r + x, c + y
22                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and board[newR][newC] >= 1:
23                        alive += 1
24                if curr >= 1:
25                    if alive < 2 or alive > 3:
26                        board[r][c] = 2
27                else:
28                    if alive == 3:
29                        board[r][c] = -1
30        
31        # second loop, standardize all the values
32        for r in range(ROWS):
33            for c in range(COLS):
34                curr = board[r][c]
35                if curr == 2:
36                    board[r][c] = 0
37                if curr == -1:
38                    board[r][c] = 1
39        