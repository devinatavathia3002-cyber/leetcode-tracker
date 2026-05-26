# Last updated: 5/25/2026, 11:21:33 PM
1class Solution:
2    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
3        dp = {}
4
5        def recurse(index):
6            if index >= len(days):
7                return 0
8            
9            if index in dp:
10                return dp[index]
11            
12            dp[index] = float('inf')
13            for i in range(len(costs)):
14                val = costs[i]
15                newDayIndex = index
16                if i == 0:
17                    newDay = days[index] + 1 - 1
18                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
19                        newDayIndex += 1
20                if i == 1:
21                    newDay = days[index] + 7 - 1
22                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
23                        newDayIndex += 1
24                if i == 2:
25                    newDay = days[index] + 30 - 1
26                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
27                        newDayIndex += 1
28                dp[index] = min(dp[index], val + recurse(newDayIndex))
29            
30            return dp[index]
31        
32        return recurse(0)