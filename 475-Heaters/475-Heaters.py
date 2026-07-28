# Last updated: 7/27/2026, 8:12:37 PM
1class Solution:
2    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
3        l, r = 0, max(max(houses), max(heaters))
4        heaters = sorted(heaters)
5        houses = sorted(houses)
6
7        def canCover(radius):
8            i = 0
9            for house in houses:
10                while i < len(heaters) and abs(heaters[i] - house) > radius:
11                    i += 1
12                if i >= len(heaters):
13                    return False
14            return True
15
16        while l <= r:
17            mid = ((r - l) // 2) + l
18            if canCover(mid):
19                r = mid - 1
20            else:
21                l = mid + 1
22
23        return l