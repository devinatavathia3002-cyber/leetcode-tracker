# Last updated: 5/10/2026, 7:22:44 PM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        
4        bool1 = False
5        bool2 = False
6        bool3 = False
7
8        valid = []
9
10        f, m, l = target
11
12        for triplet in triplets:
13            a, b, c = triplet
14            if a > f or b > m or c > l:
15                continue
16            valid.append(triplet)
17        
18        for triplet in valid:
19            a, b, c = triplet
20            if a == f:
21                bool1 = True
22            if b == m:
23                bool2 = True
24            if c == l:
25                bool3 = True
26
27        return bool1 and bool2 and bool3