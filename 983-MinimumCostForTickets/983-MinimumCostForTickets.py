# Last updated: 6/10/2026, 11:30:18 PM
1class Solution:
2    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
3        dp = [0] * (len(days) + 1)
4
5        for i in range(len(days) - 1, -1, -1):
6            
7            # skip one day
8            nextIndex = i
9            newCovered = days[i] + 1 - 1
10            while nextIndex < len(days) and days[nextIndex] <= newCovered:
11                nextIndex += 1
12            skipOne = dp[nextIndex] + costs[0]
13    
14            # skip seven days
15            nextIndex = i
16            newCovered = days[i] + 7 - 1
17            while nextIndex < len(days) and days[nextIndex] <= newCovered:
18                nextIndex += 1
19            skipSeven = dp[nextIndex] + costs[1]
20                
21            # skip 30 days
22            nextIndex = i
23            newCovered = days[i] + 30 - 1
24            while nextIndex < len(days) and days[nextIndex] <= newCovered:
25                nextIndex += 1
26            skipThirty = dp[nextIndex] + costs[2]
27
28            dp[i] = min(skipOne, skipSeven, skipThirty)
29        
30        return dp[0]