# Last updated: 5/11/2026, 8:44:00 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        oldRow = [1] * (n + 1)
4
5        while m > 1:
6            newRow = [0] * (n + 1)
7            for i in range(n - 1, -1, -1):
8                newRow[i] = oldRow[i] + newRow[i + 1]
9            oldRow = newRow
10            m -= 1
11        
12        return oldRow[0]
13