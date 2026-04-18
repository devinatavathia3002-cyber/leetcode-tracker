# Last updated: 4/17/2026, 10:51:51 PM
1class Solution:
2    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
3        
4        pre = defaultdict(list)
5        for course in prerequisites:
6            prereq, curr = course
7            pre[curr].append(prereq)
8        
9        output = [False] * len(queries)
10        
11        def dfs(start, end, course, visited):
12            if course in visited:
13                return False
14            if course == end:
15                return True
16            visited.add(course)
17            for num in pre[course]:
18                if dfs(start, end, num, visited):
19                    return True
20            return False
21        
22        for i in range(len(queries)):
23            beg, end = queries[i]
24            if dfs(end, beg, end, set()):
25                output[i] = True
26        
27        return output