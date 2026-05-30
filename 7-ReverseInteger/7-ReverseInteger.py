# Last updated: 5/29/2026, 7:42:40 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        
4        MIN = -2147483648
5        MAX = 2147483648
6
7        res = 0
8        while x:
9            # get the last digit, cut it off
10            last = int(math.fmod(x, 10))
11            x = int(x / 10)
12
13            # check to make sure x is not out of bounds
14            if (res > MAX // 10 or (res == MAX // 10 and last > MAX % 10)):
15                return 0
16            if (res < MIN // 10 or (res == MIN // 10 and last < MIN % 10)):
17                return 0
18
19            # add last to res
20            res = (res * 10) + last
21
22        return res