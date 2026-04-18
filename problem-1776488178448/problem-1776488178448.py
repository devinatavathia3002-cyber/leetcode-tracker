# Last updated: 4/17/2026, 9:56:18 PM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        
4        visited = set()
5        up = defaultdict(list)
6
7        for edge in edges:
8            beg, end = edge
9            up[beg].append(end)
10            up[end].append(beg)
11        
12        def dfs(curr, parent):
13            if curr in visited:
14                return False
15            visited.add(curr)
16            for num in up[curr]:
17                if num == parent:
18                    continue
19                if not dfs(num, curr):
20                    return False
21            return True
22        
23        return dfs(0, -1) and len(visited) == n 