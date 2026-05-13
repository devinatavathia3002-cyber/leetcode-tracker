# Last updated: 5/12/2026, 8:55:32 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        dp = [[0] * 2 for _ in range(n + 1)]
5
6        for i in range(n - 1, -1, -1):
7
8            buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]
9            cooldown = dp[i + 1][1] if i + 1 < n else 0
10            dp[i][1] = max(buy, cooldown)
11
12            sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
13            cooldown = dp[i + 1][0] if i + 1 < n else 0
14            dp[i][0] = max(sell, cooldown)
15
16        return dp[0][1]