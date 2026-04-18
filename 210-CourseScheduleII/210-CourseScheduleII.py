# Last updated: 4/17/2026, 9:10:38 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        
4        output = []
5        taken = 0
6        q = deque()
7        indegree = [0] * numCourses
8        adj = defaultdict(list)
9
10        for num in prerequisites:
11            course, pre = num
12            indegree[course] += 1
13            adj[pre].append(course)
14        
15        for num in range(numCourses):
16            if indegree[num] == 0:
17                q.append(num)
18        
19        while q:
20            length = len(q)
21            for i in range(length):
22                course = q.popleft()
23                output.append(course)
24                for num in adj[course]:
25                    indegree[num] -= 1
26                    if indegree[num] == 0:
27                        q.append(num)
28                adj[course] = []
29                taken += 1
30
31        return output if taken == numCourses else []