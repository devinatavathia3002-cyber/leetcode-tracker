# Last updated: 4/28/2026, 9:34:28 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        
4        count = 0
5        length = len(s)
6        grid = [[False for _ in range(length)] for _ in range(length)]
7
8        for r in range(length - 1, -1, -1):
9            for c in range(r, length):
10                if s[r] == s[c] and (c - r <= 2 or grid[r + 1][c - 1]):
11                    count += 1
12                    grid[r][c] = True
13
14        return count