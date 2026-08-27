# Last updated: 8/26/2026, 5:34:51 PM
1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        s = s + s
5        alt1, alt2 = "", ""
6        diff1, diff2 = 0, 0
7        res = len(s)
8
9        for i in range(len(s)):
10            if i%2:
11                alt1 += "1"
12                alt2 += "0"
13            else:
14                alt1 += "0"
15                alt2 += "1"
16        
17        l = 0
18        for r in range(len(s)):
19            curr = s[r]
20            if curr != alt1[r]:
21                diff1 += 1
22            if curr != alt2[r]:
23                diff2 += 1
24
25            if (r - l + 1) > n:
26                if s[l] != alt1[l]:
27                    diff1 -= 1
28                if s[l] != alt2[l]:
29                    diff2 -= 1
30                l += 1
31
32            if (r - l + 1) == n:
33                res = min(res, diff1, diff2)
34        
35        return res