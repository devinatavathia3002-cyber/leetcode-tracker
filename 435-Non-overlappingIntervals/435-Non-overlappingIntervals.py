# Last updated: 5/2/2026, 10:17:06 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        output = 0
4        intervals.sort()
5        lastElement = intervals[0]
6
7        for i in range(1, len(intervals)):
8            s, e = intervals[i]
9            prevS, prevE = lastElement
10
11            if prevE <= s:
12                lastElement = [s, e]
13            else:
14                output += 1
15                if prevE > e:
16                    lastElement = [s, e]
17
18        return output