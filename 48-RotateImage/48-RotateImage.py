# Last updated: 5/30/2026, 9:17:02 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        l, r = 0, len(matrix) - 1
4
5        while l < r:
6            for i in range(r - l):
7                topLeft = matrix[l][l + i]
8                matrix[l][l + i] = matrix[r - i][l]
9                matrix[r - i][l] = matrix[r][r - i]
10                matrix[r][r - i] = matrix[l + i][r]
11                matrix[l + i][r] = topLeft
12            l += 1
13            r -= 1