# Last updated: 7/20/2026, 7:26:05 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        # dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
4
5        # for i in range(len(text1) - 1, - 1, -1):
6        #     for j in range(len(text2) - 1, -1, -1):
7        #         if text1[i] == text2[j]:
8        #             dp[i][j] = 1 + dp[i + 1][j + 1]
9        #         else:
10        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
11        
12        # return dp[0][0]
13
14        n, m = len(text1), len(text2)
15        dp = [[0] * (m + 1) for _ in range(n + 1)]
16
17        for i in range(1, n + 1):
18            for j in range(1, m + 1):
19                curr1, curr2 = text1[i - 1], text2[j - 1]
20                if curr1 == curr2:
21                    dp[i][j] = 1 + dp[i - 1][j - 1]
22                else:
23                    dp[i][j] = max(
24                        dp[i - 1][j],
25                        dp[i][j - 1],
26                        dp[i - 1][j - 1]
27                    )
28        
29        return dp[n][m]