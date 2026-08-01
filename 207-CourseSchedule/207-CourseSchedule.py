# Last updated: 8/1/2026, 3:01:37 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        count = defaultdict(int)
4        adj = defaultdict(list)
5        total = 0
6
7        for crs in range(numCourses):
8            count[crs] = 0
9
10        for prereq in prerequisites:
11            crs, bf = prereq
12            adj[crs].append(bf)
13            count[bf] += 1
14        
15        q = deque()
16        for key, val in count.items():
17            if val == 0:
18                q.append(key)
19        
20        while q:
21            crs = q.popleft()
22            total += 1
23            for val in adj[crs]:
24                count[val] -= 1
25                if count[val] == 0:
26                    q.append(val)
27        
28        return True if total == numCourses else False
29