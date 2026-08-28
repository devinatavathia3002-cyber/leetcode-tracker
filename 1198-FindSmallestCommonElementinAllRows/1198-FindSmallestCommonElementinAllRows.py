# Last updated: 8/27/2026, 7:19:28 PM
1class Solution:
2    def smallestCommonElement(self, mat: List[List[int]]) -> int:
3        smallest = set()
4        counts = defaultdict(int)
5        minVal = mat[0][0]
6
7        ROWS = len(mat)
8        COLS = len(mat[0])
9
10        for r in range(ROWS):
11            if mat[r][0] > minVal:
12                minVal = mat[r][0]
13        
14        for c in range(COLS):
15            curr = mat[0][c]
16            if curr >= minVal:
17                smallest.add(curr)
18                counts[curr] = 0
19        
20        for r in range(ROWS):
21            for c in range(COLS):
22                val = mat[r][c]
23                if val in smallest:
24                    counts[val] += 1
25        
26        minimum = []
27        for key, item in counts.items():
28            if item == ROWS:
29                minimum.append(key)
30        
31        return min(minimum) if minimum else -1
32