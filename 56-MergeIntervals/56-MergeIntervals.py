# Last updated: 5/2/2026, 9:50:56 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        output = []
4        intervals.sort(key = lambda x: x[0])
5        output.append(intervals[0])
6
7        for i in range(1, len(intervals)):
8            start, end = output[-1]
9            newS, newE = intervals[i]
10
11            if end < newS:
12                output.append([newS, newE])
13            else:
14                output[-1][0] = min(start, newS)
15                output[-1][1] = max(end, newE)
16
17        return output