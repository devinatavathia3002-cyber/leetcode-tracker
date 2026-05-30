# Last updated: 5/29/2026, 6:54:14 PM
1class Solution:
2    def getSum(self, a: int, b: int) -> int:
3        mask = 0xffffffff
4
5        while b != 0:
6            tmp = (a & b) << 1
7            a = (a ^ b) & mask
8            b = tmp & mask
9
10        if a > mask // 2:
11            return ~(a ^ mask)
12        else:
13            return a