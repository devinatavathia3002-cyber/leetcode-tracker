# Last updated: 5/31/2026, 1:58:12 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        
4        ROWS = len(matrix)
5        COLS = len(matrix[0])
6
7        topCol = False
8        topRow = False
9
10        # mark first row/first col with 0
11        for r in range(ROWS):
12            for c in range(COLS):
13                if matrix[r][c] == 0:
14                    if c == 0:
15                        topCol = True
16                    if r == 0:
17                        topRow = True
18                    else:
19                        matrix[0][c] = 0
20                        matrix[r][0] = 0
21        
22        # update grid with 0s
23        for r in range(1, ROWS):
24            for c in range(1, COLS):
25                if matrix[0][c] == 0 or matrix[r][0] == 0:
26                    matrix[r][c] = 0
27        
28        # check boolean
29        if topCol:
30            for r in range(ROWS):
31                matrix[r][0] = 0
32        
33        # check top row
34        if topRow:
35            for c in range(COLS):
36                matrix[0][c] = 0
37        
38        