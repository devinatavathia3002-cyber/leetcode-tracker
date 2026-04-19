# Last updated: 4/18/2026, 9:44:17 PM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        
4        visited = [False] * n
5        counter = 0
6        pre = defaultdict(list)
7        for edge in edges:
8            beg, end = edge
9            pre[beg].append(end)
10            pre[end].append(beg)
11
12        def dfs(curr, parent):
13            if visited[curr] == True:
14                return
15            visited[curr] = True
16            for edge in pre[curr]:
17                if edge == parent:
18                    continue
19                dfs(edge, curr)
20
21        for num in range(n):
22            if visited[num] == False:
23                dfs(num, -1)
24                counter += 1
25
26        return counter