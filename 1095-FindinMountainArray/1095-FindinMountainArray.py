# Last updated: 3/6/2026, 5:18:03 PM
1class Solution:
2    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
3        
4        # try this without caching 
5        # first, find peak
6
7        l, r = 1, mountainArr.length() - 2
8
9        while l <= r:
10            m = ((r - l) // 2) + l
11
12            right = mountainArr.get(m + 1)
13            left = mountainArr.get(m - 1)
14            mid = mountainArr.get(m)
15
16            if left < mid < right:
17                # on left side
18                l = m + 1
19            elif left > mid > right:
20                # on right side
21                r = m - 1
22            else:
23                break
24        
25        peak = m
26        peakVal = mountainArr.get(peak)
27        if peakVal == target:
28            return peak
29
30        # search left side
31        l, r = 0, peak - 1
32
33        while l <= r:
34            m = ((r - l) // 2) + l
35            mid = mountainArr.get(m)
36
37            if mid < target:
38                l = m + 1
39            elif mid > target:
40                r = m - 1
41            else:
42                return m
43        
44        # search right side
45        l, r = peak + 1, mountainArr.length() - 1
46
47        while l <= r:
48            m = ((r - l) // 2) + l
49            mid = mountainArr.get(m)
50
51            if mid < target:
52                r = m - 1
53            elif mid > target:
54                l = m + 1
55            else:
56                return m
57        
58        return -1 