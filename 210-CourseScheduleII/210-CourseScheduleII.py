# Last updated: 6/13/2026, 8:04:25 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        
4        output = []
5        adj = defaultdict(list)
6        count = defaultdict(int)
7        for course in prerequisites:
8            end, beg = course
9            adj[end].append(beg)
10            count[beg] += 1
11
12        q = deque()
13        for i in range(numCourses):
14            if i not in count:
15                q.append(i)
16
17        while q:
18            course = q.popleft()
19            output.append(course)
20
21            for prereq in adj[course]:
22                count[prereq] -= 1
23                if count[prereq] <= 0:
24                    q.append(prereq)
25
26        return output[::-1] if len(output) == numCourses else []