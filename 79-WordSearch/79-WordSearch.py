# Last updated: 4/11/2026, 10:38:35 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3
4        def dfs(row, col, index):
5
6            if index >= len(word):
7                return True
8            
9            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
10                return False
11            
12            if board[row][col] != word[index]:
13                return False
14            
15            board[row][col] = '#'
16            
17            found = (dfs(row + 1, col, index + 1) or
18                    dfs(row - 1, col, index + 1) or
19                    dfs(row, col + 1, index + 1) or
20                    dfs(row, col - 1, index + 1))
21            
22            board[row][col] = word[index]
23            return found
24        
25        for r in range(len(board)):
26            for c in range(len(board[0])):
27                if board[r][c] == word[0]:
28                    if dfs(r, c, 0):
29                        return True
30        return False
31        
32