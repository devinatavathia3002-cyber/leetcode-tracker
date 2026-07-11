# Last updated: 7/11/2026, 4:53:03 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        
4        def isValid(s, start, end):
5
6            while start <= end:
7                if s[start] != s[end]:
8                    return False
9                start += 1
10                end -= 1
11            
12            return True
13        
14
15        l = 0
16        r = len(s) - 1
17        skips = 1
18
19        while l <= r:
20
21            if s[l] != s[r] and skips > 0:
22                if isValid(s, l + 1, r):
23                    l += 1
24                elif isValid(s, l, r - 1):
25                    r -= 1
26                else:
27                    return False
28                skips -= 1
29            
30            elif s[l] != s[r]:
31                return False
32            
33            else:
34                l += 1
35                r -= 1
36        
37        return True