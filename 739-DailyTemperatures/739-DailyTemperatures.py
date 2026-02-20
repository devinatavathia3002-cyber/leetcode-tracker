# Last updated: 2/19/2026, 9:36:17 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        
4        # monotonic stack
5        s = []
6
7        for i in range(len(temperatures) - 1, -1, -1):
8            if len(s) == 0:
9                s.append([temperatures[i], i])
10                temperatures[i] = 0
11            
12            else:
13                while s and s[-1][0] <= temperatures[i]:
14                    s.pop()
15                
16                if len(s) == 0:
17                    s.append([temperatures[i], i])
18                    temperatures[i] = 0
19                else:
20                    warmer, index = s[-1]
21                    s.append([temperatures[i], i])
22                    temperatures[i] = (index - i)
23        
24        return temperatures