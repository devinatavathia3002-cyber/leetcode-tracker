# Last updated: 3/4/2026, 11:21:21 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        
4        # edge case
5        if t == "":
6            return ""
7
8        tMap = [0] * 128
9        sMap = [0] * 128
10        
11        length = len(set(t))
12        have = 0
13
14        shortestLen = float("infinity")
15        substring = ""
16
17
18        for letter in t:
19            tMap[ord(letter) - ord('a')] += 1
20        
21        l, r = 0, 0
22
23        while r < len(s):
24            curr = s[r]
25            sMap[ord(curr) - ord('a')] += 1
26
27            if sMap[ord(curr) - ord('a')] == tMap[ord(curr) - ord('a')]:
28                have += 1
29            
30            while have == length:
31                shortestLen = min(shortestLen, r - l + 1)
32                if shortestLen == (r - l + 1):
33                    substring = s[l:r + 1]
34                
35                curr = s[l]
36                sMap[ord(curr) - ord('a')] -= 1
37                if sMap[ord(curr) - ord('a')] < tMap[ord(curr) - ord('a')]:
38                    have -= 1
39                l += 1
40            
41            r += 1
42        
43        return substring
44