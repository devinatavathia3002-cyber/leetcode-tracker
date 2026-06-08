# Last updated: 6/7/2026, 5:17:07 PM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        
4        q = deque()
5        q.append((sr, sc))
6
7        orig = image[sr][sc]
8        if orig == color:
9            return image
10            
11        image[sr][sc] = color
12        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
13
14        ROWS = len(image)
15        COLS = len(image[0])
16
17        while q:
18            for _ in range(len(q)):
19                x, y = q.popleft()
20                for val in directions:
21                    r, c = val
22                    newRow = r + x
23                    newCol = c + y
24                    if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS and image[newRow][newCol] == orig:
25                        image[newRow][newCol] = color
26                        q.append((newRow, newCol))
27
28        return image