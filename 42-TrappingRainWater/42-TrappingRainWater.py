# Last updated: 2/27/2026, 5:51:02 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        
4        l = 0
5        r = len(height) - 1
6
7        maxLeft = height[l]
8        maxRight = height[r]
9
10        output = 0
11
12        while l < r:
13            maxLeft = max(maxLeft, height[l])
14            maxRight = max(maxRight, height[r])
15            container = 0
16
17            if maxLeft <= maxRight:
18                container = (maxLeft - height[l])
19                l += 1
20            else:
21                container = (maxRight - height[r])
22                r -= 1
23            if container > 0:
24                output += container
25
26        return output