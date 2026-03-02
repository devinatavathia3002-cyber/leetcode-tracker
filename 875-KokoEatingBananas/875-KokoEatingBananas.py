# Last updated: 3/1/2026, 10:47:11 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        
4        l = 1
5        r = max(piles)
6        m = max(piles)
7
8        while l < r:
9            m = ((r - l) // 2) + l
10            hours = 0
11
12            hours = sum(math.ceil(p / m) for p in piles)
13            
14            if hours <= h:
15                r = m
16            else:
17                l = m + 1
18
19        return r