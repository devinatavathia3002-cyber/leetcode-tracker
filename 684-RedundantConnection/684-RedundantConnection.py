# Last updated: 4/18/2026, 11:38:07 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        
4        # topological sort
5        q = deque()
6        adj = defaultdict(list)
7        indegree = defaultdict(int)
8        for edge in edges:
9            beg, end = edge
10            adj[beg].append(end)
11            adj[end].append(beg)
12            indegree[beg] += 1
13            indegree[end] += 1
14        
15        for val in indegree.keys():
16            if indegree[val] == 1:
17                q.append(val)
18        
19        while q:
20            length = len(q)
21            for i in range(length):
22                curr = q.popleft()
23                for val in adj[curr]:
24                    indegree[val] -= 1
25                    indegree[curr] -= 1
26                    if indegree[val] == 1:
27                        q.append(val)      
28        
29        for i in range(len(edges) - 1, -1, -1):
30            u, v = edges[i]
31            if indegree[u] >= 2 and indegree[v] >= 2:
32                return edges[i]
33        
34        return edges[0]
35