# Last updated: 7/14/2026, 10:22:44 PM
1class Solution:
2    def minimumDeleteSum(self, s1: str, s2: str) -> int:
3        dp = defaultdict(int)
4        def delete(i, j):
5            if (i, j) in dp:
6                return dp[(i, j)]
7            if i >= len(s1) and j >= len(s2):
8                return 0
9            elif i >= len(s1):
10                total = 0
11                for k in range(j, len(s2)):
12                    total += ord(s2[k])
13                dp[(i, j)] = total
14            elif j >= len(s2):
15                total = 0
16                for k in range(i, len(s1)):
17                    total += ord(s1[k])
18                dp[(i, j)] = total
19            
20            else:
21                # case where both i and j are in bounds
22                if s1[i] == s2[j]:
23                    dp[(i, j)] = delete(i + 1, j + 1)
24                else:
25                    dp[(i, j)] = min(ord(s1[i]) + delete(i + 1, j), 
26                                     ord(s2[j]) + delete(i, j + 1))
27            
28            return dp[(i, j)]
29        
30        return delete(0, 0)