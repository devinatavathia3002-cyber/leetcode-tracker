# Last updated: 7/28/2026, 10:14:04 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        count = defaultdict(int)
4        adj = defaultdict(list)
5
6        for prereq in prerequisites:
7            crs, before = prereq
8            adj[crs].append(before)
9            count[before] += 1
10
11        q = deque()
12        for i in range(numCourses):
13            if i not in count:
14                q.append(i)
15        
16        output = []
17        while q:
18            popped = q.pop()
19            output.append(popped)
20            for crs in adj[popped]:
21                count[crs] -= 1
22                if count[crs] == 0:
23                    q.append(crs)
24
25        return output[::-1] if len(output) == numCourses else []
26