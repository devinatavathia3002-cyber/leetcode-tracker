# Last updated: 7/21/2026, 9:30:52 PM
1class Solution:
2    def arrangeCoins(self, n: int) -> int:
3        # (n/2) * (n + 1)
4        l, r = 1, n
5        res = 0
6
7        while l <= r:
8            mid = ((r - l) // 2) + l
9            coins = mid * (mid + 1) // 2
10
11            if coins > n:
12                r = mid - 1
13            elif coins < n:
14                l = mid + 1
15                res = mid
16            else:
17                return mid
18        
19        return res