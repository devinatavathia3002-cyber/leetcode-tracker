# Last updated: 4/21/2026, 12:29:52 AM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        
4        visited = set()
5        total = 0
6        minHeap = [[0, k]] # sum, value
7        adj = defaultdict(list) # [time, endNode]
8        for time in times:
9            src, dest, weight = time
10            adj[src].append([weight, dest])
11
12        while minHeap and len(visited) < n:
13            cumulative, val = heapq.heappop(minHeap)
14            if val in visited:
15                continue
16            visited.add(val)
17            total = cumulative
18
19            for node in adj[val]:
20                time, value = node
21                heapq.heappush(minHeap, [cumulative + time, value])
22
23        print(total)
24        return total if len(visited) == n else -1
25
26