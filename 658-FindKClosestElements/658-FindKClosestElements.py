# Last updated: 3/5/2026, 8:31:28 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        
4        l = 0
5        r = 0
6
7        output = [0] * k
8        difference = float("infinity")
9
10        testing = 0
11
12        while r < len(arr):
13
14            if (r - l + 1) > k:
15                testing -= abs(x - arr[l])
16                l += 1
17            
18            testing += abs(x - arr[r])
19
20            if (r - l + 1) == k:
21                if testing < difference:
22                    difference = testing
23                    output = arr[l:r+1]
24
25            r += 1
26        
27        return output