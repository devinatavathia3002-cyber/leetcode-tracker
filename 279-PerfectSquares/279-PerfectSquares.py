# Last updated: 5/25/2026, 7:27:27 PM
1class Solution:
2    def numSquares(self, n: int) -> int:
3        
4        # recursion
5        # def recurse(total):
6        #     if total == n:
7        #         return 0
8        #     if total > n:
9        #         return float("inf")
10            
11        #     res = n
12        #     for num in range(1, n):
13        #         val = num * num
14        #         res = min(res, recurse(total + val) + 1)
15        #     return res
16
17        # return recurse(0)
18
19        # dp
20        dp = [n] * (n + 1)
21        dp[0] = 0
22        dp[1] = 1
23
24        for index in range(2, n + 1):
25            for num in range(1, int(index ** 0.5) + 1):
26                val = num * num
27                if val > index:
28                    continue
29                dp[index] = min(dp[index], dp[index - val] + 1)
30        
31        return dp[n]