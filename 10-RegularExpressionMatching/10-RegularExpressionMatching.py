# Last updated: 5/20/2026, 9:13:46 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        
4        lenS = len(s)
5        lenP = len(p)
6        cache = {}
7
8        def recurse(l, r):
9            if l == lenS and r == lenP:
10                return True
11            if (l, r) in cache:
12                return cache[(l, r)]
13
14            if r == lenP:
15                cache[(l, r)] = False
16            elif l == lenS:
17                if r < lenP - 1 and p[r + 1] == "*":
18                    return recurse(l, r + 2)
19                cache[(l, r)] = False
20            
21            elif r < lenP - 1 and p[r + 1] == "*":
22                if s[l] != p[r] and p[r] != ".":
23                    cache[(l, r)] = recurse(l, r + 2)
24                else:
25                    cache[(l, r)] = (recurse(l + 1, r) or recurse(l, r + 2))
26            
27            elif s[l] == p[r] or p[r] == ".":
28                cache[(l, r)] = recurse(l + 1, r + 1)
29            
30            else:
31                cache[(l, r)] = False
32            
33            return cache[(l, r)]
34        
35        return recurse(0, 0)
36
37