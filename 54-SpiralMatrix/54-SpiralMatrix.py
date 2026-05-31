# Last updated: 5/30/2026, 9:53:49 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        
4        ROWS = len(matrix)
5        COLS = len(matrix[0])
6
7        l, r = 0, COLS - 1
8        top, bottom = 0, ROWS - 1
9
10        res = []
11
12        while l <= r and top <= bottom:
13
14            # get top row
15            for i in range(l, r + 1):
16                res.append(matrix[top][i])
17            top += 1
18
19            # get rightmost column
20            for i in range(top, bottom + 1):
21                res.append(matrix[i][r])
22            r -= 1
23
24            if not (l <= r and top <= bottom):
25                break
26                
27            # get bottom row
28            for i in range(r, l - 1, -1):
29                res.append(matrix[bottom][i])
30            bottom -= 1
31
32            # get leftmost column
33            for i in range(bottom, top - 1, -1):
34                res.append(matrix[i][l])
35            l += 1
36
37        return res