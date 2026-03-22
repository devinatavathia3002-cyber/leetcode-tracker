# Last updated: 3/22/2026, 4:55:59 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        
4        # monotonic stack
5        s = []
6
7        for i in range(len(temperatures) - 1, -1, -1):
8            while s and s[-1][0] <= temperatures[i]:
9                s.pop()
10                
11            if len(s) == 0:
12                s.append([temperatures[i], i])
13                temperatures[i] = 0
14            else:
15                warmer, index = s[-1]
16                s.append([temperatures[i], i])
17                temperatures[i] = (index - i)
18        
19        return temperatures