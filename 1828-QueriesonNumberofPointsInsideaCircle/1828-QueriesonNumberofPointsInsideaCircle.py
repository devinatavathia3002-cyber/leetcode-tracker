# Last updated: 8/1/2026, 12:44:29 PM
1class Solution:
2    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
3        res = [0] * len(queries)
4        index = 0
5
6        for query in queries:
7            qx, qy, r = query
8            amt = 0
9            for point in points:
10                px, py = point
11                # calc
12                if ((px - qx) ** 2 + (py - qy) ** 2) <= (r ** 2):
13                    amt += 1
14
15            res[index] = amt
16            index += 1
17
18        return res