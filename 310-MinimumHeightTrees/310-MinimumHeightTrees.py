# Last updated: 4/19/2026, 10:07:01 PM
1class Solution:
2    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
3        
4        if n == 1:
5            return [0]
6            
7        adj = defaultdict(list)
8        indegree = defaultdict(int)
9        for edge in edges:
10            beg, end = edge
11            adj[beg].append(end)
12            adj[end].append(beg)
13            indegree[beg] += 1
14            indegree[end] += 1
15        remaining = n
16
17        q = deque()
18        for num in indegree.keys():
19            if indegree[num] == 1:
20                q.append(num)
21        
22        while remaining > 2:
23            size = len(q)
24            remaining -= size
25            for i in range(size):
26                curr = q.popleft()
27                for nei in adj[curr]:
28                    indegree[nei] -= 1
29                    if indegree[nei] == 1:
30                        q.append(nei)
31
32        return list(q)