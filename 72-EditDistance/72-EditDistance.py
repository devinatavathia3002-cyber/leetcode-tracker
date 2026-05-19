# Last updated: 5/18/2026, 8:20:48 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        
4        dp = {}
5        def recurse(i1, i2):
6            if i2 == len(word2):
7                return len(word1) - i1 # amount of deletions
8            if i1 == len(word1):
9                return len(word2) - i2 # amount of insertions
10            if (i1, i2) in dp:
11                return dp[(i1, i2)]
12
13            if word1[i1] != word2[i2]:
14                # explore 3 options with 1 + and min() function
15                dp[(i1, i2)] = min(1 + recurse(i1, i2 + 1), 
16                                   1 + recurse(i1 + 1, i2), 
17                                   1 + recurse(i1 + 1, i2 + 1))
18            else:
19                dp[(i1, i2)] = recurse(i1 + 1, i2 + 1)
20            
21            return dp[(i1, i2)]
22            
23        return recurse(0, 0)
24
25