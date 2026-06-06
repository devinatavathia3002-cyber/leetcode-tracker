# Last updated: 6/6/2026, 4:47:21 PM
1class DetectSquares:
2
3    def __init__(self):
4        self.freq = defaultdict(int)
5        self.points = []
6
7    def add(self, point: List[int]) -> None:
8        self.freq[tuple(point)] += 1
9        self.points.append(point)
10
11    def count(self, point: List[int]) -> int:
12        px, py = point
13        res = 0
14        for x, y in self.points:
15            if (x == px) or (y == py) or abs(px - x) != abs(py - y):
16                continue
17            else:
18                res += self.freq[(x, py)] * self.freq[(px, y)]
19        return res
20