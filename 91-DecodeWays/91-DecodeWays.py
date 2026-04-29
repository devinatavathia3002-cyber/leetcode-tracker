# Last updated: 4/28/2026, 11:24:56 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        
4        dp, dp1, dp2 = 0, 1, 0
5        length = len(s)
6
7        for i in range(length - 1, -1, -1):
8            if s[i] == "0":
9                dp = 0
10            else:
11                dp = dp1
12            
13            if i < length - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
14                dp += dp2
15            
16            dp, dp1, dp2 = 0, dp, dp1
17
18
19        return dp1