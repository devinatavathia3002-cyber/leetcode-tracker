# Last updated: 4/23/2026, 8:00:51 PM
1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        
4        largest = grid[0][0]
5        maxHeap = [] # value, coords
6        visited = set()
7
8        ROWS = len(grid)
9        COLS = len(grid[0])
10
11        heapq.heappush(maxHeap, [largest, (0, 0)])
12        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
13
14        while len(maxHeap) > 0:
15            curr = heapq.heappop(maxHeap)
16            val, coords = curr
17            x = coords[0]
18            y = coords[1]
19
20            if coords in visited:
21                continue
22            visited.add((coords))
23            largest = max(largest, val)
24
25            if x == ROWS - 1 and y == COLS - 1:
26                return largest
27
28            for direction in directions:
29                xCoord, yCoord = direction
30                newX, newY = xCoord + x, yCoord + y
31                if (newX < 0 or newY < 0 or 
32                    newX >= ROWS or newY >= COLS or
33                    (newX, newY) in visited):
34                    continue
35                heapq.heappush(maxHeap, [grid[newX][newY], (newX, newY)])