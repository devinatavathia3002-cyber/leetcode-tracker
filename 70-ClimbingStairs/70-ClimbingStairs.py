# Last updated: 4/26/2026, 7:42:25 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        one, two = 1, 1
5
6        for i in range(n - 1):
7            temp = one
8            one += two
9            two = temp
10        
11        return one