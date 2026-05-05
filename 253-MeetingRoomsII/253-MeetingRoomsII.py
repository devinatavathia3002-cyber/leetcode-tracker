# Last updated: 5/4/2026, 11:24:45 PM
1"""
2Definition of Interval:
3class Interval(object):
4    def __init__(self, start, end):
5        self.start = start
6        self.end = end
7"""
8
9class Solution:
10    def minMeetingRooms(self, intervals: List[Interval]) -> int:
11        
12        start = sorted([i[0] for i in intervals])
13        end = sorted([i[1] for i in intervals])
14
15        res, curr = 0, 0
16        s, e = 0, 0
17
18        while s < len(start):
19            if start[s] < end[e]:
20                curr += 1
21                s += 1
22            else:
23                curr -= 1
24                e += 1
25            res = max(res, curr)
26
27        return res