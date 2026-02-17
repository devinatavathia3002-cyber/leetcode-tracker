# Last updated: 2/16/2026, 11:23:06 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        
4        count = {}
5        maxf = 0
6
7        l = 0
8        res = 0
9
10        for r in range(len(s)):
11            count[s[r]] = (count.get(s[r], 0) + 1)
12            maxf = max(maxf, count[s[r]])
13
14            while (r - l + 1) - maxf > k:
15                count[s[l]] -= 1
16                l += 1
17            
18            res = max(res, (r - l + 1))
19
20        return res