# Last updated: 5/23/2026, 9:09:51 PM
1class Solution:
2    def numSquares(self, n: int) -> int:
3
4        dp = {} # dp cache
5    
6        def recurse(total):
7            if total == n:
8                return 0
9            if total > n:
10                return float("inf")
11            if total in dp:
12                return dp[total]
13            
14            res = n
15            for i in range(1, int(n ** 0.5) + 1):
16                new = i * i
17                res = min(res, recurse(total + new) + 1)
18            dp[total] = res
19            return res
20        
21        return recurse(0)
22
23            