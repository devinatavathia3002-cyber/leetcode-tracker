# Last updated: 4/15/2026, 10:12:52 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        
4        rows = len(heights)
5        cols = len(heights[0])
6        pac = set()
7        atl = set()
8        output = []
9
10        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
11
12        def dfs(r, c, visited, prev):
13            if r < 0 or c < 0 or r >= rows or c >= cols:
14                return
15            curr = heights[r][c]
16            if prev > curr or (r, c) in visited:
17                return
18            
19            visited.add((r, c))
20            for num in directions:
21                x, y = num
22                dfs(r + x, c + y, visited, heights[r][c])
23        
24
25        for r in range(rows):
26            for c in range(cols):
27                if r == 0 or c == 0: # pacific
28                    dfs(r, c, pac, heights[r][c])
29                if r == rows - 1 or c == cols - 1: # atlantic
30                    dfs(r, c, atl, heights[r][c])
31        
32        for r in range(rows):
33            for c in range(cols):
34                if (r, c) in pac and (r, c) in atl:
35                    output.append([r, c])
36
37        return output