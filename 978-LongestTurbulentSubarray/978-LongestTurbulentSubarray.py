# Last updated: 7/11/2026, 8:14:00 PM
1class Solution:
2    def maxTurbulenceSize(self, arr: List[int]) -> int:
3        # [2,4,3,2,2,5,1,4]
4        if len(arr) <= 1:
5            return 1
6
7        l, r = 0, 0
8        longest = 1
9        curr = 1
10
11        former = 0
12
13        while r < len(arr) - 1:
14            first = arr[r]
15            second = arr[r + 1]
16
17            if first == second:
18                curr = 1
19                l = r + 1
20                former = 0
21            elif first < second:
22                if former == 1 or former == 0:
23                    curr += 1
24                    longest = max(longest, curr)
25                else:
26                    curr = 2
27                    l = r
28                former = -1
29            else:
30                if former == -1 or former == 0:
31                    curr += 1
32                    longest = max(longest, curr)
33                else:
34                    curr = 2
35                    l = r
36                former = 1
37            r += 1
38
39        return longest