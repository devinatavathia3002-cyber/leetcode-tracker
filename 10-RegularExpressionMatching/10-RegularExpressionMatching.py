# Last updated: 5/20/2026, 8:58:28 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        
4        lenS = len(s)
5        lenP = len(p)
6
7        def recurse(l, r):
8            if l == lenS and r == lenP:
9                return True
10            if r == lenP:
11                return False
12            
13            if l == lenS:
14                if r < lenP - 1 and p[r + 1] == "*":
15                    return recurse(l, r + 2)
16                return False
17            
18            if r < lenP - 1 and p[r + 1] == "*":
19                # take or not take
20                if s[l] != p[r] and p[r] != ".":
21                    return recurse(l, r + 2)
22                else:
23                    return recurse(l + 1, r) or recurse(l, r + 2)
24            
25            elif s[l] == p[r] or p[r] == ".":
26                return recurse(l + 1, r + 1)
27            
28            else:
29                return False
30        
31        return recurse(0, 0)
32
33