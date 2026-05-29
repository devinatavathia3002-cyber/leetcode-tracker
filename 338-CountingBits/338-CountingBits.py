# Last updated: 5/28/2026, 8:04:58 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3        dp = [0] * (n + 1)
4        offset = 1
5
6        for index in range(1, n + 1):
7            if offset * 2 == index:
8                offset = index
9            dp[index] = 1 + dp[index - offset]
10
11        return dp