# Last updated: 4/19/2026, 4:44:45 PM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        adj = defaultdict(list) # a --> [b, a/b]
4        for i, val in enumerate(equations):
5            top, bottom = val
6            adj[top].append([bottom, values[i]])
7            adj[bottom].append([top, 1 / values[i]])
8        
9        output = []
10
11        def bfs(src, tar):
12            q = deque()
13            visited = set()
14            q.append((src, 1))
15
16            while q:
17                node, w = q.popleft()
18                if node == tar:
19                    return w
20                visited.add(node)
21                for nei in adj[node]:
22                    if nei[0] in visited:
23                        continue
24                    visited.add(nei[0])
25                    q.append((nei[0], nei[1] * w))
26            return -1
27
28        for q in queries:
29            source, target = q
30            if source not in adj.keys():
31                output.append(-1)
32            else:
33                output.append(bfs(source, target))
34        
35        return output