# Last updated: 5/29/2026, 12:20:34 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        reversed_n = 0
4
5        for _ in range(32):
6            reversed_n = reversed_n << 1
7            last = n & 1
8            n = n >> 1
9            reversed_n = reversed_n | last
10
11        return reversed_n