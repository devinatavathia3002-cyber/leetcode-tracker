# Last updated: 5/1/2026, 6:10:38 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        
4        dp = [False] * (len(s) + 1)
5        dp[len(s)] = True
6
7        for i in range(len(s) - 1, -1, -1):
8            for word in wordDict:
9                if dp[i]:
10                    break
11                if len(word) > len(s[i:]):
12                    continue
13                if word == s[i: len(word) + i]:
14                    dp[i] = dp[i + len(word)]
15
16        return dp[0]