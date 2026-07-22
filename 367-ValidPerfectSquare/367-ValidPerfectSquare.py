# Last updated: 7/21/2026, 9:48:40 PM
1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        if num == 1:
4            return True
5            
6        l, r = 1, (num // 2)
7
8        while l <= r:
9            mid = ((r - l) // 2) + l
10            square = mid * mid
11
12            if square < num:
13                l = mid + 1
14            elif square > num:
15                r = mid - 1
16            else:
17                return True
18        
19        return False