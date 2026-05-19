# Last updated: 5/18/2026, 7:07:32 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3
4        # output = 0
5        
6        # def dfs(sIndex, tIndex):
7        #     nonlocal output
8        #     if tIndex == len(t):
9        #         output += 1
10        #         return
11        #     if sIndex == len(s):
12        #         return 
13            
14        #     if s[sIndex] != t[tIndex]:
15        #         dfs(sIndex + 1, tIndex)
16        #     else:
17        #         dfs(sIndex + 1, tIndex + 1)
18        #         dfs(sIndex + 1, tIndex)
19        
20        # dfs(0, 0)
21        # return output
22
23        # top-down memoization
24        dp = {}
25        lenS = len(s)
26        lenT = len(t)
27
28        def dfs(sIndex, tIndex):
29            if tIndex == lenT:
30                return 1
31            if sIndex == lenS:
32                return 0
33            if (sIndex, tIndex) in dp:
34                return dp[(sIndex, tIndex)]
35            
36            res = dfs(sIndex + 1, tIndex)
37            if s[sIndex] == t[tIndex]:
38                res += dfs(sIndex + 1, tIndex + 1)
39            dp[(sIndex, tIndex)] = res
40            return res
41
42        return dfs(0, 0)