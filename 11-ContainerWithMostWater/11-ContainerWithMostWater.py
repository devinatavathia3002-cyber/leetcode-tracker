# Last updated: 2/14/2026, 12:26:10 PM
1class Solution:
2    def maxArea(self, heights: List[int]) -> int:
3        
4        left = 0
5        right = len(heights) - 1
6        mostWtr = 0
7
8        while left != right:
9            container = (right - left) * min(heights[right], heights[left])
10            if heights[right] <= heights[left]:
11                right -= 1
12            else:
13                left += 1
14            
15            mostWtr = max(container, mostWtr)
16
17        
18        return mostWtr