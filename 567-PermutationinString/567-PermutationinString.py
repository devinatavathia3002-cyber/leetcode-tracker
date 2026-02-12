# Last updated: 2/12/2026, 12:17:10 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        
4        if len(s1) > len(s2):
5            return False
6            
7        matched = 0
8
9        s1Map = [0] * 26
10        s2Map = [0] * 26
11
12        for i in range(len(s1)):
13            s1Map[ord(s1[i]) - ord('a')] += 1
14            s2Map[ord(s2[i]) - ord('a')] += 1
15
16        for i in range(26):
17            if s1Map[i] == s2Map[i]:
18                matched += 1
19
20        if s1Map == s2Map:
21            return True
22        
23        l = 0
24
25        for r in range(len(s1), len(s2)):
26    
27            if matched == 26:
28                return True
29            
30            s2Map[ord(s2[r]) - ord('a')] += 1
31            if s1Map[ord(s2[r]) - ord('a')] == s2Map[ord(s2[r]) - ord('a')]:
32                matched += 1
33            if s1Map[ord(s2[r]) - ord('a')] == s2Map[ord(s2[r]) - ord('a')] - 1:
34                matched -= 1
35            
36            s2Map[ord(s2[l]) - ord('a')] -= 1
37            if s1Map[ord(s2[l]) - ord('a')] == s2Map[ord(s2[l]) - ord('a')]:
38                matched += 1
39            if s1Map[ord(s2[l]) - ord('a')] == s2Map[ord(s2[l]) - ord('a')] + 1:
40                matched -= 1
41            
42            l += 1
43            
44
45        return matched == 26