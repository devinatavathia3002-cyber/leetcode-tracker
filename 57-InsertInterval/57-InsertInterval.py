# Last updated: 5/2/2026, 9:08:09 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4        newS = newInterval[0]
5        newE = newInterval[1]
6
7        for i in range(len(intervals)):
8            start, end = intervals[i]
9            if newE < start:
10                res.append(newInterval)
11                return res + intervals[i: len(intervals)]
12            elif newS > end:
13                res.append([start, end])
14            else:
15                newInterval[0] = min(newS, start)
16                newInterval[1] = max(newE, end)
17                newS, newE = newInterval
18
19        res.append(newInterval)
20        return res