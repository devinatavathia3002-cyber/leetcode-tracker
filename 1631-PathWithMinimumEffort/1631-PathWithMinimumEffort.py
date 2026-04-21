# Last updated: 4/20/2026, 11:03:14 PM
1class Solution:
2    def minimumEffortPath(self, heights: List[List[int]]) -> int:
3        
4        ROWS = len(heights)
5        COLS = len(heights[0])
6        minHeap = [[0, 0, 0]] # difference, r, c
7
8        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
9        visited = set()
10
11        while minHeap:
12            curr = heapq.heappop(minHeap)
13            diff, r, c = curr
14            if (r, c) in visited:
15                continue
16
17            visited.add((r, c))
18
19            if r == ROWS - 1 and c == COLS - 1:
20                return diff
21            
22            for direction in directions:
23                row, col = direction
24                newR, newC = row + r, col + c
25                if (newR < 0 or newC < 0 or 
26                    newR >= ROWS or newC >= COLS):
27                    continue
28                difference = max(diff, abs(heights[newR][newC] - heights[r][c]))
29                heapq.heappush(minHeap, [difference, newR, newC])