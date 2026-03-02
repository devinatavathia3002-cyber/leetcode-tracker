# Last updated: 3/1/2026, 9:25:31 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        
4        # first, search through rows
5        rows = len(matrix)
6        cols = len(matrix[0])
7
8        l = 0
9        r = rows - 1
10        c = cols - 1
11
12        rowIndex = 0
13
14        while l <= r:
15            m = ((r - l) // 2) + l
16            curr = matrix[m]
17
18            if target >= matrix[m][0] and target <= matrix[m][c]:
19                rowIndex = m
20                break
21            elif target < matrix[m][0]:
22                r = m - 1
23            else:
24                l = m + 1
25        
26        l = 0
27        r = len(matrix[rowIndex]) - 1
28
29        while l <= r:
30            m = ((r - l) // 2) + l
31            curr = matrix[rowIndex]
32            
33            if target == curr[m]:
34                return True
35            elif target < curr[m]:
36                r = m - 1
37            else:
38                l = m + 1
39        
40        return False
41