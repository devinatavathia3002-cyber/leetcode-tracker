# Last updated: 5/23/2026, 9:34:05 PM
1class Solution:
2    def numSquares(self, n: int) -> int:
3        # with cache
4        # dp = {} # dp cache
5    
6        # def recurse(total):
7        #     if total == n:
8        #         return 0
9        #     if total > n:
10        #         return float("inf")
11        #     if total in dp:
12        #         return dp[total]
13            
14        #     res = n
15        #     for i in range(1, int(n ** 0.5) + 1):
16        #         new = i * i
17        #         res = min(res, recurse(total + new) + 1)
18        #     dp[total] = res
19        #     return res
20        
21        # return recurse(0)
22
23        # with dp
24
25        dp = [n] * (n + 1)
26        dp[0] = 0
27
28        for i in range(1, n + 1):
29            for j in range(1, i + 1):
30                new = j * j
31                if new > i:
32                    break
33                else:
34                    dp[i] = min(dp[i], 1 + dp[i - new])
35        
36        return dp[n]
37
38            