# Last updated: 5/10/2026, 8:09:39 PM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        
4        output = []
5        l, r = 0, 0
6
7        count = defaultdict(int)
8        for i in range(len(s)):
9            char = s[i]
10            count[char] = i
11
12        while r < len(s):
13
14            i = l
15            while i <= r:
16                curr = s[i]
17                r = max(r, count[curr])  # get farthest index
18                i += 1
19            
20            output.append(r - l + 1)
21            l = r + 1
22            r += 1
23
24        return output