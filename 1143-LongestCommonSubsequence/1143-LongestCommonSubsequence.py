# Last updated: 5/11/2026, 11:08:01 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
4
5        for i in range(len(text1) - 1, - 1, -1):
6            for j in range(len(text2) - 1, -1, -1):
7                if text1[i] == text2[j]:
8                    dp[i][j] = 1 + dp[i + 1][j + 1]
9                else:
10                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
11        
12        return dp[0][0]