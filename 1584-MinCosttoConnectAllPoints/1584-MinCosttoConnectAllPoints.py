# Last updated: 4/23/2026, 1:24:05 AM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        # prim's algo (optimal)
4
5        res = 0
6        visited = [False] * len(points)
7        distances = [float("inf")] * len(points)
8        edges = 0
9        node = 0
10
11        while edges < len(points) - 1:
12            x, y = points[node]
13            nextPoint = -1
14            visited[node] = True
15
16            for i in range(len(points)):
17                if visited[i]:
18                    continue
19                xCord, yCord = points[i]
20                distance = abs(xCord - points[node][0]) + abs(yCord - points[node][1])
21                distances[i] = min(distances[i], distance)
22                if nextPoint == -1 or distances[i] < distances[nextPoint]:
23                    nextPoint = i
24
25            node = nextPoint
26            res += distances[nextPoint]
27            edges += 1
28        
29        return res
30
31
32