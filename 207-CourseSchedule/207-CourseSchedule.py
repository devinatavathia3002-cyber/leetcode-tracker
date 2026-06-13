# Last updated: 6/13/2026, 4:49:33 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        
4        pre = defaultdict(list)
5        visited = set()
6        for pair in prerequisites:
7            past, post = pair
8            pre[past].append(post)
9        
10        def dfs(num):
11            nonlocal visited
12            if pre[num] == []:
13                return True
14            if num in visited:
15                return False
16            
17            visited.add(num)
18            for prereq in pre[num]:
19                if not dfs(prereq):
20                    return False
21            
22            visited.remove(num)
23            pre[num] = []
24            return True
25            
26        for num in range(numCourses):
27            if not dfs(num):
28                return False
29        return True