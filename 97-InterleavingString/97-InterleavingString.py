# Last updated: 5/17/2026, 12:30:22 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3
4        # def recurse(i1, i2, i3):
5        #     if i3 == len(s3):
6        #         return True
7        #     if i1 >= len(s1) and i2 >= len(s2):
8        #         return False
9            
10        #     if i1 < len(s1) and s1[i1] == s3[i3] and i2 < len(s2) and s2[i2] == s3[i3]:
11        #         return recurse(i1 + 1, i2, i3 + 1) or recurse(i1, i2 + 1, i3 + 1)
12        #     elif i1 < len(s1) and s1[i1] == s3[i3]:
13        #         return recurse(i1 + 1, i2, i3 + 1)
14        #     elif i2 < len(s2) and s2[i2] == s3[i3]:
15        #         return recurse(i1, i2 + 1, i3 + 1)
16        #     else:
17        #         return False
18        
19        # return recurse(0, 0, 0)
20
21        # with dp
22
23        if len(s1) + len(s2) != len(s3):
24            return False
25
26        grid = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
27        grid[len(s2)][len(s1)] = True
28
29        for i in range(len(s2), -1, -1):
30            for j in range(len(s1), -1, -1):
31                if i < len(s2) and s3[i + j] == s2[i] and grid[i + 1][j] == True:
32                    grid[i][j] = True
33                if j < len(s1) and s3[i + j] == s1[j] and grid[i][j + 1] == True:
34                    grid[i][j] = True
35
36        return grid[0][0]
37
38
39