# Last updated: 5/20/2026, 10:11:32 PM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3
4        if n == 0:
5            return 0
6        if n == 1 or n == 2:
7            return 1
8        
9        num1, num2, num3 = 0, 1, 1
10
11        for i in range(3, n + 1):
12            new = num1 + num2 + num3
13            num1, num2, num3 = num2, num3, new
14
15        return num3