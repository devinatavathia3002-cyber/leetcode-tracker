# Last updated: 5/17/2026, 1:44:54 PM
1# class Solution:
2#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
3#         directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
4#         ROWS = len(matrix)
5#         COLS = len(matrix[0])
6#         def dfs(r, c, prev):
7#             if r >= ROWS or c >= COLS or r < 0 or c < 0:
8#                 return 0
9#             curr = matrix[r][c]
10
11#             # how to get max from here
12#             if curr > prev:
13#                 best = 0
14#                 for coord in directions:
15#                     x, y = coord
16#                     best = max(best, dfs(x + r, y + c, matrix[r][c]) + 1)
17#                 return best
18#             else:
19#                 return 0
20
21#         output = 0
22#         for i in range(ROWS):
23#             for j in range(COLS):
24#                 output = max(output, dfs(i, j, -1))
25#         return output
26
27# dp solution:
28
29class Solution:
30    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
31        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
32        ROWS = len(matrix)
33        COLS = len(matrix[0])
34        dp = {}
35
36        def dfs(r, c, prev):
37            if r >= ROWS or c >= COLS or r < 0 or c < 0:
38                return 0
39            curr = matrix[r][c]
40            if curr > prev:
41                if (r, c) in dp:
42                    return dp[(r, c)]
43
44            # how to get max from here
45            if curr > prev:
46                best = 0
47                for coord in directions:
48                    x, y = coord
49                    best = max(best, dfs(x + r, y + c, matrix[r][c]) + 1)
50                dp[(r, c)] = best
51                return best
52            
53            return 0
54                
55        for i in range(ROWS):
56            for j in range(COLS):
57                dfs(i, j, -1)
58        return max(dp.values())