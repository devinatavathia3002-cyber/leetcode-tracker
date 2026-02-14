# Last updated: 2/14/2026, 1:11:46 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3          
4        rows = defaultdict(list)   
5        cols = defaultdict(list)
6        grid = defaultdict(list)
7
8        for r in range(0, 9):
9            for c in range(0, 9):
10                if board[r][c] == ".":
11                    continue
12                
13                val = board[r][c]
14                
15                # check rows
16                if val in rows[r]:
17                    return False
18                rows[r].append(val)
19
20                # check cols
21                if val in cols[c]:
22                    return False
23                cols[c].append(val)
24
25                # check 3x3 grid
26                currR = (r // 3)
27                currC = (c // 3)
28
29                if val in grid[(currR, currC)]:
30                    return False
31                grid[(currR, currC)].append(val)
32
33
34
35        return True