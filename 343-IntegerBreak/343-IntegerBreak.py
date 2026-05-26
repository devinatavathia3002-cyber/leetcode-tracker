# Last updated: 5/25/2026, 5:07:25 PM
1class Solution:
2    def integerBreak(self, n: int) -> int:
3        
4        # recursive solution
5
6        # def recurse(target):
7        #     if target == 0:
8        #         return 1
9        #     if target < 0:
10        #         return 0
11
12        #     res = 1
13        #     for i in range(2, target + 1):
14        #         remaining = target - i
15        #         res = max(res, recurse(remaining) * i)
16        #     return res
17        
18        # return recurse(n)
19
20        # bottom-up dp
21        
22        dp = [1] * (n + 1)
23        for i in range(2, n + 1):
24            dp[i] = (i if i != n else 1)
25            for j in range(2, n):
26                dp[i] = max(dp[i], dp[j] * dp[i - j])
27
28        return dp[n]
29        