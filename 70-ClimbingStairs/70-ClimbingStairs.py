# Last updated: 5/25/2026, 6:35:01 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [0] * (n + 1)
4        dp[0] = 1
5        dp[1] = 1
6
7        for i in range(2, n + 1):
8            # 1 or 2
9            dp[i] += (dp[i - 1] + dp[i - 2])
10        
11        return dp[n]
12
13        # for 3 --> [1, 1, 2, 3]