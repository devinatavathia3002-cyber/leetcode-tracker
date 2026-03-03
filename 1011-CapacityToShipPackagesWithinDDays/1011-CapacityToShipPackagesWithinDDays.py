# Last updated: 3/2/2026, 8:21:28 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        
4        r = sum(weights)
5        l = max(weights)
6
7        while l < r:
8
9            m = ((r - l) // 2) + l
10            totalW = 0
11            daysC = 0
12
13            for weight in weights:
14                if totalW + weight > m:
15                    daysC += 1
16                    totalW = weight
17                else:
18                    totalW += weight
19            
20            if totalW > 0:
21                daysC += 1
22            
23            if daysC <= days:
24                r = m
25            else:
26                l = m + 1
27
28        return r