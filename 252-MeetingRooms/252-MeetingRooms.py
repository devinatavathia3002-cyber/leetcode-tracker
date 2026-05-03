# Last updated: 5/2/2026, 10:54:30 PM
1"""
2Definition of Interval:
3class Interval(object):
4    def __init__(self, start, end):
5        self.start = start
6        self.end = end
7"""
8
9class Solution:
10    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
11        if len(intervals) == 0:
12            return True
13        intervals.sort(key = lambda x: x[0])
14        prev = intervals[0]
15
16        for i in range(1, len(intervals)):
17            start, end = intervals[i]
18            prevS, prevE = prev
19
20            if prevE <= start:
21                prev = [start, end]
22            else:
23                return False
24
25        return True