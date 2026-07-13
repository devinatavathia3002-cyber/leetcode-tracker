# Last updated: 7/13/2026, 12:15:54 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        adj = defaultdict(list)
4        visited = set()
5        for edge in edges:
6            s, e = edge
7            adj[s].append(e)
8            adj[e].append(s)
9        
10
11        def findLoop(v, parent):            
12            if v in visited:
13                return False
14            
15            visited.add(v)
16            for edge in adj[v]:
17                if edge == parent:
18                    continue
19
20                if findLoop(edge, v) == False:
21                    return False
22            
23            return True
24
25        return findLoop(0, -1) and len(visited) == n
26