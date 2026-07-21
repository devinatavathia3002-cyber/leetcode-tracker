# Last updated: 7/20/2026, 6:57:23 PM
1class Solution:
2    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
3        n, m = len(str1), len(str2)
4        dp = [[0] * (m + 1) for _ in range(n + 1)]
5
6        for i in range(n + 1):
7            dp[i][0] = i
8        for j in range(m + 1):
9            dp[0][j] = j
10
11        for r in range(1, n + 1):
12            for c in range(1, m + 1):
13                curr1, curr2 = str1[r - 1], str2[c - 1]
14                if curr1 == curr2:
15                    dp[r][c] = 1 + dp[r - 1][c - 1]
16                else:
17                    dp[r][c] = min(
18                        1 + dp[r-1][c],
19                        1 + dp[r][c - 1]
20                    )
21        
22        # traceback
23        res = []
24        i, j = n, m
25
26        while i > 0 and j > 0:
27            currI, currJ = str1[i - 1], str2[j - 1]
28            if currI == currJ:
29                res.append(currI)
30                i -= 1
31                j -= 1
32            else:
33                if dp[i - 1][j] < dp[i][j - 1]:
34                    res.append(currI)
35                    i -= 1
36                else:
37                    res.append(currJ)
38                    j -= 1
39        
40        while i > 0:
41            res.append(str1[i - 1])
42            i -= 1
43        while j > 0:
44            res.append(str2[j - 1])
45            j -= 1
46
47        return "".join(reversed(res))
48