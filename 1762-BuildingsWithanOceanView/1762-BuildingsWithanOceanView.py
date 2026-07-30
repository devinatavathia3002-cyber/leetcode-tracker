# Last updated: 7/29/2026, 6:09:12 PM
1class Solution:
2    def findBuildings(self, heights: List[int]) -> List[int]:
3        stack = []
4        output = []
5
6        for i in range(len(heights) - 1, -1, -1):
7            curr = heights[i]
8            while stack and stack[-1] < curr:
9                stack.pop()
10            if len(stack) == 0:
11                output.append(i)
12            stack.append(curr)
13        
14        return output[::-1]