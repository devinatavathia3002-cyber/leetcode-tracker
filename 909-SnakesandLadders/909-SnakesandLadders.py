# Last updated: 8/1/2026, 7:18:26 PM
1class Solution:
2    def snakesAndLadders(self, board: List[List[int]]) -> int:
3        ROWS = len(board)
4        COLS = len(board[0])
5
6        def intToPos(num):
7            r = (num - 1) // ROWS
8            c = (num - 1) % ROWS
9            if r % 2:
10                c = ROWS - 1 - c
11            r = ROWS - 1 - r
12            return (r, c)
13        
14        q = deque()
15        moves = 0
16
17        q.append(1)
18        row, col = intToPos(1)
19        board[row][col] = 0
20
21        while q:
22            length = len(q)
23            for i in range(length):
24                val = q.popleft()
25                for j in range(1, 7):
26                    newVal = val + j
27                    if newVal > ROWS * ROWS:
28                        break
29                    r, c = intToPos(newVal)
30                    if board[r][c] == 0:
31                        continue
32                    if board[r][c] != -1:
33                        newVal = board[r][c]
34                    if newVal == (ROWS * ROWS):
35                        return moves + 1
36
37                    q.append(newVal)
38                    board[r][c] = 0
39
40            moves += 1
41        
42        return -1