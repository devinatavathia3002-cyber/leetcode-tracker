# Last updated: 2/24/2026, 10:34:01 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        
4        # stack with map (index, height)
5        s = []
6        maxArea = 0
7
8        for i in range(len(heights)):
9            
10            start = i
11            while s and s[-1][1] > heights[i]:
12                index, height = s.pop()
13                maxArea = max(maxArea, height * (i - index))
14                start = index
15            
16            s.append((start, heights[i]))
17        
18
19        end = len(heights)
20        while s:
21            index, height = s.pop()
22            maxArea = max(maxArea, height * (end - index))
23
24        return maxArea
25        