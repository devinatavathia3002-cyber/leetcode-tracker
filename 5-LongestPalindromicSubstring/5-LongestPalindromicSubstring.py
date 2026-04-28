# Last updated: 4/28/2026, 12:09:28 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        
4        longest, index = 0, 0
5        length = len(s)
6        grid = [[False for _ in range(length)] for _ in range(length)]
7        
8        for r in range(length - 1, -1, -1):
9            for c in range(r, length):
10                if s[r] == s[c] and ((c - r <= 2) or grid[r + 1][c - 1]):
11                    grid[r][c] = True
12                    longest = max(longest, c - r + 1)
13                    if longest == (c - r + 1):
14                        index = r
15
16        return s[index:index + longest]